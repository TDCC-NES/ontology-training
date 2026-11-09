# Complete bicycle ontology

A reference model for the OWL 2 constructs taught in this course. It extends the bicycle inventory with configuration snapshots, inventory records and mass observations. All records are fictional.

## Files and opening instructions

- `bike-ontology-complete.ttl`: the complete model and example records. Open it on its own in Protégé. It uses the same ontology and term IRIs as the smaller bicycle example, with version `3.0.0`.
- `bike-study.ttl`: an optional study ontology that imports that version and defines the cohort B001–B003.
- `catalog-v001.xml`: maps the imported version IRI to the local complete model. Keep it beside both Turtle files when opening the study ontology. Protégé uses this catalog to load the import without a Web request.

Choose **View > Render by prefixed name**, then select **Reasoner > HermiT** and **Reasoner > Start reasoner**. For the checks below, use **DL Query**, select **Instances** and choose **Execute**. Synchronise the reasoner after edits.

The smaller course files remain the starting points for the walkthroughs. This complete model is a reference to explore as needed.

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
| Enumeration and closure | C001/C002's installed-component lists; the cohort in `bike-study.ttl` |
| Object `some`, `only` and `value` | BicycleWithSteelFrame; AssembledConfiguration; B001Configuration |
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
| Named data ranges, intersection, union, complement, enumeration and facets | StudyMassKg, InventoryCode and StudyInventoryCode |
| Identity, difference and negative assertions | B001/C17; tag-based alias; duplicate inventory record; AllDifferent; explicit excluded pairs |
| Anonymous individuals | C003's unnamed spare frame |
| Punning | Frame as both a class and a TermRecord individual, with independent interpretations |
| Annotation assertions, hierarchy, domain/range, axiom and nested annotations | Labels and definitions; reviewNote; the Frame–Component subclass statement |
| Ontology metadata, versioning and imports | Ontology headers; the optional study ontology and local catalog |

This covers the course's construct families. OWL profiles, semantics and serialisation formats are choices about the language and its use. The datatype inventory lists further supported types; the model uses those needed by its records.

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
| `study:CohortBicycle` in the optional study ontology | B001–B003 and names known to identify those bicycles |

The reasoner also identifies TagAlias001 with B001 and R001Duplicate with R001. It infers F001 isComponentOf B001, B001 hasPart Tube001, and C002 sharesStorageWith C001. B001 hasComponent Tube001 does not follow: hasComponent is not transitive.

## Documentation and publication

Every internally defined class, property and datatype has a definition. Labels use English and Dutch consistently; definitions and notes use English. Machine codes, version strings and typed measurements are not natural-language text.

The model follows the course conventions and the [Ask Wol publishing guide](https://lod-4tu.tudelft.nl/askwol/guide). Its `example.org` IRIs are placeholders. Before publishing a real ontology, choose maintained identifiers, configure their resolution and serve RDF and human-readable descriptions. The local catalog demonstrates import resolution; it is not a public redirect service.

The counted component properties are kept separate from transitive parthood. Reflexive parthood-or-self has `owl:Thing` as domain and range so it does not classify every individual as a physical object. These choices follow the [OWL 2 DL global restrictions](https://www.w3.org/TR/owl2-syntax/#Global_Restrictions_on_Axioms_in_OWL_2_DL). The key on records follows [OWL's named-individual key semantics](https://www.w3.org/TR/owl2-direct-semantics/#Keys).

## Validation

Checked on 9 November 2026 with the course's installed OWLAPI 4.5.29 and HermiT 1.4.3.456:

- The complete model and the imported study pass the OWL 2 DL profile check, are consistent, and all their internally defined classes are satisfiable.
- The complete model passes 60 expected inference/non-inference checks. The imported study passes 66, including the cohort's membership and B004's exclusion.
- Protégé's bundled catalog resolver loads the local import and matches its version IRI.
- Six invalid test variations produce the expected contradictions, covering component roles, functional values, inventory-code ranges and tag-based identity.
- Ask Wol's offline checks report no errors, warnings or recommendations. Namespace and HTTP import checks are skipped; Web publication is not tested.

The installed tools support the RDF 1.1 `rdf:langString` datatype used throughout the course. This extends OWL 2's original 2012 datatype map.
