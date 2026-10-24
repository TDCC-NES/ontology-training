(running-example)=
# Running example: bicycles

We will use a bicycle inventory throughout the training.

## The bicycle

B001 is our fictional blue cargo bicycle, or *bakfiets*. It has two wheels, a cargo box and a steel frame, identified as F001. Cargo bicycles are designed to carry loads in addition to the rider, such as shopping, passengers or pets.

![B001, a blue two-wheeled cargo bicycle with a cargo box in front of the rider.](../figures/b001-cargo-bicycle.svg)

## Our question

Which bicycles have steel frames?

To answer this, we need to connect each bicycle to its frame and record the frame's material. The cargo box may be made of a different material.

## A first model

The diagram shows B001 and its frame. Read each arrow in its direction to make a sentence. Colour and material are recorded inside the individual boxes.

```mermaid
---
name: bicycle-running-example
align: center
caption: A first model of B001 and its frame. Only the bicycle, frame, colour, and material are shown.
alt: Bicycle is a kind of Vehicle. B001 is an instance of Bicycle and has component F001, which is an instance of Frame. B001 has colour "blue". F001 has material "steel".
---

%%{init: {"theme": "base", "block": {"padding": 20}, "themeVariables": {"darkMode": false, "background": "#ffffff", "lineColor": "#44546a", "textColor": "#182c3e", "primaryTextColor": "#182c3e", "edgeLabelBackground": "#ffffff"}, "themeCSS": "& { background-color: #ffffff !important; } .edgeLabel, .edgeLabel p { color: #182c3e !important; }"}}%%
block-beta
    columns 3
    Vehicle["Vehicle"] space:2
    space:3
    Bicycle["Bicycle"] space Frame["Frame"]
    space:3
    B001("B001<br/>colour: “blue”") space F001("F001<br/>material: “steel”")

    Bicycle -- "is a kind of" --> Vehicle
    B001 -- "is an instance of" --> Bicycle
    F001 -- "is an instance of" --> Frame
    B001 -- "has component" --> F001

    classDef kind fill:#edf3fb,stroke:#406b92,color:#182c3e,stroke-width:2px
    classDef individual fill:#e8f4ee,stroke:#36705a,color:#183c2d,stroke-width:2px

    class Vehicle,Bicycle,Frame kind
    class B001,F001 individual
```

*Bicycle*, *Vehicle* and *Frame* are classes: they describe kinds of things. Bicycle is a subclass of Vehicle, so every bicycle is a vehicle.

B001 and F001 are individuals: a particular bicycle and its particular frame. B001 is an instance of Bicycle; F001 is an instance of Frame. Because every bicycle is a vehicle, B001 is also a vehicle.

Properties connect these individuals to other individuals or to values. “Has component” links B001 to F001. “Colour” connects B001 to “blue”; “material” connects F001 to “steel”.

A frame is part of a bicycle; a bicycle is a kind of vehicle. The model uses different relationships for these meanings.

We can now answer our question: B001 has component F001, which is a frame made of steel. B001 is therefore a bicycle with a steel frame.

Next: [Linked data foundations](linked-data-foundations.md).
