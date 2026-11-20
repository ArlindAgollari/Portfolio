"""Run with Python 3 and NumPy. Writes comparison and selected-design CSV files."""
from itertools import product
from pathlib import Path
import csv
import numpy as np

OUT = Path(__file__).resolve().parent
E, FY, RHO, G = 69e9, 240e6, 2700, 9.81
# OD and wall (inches). One stock size per bottom chord, upper chord, and web group.
STOCK = np.array([(1,.125),(2,.063),(2.25,.065),(2.5,.065),(3,.063),(2.5,.125),(3,.125)])
D, T = (STOCK * .0254).T
AREA = np.pi/4*(D**2-(D-2*T)**2)
INERTIA = np.pi/64*(D**4-(D-2*T)**4)
COMBOS = np.array(list(product(range(len(STOCK)), repeat=3)))

def write(name, header, rows):
    with (OUT/name).open('w', newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(header)
        writer.writerows(rows)

def solve(kind, panels, height):
    pitch = 12/panels
    xy = [(i*pitch,0) for i in range(panels+1)]
    names = [f'B{i}' for i in range(panels+1)]
    edges = [(i,i+1,0) for i in range(panels)]
    first = len(xy)
    upper = np.arange(panels)+.5 if kind=='Warren' else np.arange(1,panels)
    for i,x in enumerate(upper):
        xy.append((x*pitch,height))
        names.append(f'T{i+1}')
    edges += [(i,i+1,1) for i in range(first,len(xy)-1)]
    for i in range(len(upper)):
        top = first+i
        if kind=='Warren':
            joints = [i,i+1]
        else:
            j=i+1
            joints=[j]
            if j==1: joints.append(0)
            if j==panels-1: joints.append(panels)
            if j<panels/2: joints.append(j+1)
            if j>panels/2: joints.append(j-1)
        edges.extend((b,top,2) for b in joints)
    xy=np.array(xy)
    n=len(xy)
    a,b,group=np.array(edges).T
    dr=xy[b]-xy[a]
    length=np.linalg.norm(dr,axis=1)
    # B maps joint displacements to bar extensions.
    B=np.zeros((len(edges),2*n))
    for i,(j,k,_) in enumerate(edges):
        B[i,2*j:2*j+2]=-dr[i]/length[i]
        B[i,2*k:2*k+2]=dr[i]/length[i]
    free=np.setdiff1d(np.arange(2*n),[0,1,2*panels+1])
    H=np.linalg.inv(B[:,free].T)
    idx=COMBOS[:,group]
    area=AREA[idx]
    mass=RHO*area*length
    loads=np.zeros((len(idx),2*n))
    loads[:,1:2*panels+2:2]=-15000/panels
    loads[:,[1,2*panels+1]] *= .5
    for i,(j,k,_) in enumerate(edges):
        loads[:,[2*j+1,2*k+1]]-=mass[:,i,None]*G/2
    force=loads[:,free]@H.T
    pcr=np.pi**2*E*INERTIA[idx]/length**2
    capacity=np.where(force<0,np.minimum(FY*area,pcr),FY*area)
    fos=capacity/np.maximum(abs(force),1e-12)
    disp=np.zeros_like(loads)
    disp[:,free]=(force*length/(area*E))@H
    delta=np.max(abs(disp[:,1::2]),axis=1)*1000
    ok=(fos.min(axis=1)>=2)&(delta<=25)
    if not np.any(ok): return None
    best=np.argmin(np.where(ok,mass.sum(axis=1),np.inf))
    q=best
    return dict(kind=kind,panels=panels,height=height,kg=2*mass[q].sum(),mm=delta[q],
        sf=fos[q].min(),names=names,xy=xy,edges=edges,B=B,free=free,H=H,
        stock=idx[q],length=length,mass=mass[q],load=loads[q],force=force[q],
        disp=disp[q],fos=fos[q],pcr=pcr[q])

def run():
    cases=[solve(k,p,h) for k,p,h in product(['Warren','Pratt'],[4,6,8],[2,2.5,3])]
    feasible=[c for c in cases if c]
    best=min(feasible,key=lambda c:c['kg'])
    write('iterations.csv',['layout','panels','height_m','two_truss_kg','max_vertical_mm','min_FoS'],
          [[c[key] for key in ['kind','panels','height','kg','mm','sf']] for c in feasible])
    c=best
    B,free,force=c['B'],c['free'],c['force']
    idx=c['stock']
    K=B.T@np.diag(E*AREA[idx]/c['length'])@B
    u=np.zeros_like(c['disp'])
    u[free]=np.linalg.solve(K[np.ix_(free,free)],c['load'][free])
    assert np.allclose(u,c['disp'])
    reactions=B.T@force-c['load']
    assert np.max(abs(reactions[free]))<1e-7
    assert np.isclose(reactions[1::2].sum(),15000+c['kg']*G/2)
    crit=2*np.argmax(abs(u[1::2]))+1
    unit=np.zeros_like(u)
    unit[crit]=-1
    virtual=c['H']@unit[free]
    terms=1000*force*virtual*c['length']/(E*AREA[idx])
    assert np.isclose(terms.sum(),c['mm'])
    write('members.csv',['from','to','group','length_m','OD_in','wall_in','area_mm2','I_mm4','mass_kg','force_kN_tension_positive','stress_MPa','Euler_kN','FoS','virtual_force_N_per_N','deflection_term_mm'],
          [[c['names'][a],c['names'][b],['bottom','top','web'][g],c['length'][i],*STOCK[idx[i]],AREA[idx[i]]*1e6,INERTIA[idx[i]]*1e12,c['mass'][i],force[i]/1000,force[i]/AREA[idx[i]]/1e6,c['pcr'][i]/1000,c['fos'][i],virtual[i],terms[i]] for i,(a,b,g) in enumerate(c['edges'])])
    write('joints.csv',['joint','x_m','y_m','combined_downward_kN','reaction_x_kN','reaction_y_kN','ux_mm','uy_mm'],
          [[name,*xy,-c['load'][2*i+1]/1000,*reactions[2*i:2*i+2]/1000,*u[2*i:2*i+2]*1000] for i,(name,xy) in enumerate(zip(c['names'],c['xy']))])
    return c

if __name__=='__main__': run()
