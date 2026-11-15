# Logical modelling in OWL

:::{admonition} Learning objectives
:class: note

By the end of this chapter, you will be able to:

- Define classes using logical expressions and property restrictions.
- Explain the consequences of property axioms for relationships and identity.
- Use a reasoner to check consistency and class satisfiability.
- Explain inferred class memberships and unresolved classifications using the example records.
:::

The reasoner already classified B001 as a Vehicle. We now add logical conditions for recognising bicycles with frames whose material value is `"steel"@en`.

{doc}`advanced-owl-modelling` covers optional constructs and language choices. The {doc}`OWL 2 cheat sheet <owl-2-cheat-sheet>` provides the syntax reference.

```{tableofcontents}
```

:::{dropdown} Complete bicycle example (reference)

The complete ontology defines the classes, properties and logical statements used in this course. Separate fictional data illustrates components, configuration snapshots, inventory records and mass observations. The smaller walkthrough files remain the starting points for the lessons.

## Files and opening instructions

- {download}`bicycle-ontology.ttl <../data/bicycle-ontology.ttl>`: the complete ontology definitions, version `1.0.0`.
- {download}`bicycle-example-data.ttl <../data/bicycle-example-data.ttl>`: the fictional records and observations. It imports the ontology.
- {download}`catalog-v001.xml <../data/catalog-v001.xml>`: maps the imports to local files. Keep it beside the Turtle files so Protégé can load them without a Web request.

Open `bicycle-example-data.ttl` in Protégé to explore the records with the ontology. Opening `bicycle-ontology.ttl` shows the reusable definitions.

Choose **View > Render by prefixed name**, then select **Reasoner > HermiT** and **Reasoner > Start reasoner**. For the checks below, use **DL Query**, select **Instances** and choose **Execute**. Synchronise the reasoner after edits.

## What the model describes

B001–B003 retain their recorded colours, frames and materials. F003's material remains unknown. `SteelFrame` still matches the exact recorded value `"steel"@en`; other material values remain possible. B004 is an additional cargo fatbike showing how those two classes can overlap.

A `Configuration` describes one bicycle at one time. Counts and installed/spare roles apply to that snapshot. C001 records B001's frame, two wheels and cargo box; C002 records B002's frame and two wheels. Their lists are explicitly closed. The tube inside F001 is an indirect part of B001 and is not an additional installed component in C001.

An `InventoryRecord` keeps an inventory and its local code together. The compound key identifies records within their inventory. Different inventory records can describe the same bicycle.

A `MassObservation` records one measurement, in kilograms, for one physical object at one time. Repeated measurements use separate records. The number of distinct numeric values is not a count of measurement events.

The physical tags in this fictional study are permanently assigned to bicycles. That agreement supports inverse functionality. Storage allocations belong to configuration snapshots.

## Construct map

| Constructs | Where to find them |
|---|---|
| Classes, subclassing, individuals and property assertions | Bicycle/Vehicle, Frame/Component and the original inventory records |
| Equivalent classes and intersections | SteelFrame, BicycleWithSteelFrame and CargoFatbike |
| Union and complement | ResearchRecord; NonCargoBicycle |
| Disjoint classes and disjoint union | PhysicalObject/ResearchRecord/Inventory/Organisation; StudyComponent's Frame, Wheel and CargoBox categories |
| Enumeration and closure | C001/C002's installed-component lists; the {ref}`inline cohort example <owl-enumerations>` |
| Object `some`, `only` and `value` | BicycleWithSteelFrame; AssembledConfiguration; the {ref}`restriction table <owl-object-restrictions>` |
| Qualified/unqualified object cardinalities | AssembledConfiguration; FourComponentConfiguration |
| Inverse expressions and `Self` | BicycleComponent; StoredConfiguration |
| Subproperties, inverse and equivalent object properties | hasFrame/hasComponent/hasPart; isComponentOf; hasInstalledPart |
| Disjoint object properties | Installed, spare and excluded components of one Configuration |
| Functional and inverse-functional properties | describesBicycle and hasAssignedStorageBay; hasInventoryTag |
| Symmetric, transitive and reflexive properties | sharesStorageWith; hasPart/isPartOf; isPartOfOrSelf |
| Asymmetric and irreflexive properties | hasDirectComponent |
| Property chains | recordedIn followed by maintainedBy entails hasInventoryMaintainer |
| Keys | InventoryRecord's recordedIn plus inventoryCode |
| Data `some`, `only`, `value`, minimum, maximum and exact counts | StudyMassObservation; SteelFrame; InventoryRecord; MassObservation and recordedAt |
| Data-property hierarchy, equivalence, disjointness and functionality | studyInventoryCode/inventoryCode; recordedMassKg/massKg; inventoryCode/retiredInventoryCode; massKg |
| Named data ranges, intersection and facets | StudyMassKg and StudyMassObservation |
| Identity, difference and negative assertions | B001/C17; tag-based alias; duplicate inventory record; AllDifferent; explicit excluded pairs |
| Anonymous individuals | C003's unnamed spare frame |
| Punning | Frame as both a class and a TermRecord individual, with independent interpretations |
| Annotation assertions, hierarchy, domain/range, axiom and nested annotations | Labels and definitions; reviewNote; the Frame–Component subclass statement |
| Ontology metadata, versioning and imports | Ontology headers; {ref}`versioning <owl-versioning>`; the example data's import and local catalog |

The model illustrates these constructs; the cheat sheet provides further patterns. OWL profiles, semantics and serialisation formats are choices about the language and its use. The datatype inventory lists further supported types; the model uses those needed by its records.

## Results to inspect

| Query or statement | Expected result |
|---|---|
| `def:SteelFrame` | F001 |
| `def:BicycleWithSteelFrame` | B001 and its aliases C17 and TagAlias001 |
| `def:Bicycle and not def:BicycleWithSteelFrame` | No instances: B002/B003's exclusion is not established |
| `def:FourComponentConfiguration` | C001 |
| `def:CargoFatbike` | B004 |
| `def:hasInstalledComponent exactly 3` | C002 |
| `def:StoredConfiguration` | C001 |
| `def:StudyMassObservation` | M001, M002 and M003 |

The reasoner also identifies TagAlias001 with B001 and R001Duplicate with R001. It infers F001 isComponentOf B001, B001 hasPart Tube001, and C002 sharesStorageWith C001. B001 hasComponent Tube001 does not follow: hasComponent is not transitive.

## Documentation and publication

Every internally defined class, property and datatype has a definition. Labels use English and Dutch consistently; definitions and notes use English. Machine codes, version strings and typed measurements are not natural-language text.

The model follows the course conventions and the [Ask Wol publishing guide](https://lod-4tu.tudelft.nl/askwol/guide). It uses the `https://w3id.org/bicycle-ontology/` namespace; w3id registration is pending. The supplied catalog resolves imports of the ontology and example data locally.

The counted component properties are kept separate from transitive parthood. Reflexive parthood-or-self has `owl:Thing` as domain and range so it does not classify every individual as a physical object. These choices follow the [OWL 2 DL global restrictions](https://www.w3.org/TR/owl2-syntax/#Global_Restrictions_on_Axioms_in_OWL_2_DL). The key on records follows [OWL's named-individual key semantics](https://www.w3.org/TR/owl2-direct-semantics/#Keys).
:::
