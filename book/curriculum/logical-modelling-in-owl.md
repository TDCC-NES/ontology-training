# Logical modelling in OWL

:::{admonition} Learning objectives
:class: note

By the end of this chapter, you will be able to:

- Define classes using logical expressions and property restrictions.
- Explain the consequences of property axioms for relationships and identity.
- Use a reasoner to check consistency and class satisfiability.
- Explain why particular class memberships follow from the example records and others remain undetermined.
:::

The reasoner already classified B001 as a Vehicle. We now add logical conditions for recognising bicycles with frames whose material value is `"steel"@en`.

{doc}`advanced-owl-modelling` covers optional constructs and language choices. The {doc}`OWL 2 cheat sheet <owl-2-cheat-sheet>` provides the syntax reference.

The {ref}`file guide <course-example-files>` summarises the roles of the working, reference and data files.

```{tableofcontents}
```

:::{dropdown} Course files and extended bicycle reference example

The walkthroughs use the smaller working files listed below. The extended reference ontology brings together the bicycle hierarchy, component relationships and steel-frame definitions, with separate fictional data illustrating their use.

(course-example-files)=
## Files and opening instructions

| File | Role |
|---|---|
| Your `bike-working.ttl` and `bike-logical.ttl` | Working copies containing B001 and F001. Chapter 5 adds logical definitions to the copy created in chapter 4. |
| {download}`owl2-reasoning.ttl <../data/owl2-reasoning.ttl>` | Completed steel-frame definitions for the reasoning checks; imports the three inventory records. |
| {download}`bicycle-inventory.ttl <../data/bicycle-inventory.ttl>` | The three inventory records used in chapters 5–6, kept separate from the definitions. |
| Your `inventory-data.ttl` | Chapter 6's conversion output; contains the same record triples as `bicycle-inventory.ttl`. |
| {download}`bicycle-ontology.ttl <../data/bicycle-ontology.ttl>` | Reference definitions and publication metadata, version `1.0.0`; used for ontology validation in chapter 6 and publication in chapter 7. |
| {download}`bicycle-example-data.ttl <../data/bicycle-example-data.ttl>` | Extended fictional bicycle and component records; imports the reference ontology. |
| {download}`catalog-v001.xml <../data/catalog-v001.xml>` | Maps imports to local files. Keep it beside the Turtle files so Protégé can load them without a Web request. |

Open `bicycle-example-data.ttl` in Protégé to explore the records with the ontology. Opening `bicycle-ontology.ttl` shows the reusable definitions.

Choose **View > Render by prefixed name**, then select **Reasoner > HermiT** and **Reasoner > Start reasoner**. For the checks below, use **DL Query**, select **Instances** and choose **Execute**. Synchronise the reasoner after edits.

## What the model describes

B001–B003 retain their recorded colours, frames and materials. F003's material remains unknown. `SteelFrame` still matches the exact recorded value `"steel"@en`; other material values remain possible. B004 is an additional cargo fatbike showing how those two classes can overlap.

B001 also has two recorded wheels and a cargo box. Its frame F001 has a tube, Tube001, which is therefore an indirect part of B001.

C17 is another name for B001, linked through `owl:sameAs`. The `owl:AllDifferent` statement distinguishes the other named objects and leaves out this alias.

## Construct map

| Constructs | Where to find them |
|---|---|
| Classes, subclassing, individuals and property assertions | Bicycle/Vehicle, Frame/Component and the bicycle records |
| Equivalent classes, intersections and restrictions | SteelFrame's material `value`; BicycleWithSteelFrame's `some` SteelFrame component |
| Disjoint classes | Frame, Wheel and CargoBox |
| Subproperties and inverse properties | hasFrame/hasComponent/hasPart; isComponentOf and isPartOf |
| Transitive properties | hasPart/isPartOf; B001's indirect part Tube001 |
| Identity and difference | B001/C17; AllDifferent |
| Annotations | English and Dutch labels; English definitions |
| Ontology metadata, versioning and imports | Ontology headers; {ref}`versioning <owl-versioning>`; the example data's import and local catalog |

Further constructs are illustrated separately in {doc}`define-classes-logically`, {doc}`property-characteristics-and-identity`, {doc}`advanced-owl-modelling` and the {doc}`OWL 2 cheat sheet <owl-2-cheat-sheet>`.

## Results to inspect

| Query or statement | Expected result |
|---|---|
| `def:SteelFrame` | F001 |
| `def:BicycleWithSteelFrame` | B001 and its alias C17 |
| `def:Bicycle and not def:BicycleWithSteelFrame` | No instances: B002/B003's exclusion is not established |
| `def:CargoBicycle and def:Fatbike` | B004 |

The reasoner also infers F001 isComponentOf B001 and B001 hasPart Tube001. B001 hasComponent Tube001 does not follow: hasComponent is not transitive.

## Documentation and publication

Every internally defined class and property has a definition. Labels use English and Dutch; definitions use English. Dates use `xsd:date`; the version string is untagged.

The model follows the course conventions and the [Ask Wol publishing guide](https://askwol.net/guide). It uses the `https://w3id.org/bicycle-ontology/` namespace. The supplied catalog resolves imports of the ontology and example data locally.

The non-transitive hasComponent property stays separate from transitive hasPart. This lets the optional cardinality examples count distinct components while following the [OWL 2 DL global restrictions](https://www.w3.org/TR/owl2-syntax/#Global_Restrictions_on_Axioms_in_OWL_2_DL).
:::
