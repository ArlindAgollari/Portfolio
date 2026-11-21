---
layout: project
title: Design of a 12 m pedestrian truss
description: Two aluminum Warren trusses carry a shared 30 kN pedestrian load across a 12 m span. Their combined member mass is 73.40 kg.
technologies: [Statics, Mechanics of materials]
image: /assets/bridge-truss/elevation.png
imagealt: Side elevation of the six-panel Warren truss, with the members in tension and compression shown in different colors.
permalink: /projects/bridge-truss/
featured: true
---

[Read the design summary (PDF)]({{ '/assets/bridge-truss/design-summary.pdf' | relative_url }}) · [Jump to drawings and hand calculations](#drawings-and-hand-calculations)

## Choosing the geometry

I compared two six-panel designs for a 12 m pedestrian bridge. Both are 2 m tall and use two side trusses spaced 2 m apart. The Warren uses a repeating pattern of triangles. The Pratt adds vertical members and has diagonals that slope toward the center. Both designs use the same chord sections and include the weight of their own members.

| Design | Combined longitudinal member mass | Midspan deflection |
|---|---:|---:|
| Warren | 73.40 kg | 12.64 mm |
| Pratt | 82.84 kg | 12.01 mm |

I chose the Warren design because it saves 9.44 kg. Its additional 0.63 mm of midspan deflection keeps it within the 25 mm limit.

## Sections and loading

I used standard 6061-T6 aluminum round tubes and converted the stock dimensions to millimeters. Each side has 13 pin joints and 23 straight members. A pin at B0 and a roller at B6 support the triangulated layout.

| Members in one side truss | Quantity | Length (m) | Outside diameter × wall (mm) |
|---|---:|---:|---:|
| Bottom chord | 6 | 2.000 | 25.400 × 3.175 |
| Top chord | 5 | 2.000 | 63.500 × 1.651 |
| Diagonals | 12 | 2.236 | 57.150 × 1.651 |

Each side carries 15 kN of pedestrian load. Each interior bottom joint receives 2.50 kN and each end joint receives 1.25 kN. I assigned half of each member’s weight to each of its end joints. The combined loading produces an upward reaction of 7.680 kN at each of the four supports.

## Strength and deflection

The central bottom-chord members B2–B3 and B3–B4 carry 10.896 kN in tension. Dividing that force by the tube area of 221.685 mm² gives the largest axial stress, 49.15 MPa. The minimum yield strength of 240 MPa gives a **factor of safety against axial yielding of 4.88**, above the required 2.0.

A downward unit load at B3 gives a **midspan deflection of 12.643 mm** under the actual pedestrian load and self-weight. This is the largest vertical joint displacement. The mass estimate covers both side trusses’ chords and diagonals. Deck, floor beams, connections and transverse bracing would add weight to a complete bridge.

## Drawings and hand calculations

| Sheet | PDF | Work shown |
|---|---|---|
| 1 | [Dimensioned drawing]({{ '/assets/bridge-truss/01-dimensioned-drawing.pdf' | relative_url }}) | Joint layout, span, height and bridge width |
| 2 | [Free-body diagram and support reactions]({{ '/assets/bridge-truss/02-loads-and-reactions.pdf' | relative_url }}) | Pedestrian load, member self-weight and whole-truss equilibrium |
| 3 | [Member forces by the method of joints]({{ '/assets/bridge-truss/03-member-forces.pdf' | relative_url }}) | Signed axial forces and joint equilibrium |
| 4 | [Tube properties and axial stress]({{ '/assets/bridge-truss/04-tube-stresses.pdf' | relative_url }}) | Cross-sectional areas, tension, compression and yielding |
| 5 | [Vertical deflection at midspan]({{ '/assets/bridge-truss/05-midspan-deflection.pdf' | relative_url }}) | Virtual member forces and the unit-load sum |
| 6 | [Mass and final design comparison]({{ '/assets/bridge-truss/06-mass-and-comparison.pdf' | relative_url }}) | Member masses, weight check and design choice |
