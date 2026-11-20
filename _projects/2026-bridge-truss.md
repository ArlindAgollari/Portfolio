---
layout: project
title: A lightweight pedestrian truss for a 12 m crossing
description: A six-panel aluminum Warren truss carries a shared pedestrian load with a calculated midspan deflection of 12.64 mm.
technologies: [Statics, Structural mechanics, Python]
image: /assets/bridge-truss/elevation.png
imagealt: Six triangular panels spanning twelve metres, with member forces shown by color.
permalink: /projects/bridge-truss/
---

## Design objective

The design brief calls for a 12 m crossing, 2 m wide, carrying a 30 kN uniformly distributed pedestrian load. Two identical side trusses share the load. The brief permits a truss height of 2–3 m and requires a factor of safety of at least 2 and a vertical deflection no greater than 25 mm. The objective used here is the combined mass of the members in both longitudinal planes.

## Choosing the geometry

A Warren layout uses alternating inclined web members. A Pratt layout with sloping end posts adds vertical members and directs most interior diagonal forces into tension under gravity loading. Shorter compression members can resist more load before buckling, but each additional panel adds web material. [Truss types, North Carolina Department of Transportation](https://www.ncdot.gov/initiatives-policies/Transportation/bridges/historic-bridges/bridge-types/Pages/truss.aspx)

The comparison covered both layouts, 4, 6 and 8 panels, and heights of 2.0, 2.5 and 3.0 m. For each geometry, seven round-tube sizes were available independently to the bottom chord, upper chord and web. Each of the 6,174 combinations was evaluated with its own self-weight. The table shows the lightest passing section assignment for selected geometries.

| Layout | Panels | Height (m) | Both trusses (kg) | Max vertical deflection (mm) | Minimum factor of safety |
|---|---:|---:|---:|---:|---:|
| Warren | 4 | 2.5 | 79.83 | 7.88 | 2.14 |
| Warren | 6 | 2.0 | 73.40 | 12.64 | 2.11 |
| Warren | 6 | 2.5 | 85.88 | 9.60 | 2.04 |
| Warren | 8 | 2.0 | 83.81 | 13.74 | 2.29 |
| Pratt | 6 | 2.0 | 82.84 | 12.01 | 2.26 |

The six-panel, 2 m Warren saves 9.44 kg relative to the lightest Pratt tested. Increasing its height reduced deflection but lengthened its diagonals and increased the web size needed for buckling. The selected design is the lightest in this grouped-stock search. Individual member sizing or a larger catalog could reduce mass further.

## Geometry and sections

The lower joints B0 through B6 lie at x = 0, 2, 4, 6, 8, 10 and 12 m. The upper joints T1 through T6 lie at x = 1, 3, 5, 7, 9 and 11 m, each 2 m above the lower chord. Each upper joint connects to both lower joints directly beneath its panel. The left support at B0 is a pin and B6 rests on a horizontal roller surface. The two planes are spaced 2 m apart. One side has 13 joints, 23 members and three reaction components. Its connected triangles and support restraints make it stable in plane, and 23 + 3 = 2(13) makes it statically determinate.

| Member family | Quantity per side | Length (m) | Tube OD × wall (in) | Area (mm²) |
|---|---:|---:|---:|---:|
| Bottom chord | 6 | 2.000 | 1.000 × 0.125 | 221.68 |
| Top chord | 5 | 2.000 | 2.500 × 0.065 | 320.80 |
| Diagonals | 12 | 2.236 | 2.250 × 0.065 | 287.86 |

The model uses straight, unwelded 6061-T6 aluminum tubes with E = 69 GPa, density = 2,700 kg/m³ and a design yield strength of 240 MPa. Tubes give equal bending stiffness about both centroidal axes. The larger diameters place material farther from those axes in the members that carry compression. The bottom chord stays in tension in the specified case. [Hydro alloy data](https://www.hydro.com/globalassets/01-products--services/extruded-profiles/americas/ena-resources/alloy-data-sheets/hydro_2019_data_sheet_6061.pdf) · [ADI round tube properties](https://aluminum.adimetal.com/Asset/adi-6061-t6-round-tube.pdf) · [Coast Aluminum stock catalog](https://coastaluminum.com/wp-content/uploads/2025/08/Coast-Aluminum-Catalog.pdf)

## Loads, reactions and member forces

Each side receives 15 kN, or 1.25 kN/m. Deck load enters the lower joints through transverse floor beams. Each interior lower joint receives 2.50 kN of pedestrian load and each end receives 1.25 kN. Half the weight of each bar is added at each of its two ends, including upper joints. The resulting downward loads per side are 1.26440 kN at each lower end, 2.52879 kN at each interior lower joint, 0.02555 kN at each upper end and 0.03404 kN at each interior upper joint.

Summing moments about B0 and then vertical forces gives 7.68001 kN upward at each support of one truss. Horizontal equilibrium gives zero horizontal reaction. At B0, the diagonal rises 2 m over a horizontal run of 1 m. With tension positive, vertical equilibrium gives N(B0–T1) = −(7.68001 − 1.26440)√5/2 = −7.17287 kN. Horizontal equilibrium gives N(B0–B1) = −N(B0–T1)/√5 = +3.20781 kN.

| Member | Axial force (kN) | Member | Axial force (kN) |
|---|---:|---|---:|
| B0–B1 | +3.208 | B0–T1 | −7.173 |
| B1–B2 | +8.333 | B1–T1 | +7.144 |
| B2–B3 | +10.896 | B1–T2 | −4.317 |
| T1–T2 | −6.403 | B2–T2 | +4.279 |
| T2–T3 | −10.247 | B2–T3 | −1.452 |
| T3–T4 | −11.529 | B3–T3 | +1.414 |

Reflected members have equal forces. The downloadable member table lists all 23 members, with signed stresses and safety factors.

## Strength and stability

For outside diameter D and inside diameter d, the section properties are A = π(D² − d²)/4 and I = π(D⁴ − d⁴)/64. The axial yield factor is 240 MPa divided by the absolute axial stress, |N|/A. Compression members also receive a pin-ended Euler buckling check, Pcr = π²EI/L². The model assumes each compression joint has adequate transverse restraint so that its effective length is one member length in both directions. [Column buckling reference](https://engineeringlibrary.org/reference/column-data-air-force-stress-manual)

The center upper chord carries the greatest compression, 11.529 kN, and has an elastic buckling load of 26.134 kN, giving a factor of 2.27. Each end diagonal has a smaller diameter and longer unsupported length. Its buckling load is 15.109 kN against 7.173 kN demand, giving the governing **factor of 2.106**. The peak gross axial stress is 49.15 MPa in the central bottom chord, giving a yield factor of 4.88.

## Deflection and mass

A downward unit load at midspan B3 gives a second set of member forces n per unit applied load. The midspan displacement equals the sum of NnL/(EA) over all members, using signed real-load forces N and consistent SI units. For example, B2–B3 contributes (10,896.3)(1.25)(2)/(69 × 10⁹ × 0.000221685) = 1.781 mm. Summing all 23 terms gives **12.643 mm downward**. A separate direct-stiffness solution checks every joint displacement and confirms B3 has the largest vertical movement. [Unit-load method and derivation](https://eng.libretexts.org/Bookshelves/Civil_Engineering/Structural_Analysis_(Udoeyo)/01%3A_Chapters/1.08%3A_Deflections_of_Structures-_Work-Energy_Methods)

Summing density × area × member length gives 36.699 kg per side, or **73.398 kg for both side trusses**. Their total weight is 0.720 kN. Adding that weight to the 30 kN pedestrian load gives 30.720 kN, equal to the sum of the four vertical support reactions.

## Design limits and next checks

These results apply to the assigned planar load case. A physical crossing needs a transverse system that transfers floor loads to the lower joints and restrains the upper compression chord. Doubling an unbraced length would reduce its calculated Euler capacity to one quarter. Deck, floor beams, lateral bracing, pins and gussets are outside the reported mass. A construction design would need their loads, connection and local wall checks, out-of-plane stability, vibration and the applicable bridge design load combinations.

## Calculation files

- [Member forces, stresses, safety factors and virtual-work terms]({{ '/assets/bridge-truss/members.csv' | relative_url }})
- [Joint coordinates, loads, reactions and displacements]({{ '/assets/bridge-truss/joints.csv' | relative_url }})
- [Minimum-mass passing design for each geometry]({{ '/assets/bridge-truss/iterations.csv' | relative_url }})
- [Reproducible Python analysis]({{ '/assets/bridge-truss/analyze.py' | relative_url }}) (requires NumPy)
