# Advanced OWL modelling (optional)

:::{admonition} Learning objectives
:class: note

By the end of this page, you will be able to:

- Predict inferences and contradictions from the advanced modelling examples.
- Distinguish OWL 2 DL restrictions, profiles and writing formats.
:::

These topics build on {ref}`class restrictions <owl-object-restrictions>` and {ref}`property axioms <owl-property-axioms>`. The examples illustrate separate modelling choices; the {ref}`reasoning example <reasoning-example-files>` contains the steel-frame definitions and imports the separate bicycle/frame records. Expressions use Manchester syntax; Turtle blocks are fragments using the {ref}`course prefixes <owl-turtle-example>`.

(owl-enumerations)=
## Enumerations and disjoint unions

An enumeration fixes a class's members to the individuals denoted by the listed names. For a study-specific class, `study:` abbreviates `https://w3id.org/bicycle-ontology/study/def/`:

```text
Class: study:CohortBicycle
    SubClassOf: def:Bicycle
    EquivalentTo: {id:B001, id:B002, id:B003}
```

This cohort contains B001, B002 and B003; known aliases denote members too. Another member must be identical to one of those individuals. The names alone do not establish three distinct bicycles. [Class expressions](https://www.w3.org/TR/owl2-syntax/#Propositional_Connectives_and_Enumeration_of_Individuals)

A single-individual enumeration, such as `{id:B001}`, is a [*nominal*](https://www.cs.ox.ac.uk/people/ian.horrocks/Publications/download/2010/HoPa10a.pdf).

A *disjoint union* makes its alternatives exhaustive and mutually exclusive. In the complete example, StudyComponent is the disjoint union of Frame, Wheel and CargoBox: these are exactly its three categories. The broader Component class also accommodates other kinds of part, so that partition would not suit it. [Class axioms](https://www.w3.org/TR/owl2-syntax/#Class_Expression_Axioms)

(owl-closure)=
## Closure axioms

A *closure axiom* records a local boundary. Suppose W001 and W002 are all B001's wheel fillers, using a new object property `def:hasWheel`:

```text
Individual: id:B001
    Types: def:hasWheel only {id:W001, id:W002}
    Facts: def:hasWheel id:W001, def:hasWheel id:W002
```

Every wheel filler must be one of those individuals. The facts supply the links; the restriction excludes additional, different fillers. State `id:W001 owl:differentFrom id:W002 .` to require two distinct wheels. `def:hasComponent max 0 def:CargoBox` similarly excludes any CargoBox component; missing cargo-box links alone do not establish it.

(owl-inverse-self)=
## Inverse and self restrictions

An inverse expression follows a relationship backwards: `inverse def:hasComponent some def:Bicycle` describes components of a Bicycle. It needs no separately named inverse property.

`def:sharesStorageWith Self` describes individuals related to themselves by sharesStorageWith, if the study defines that relationship to include self-sharing. This local Self condition differs from declaring a property reflexive, which requires self-links for every individual. [Inverse expressions](https://www.w3.org/TR/owl2-syntax/#Object_Property_Expressions), [Self restrictions](https://www.w3.org/TR/owl2-syntax/#Self-Restriction)

(owl-data-ranges)=
## Describing data values

Data-property restrictions use the same `some`, `only`, `value`, `min`, `max` and `exactly` patterns, with data values and *data ranges* in place of individuals and classes.

For these examples, introduce `def:massKg` for decimal mass measurements in kilograms within the study's observation context. The `xsd:` prefix abbreviates `http://www.w3.org/2001/XMLSchema#`.

| Manchester expression | Meaning |
|---|---|
| `def:massKg some xsd:decimal` | At least one decimal mass value |
| `def:massKg exactly 1 xsd:decimal` | Exactly one distinct decimal mass value |
| `def:massKg some xsd:decimal[> 0, <= 100]` | At least one decimal mass value greater than 0 and at most 100 |

The last expression uses *facets* to narrow a datatype. A datatype-definition axiom can give a reusable range a name. Data ranges also support intersection, union, complement and enumeration. For example, an enumeration can contain exactly `"steel"@en` and `"aluminium"@en`. A complement includes all data values outside its range, so the complement of positive integers includes strings too. [Data ranges](https://www.w3.org/TR/owl2-syntax/#Data_Ranges)

Cardinalities count values, not written forms: `"01"^^xsd:integer` and `"1"^^xsd:integer` denote one integer. Unqualified data cardinalities count all values. Data properties have no inverse expressions.

The {ref}`cheat sheet <owl-cheat-datatypes>` lists OWL 2's supported datatypes and facets. OWL 2's 2012 datatype map uses `rdf:PlainLiteral`; RDF 1.1 uses `rdf:langString` for language-tagged text. Our `"steel"@en` values work in both syntax frameworks. The course files use the `rdf:langString` range supported by the tested Protégé/HermiT combination in chapter 4. [Plain literals](https://www.w3.org/TR/rdf-plain-literal/), [RDF 1.1 literals](https://www.w3.org/TR/rdf11-concepts/#section-Graph-Literal)

(owl-more-property-characteristics)=
## Further property characteristics

These characteristics apply to object properties:

| Characteristic | Consequence | Possible relationship |
|---|---|---|
| Inverse-functional | Each filler has at most one subject | hasAssignedInventoryTag for a physical tag identifying one bicycle |
| Reflexive | Every individual relates to itself | isPartOfOrSelf |
| Irreflexive | No individual relates to itself | isDirectComponentOf |
| Asymmetric | A link excludes its reverse, including self-links | isDirectComponentOf |

Reflexivity applies to every individual, so combining it with a domain can classify every individual in that domain. Irreflexivity alone excludes self-links, without excluding reversed links between different individuals. [Property characteristics](https://www.w3.org/TR/owl2-primer/#Property_Characteristics)

(owl-chains-keys)=
## Chains and keys

A property chain derives a relationship from an ordered path. Introduce recordedIn from a bicycle to an inventory, and maintainedBy from an inventory to its maintaining organisation:

```turtle
def:recordedIn a owl:ObjectProperty .
def:maintainedBy a owl:ObjectProperty .

def:hasInventoryMaintainer a owl:ObjectProperty ;
    owl:propertyChainAxiom (def:recordedIn def:maintainedBy) .
```

If B001 is recorded in InventoryA and InventoryA is maintained by TeamA, infer B001 hasInventoryMaintainer TeamA. The reverse implication does not follow. Chains use object properties, including inverse expressions; they cannot traverse material strings. [Property chains](https://www.w3.org/TR/owl2-primer/#Property_Chains)

A *key* specifies identifying properties within a class. In the complete example, an InventoryRecord identifies one bicycle within one inventory. For named records, the named inventory and local code form the key: two records sharing a value for every key property must be the same individual. Different records can describe the same bicycle. Keys allow additional values and require neither existence nor functionality. Use this key only when sharing those values identifies one record. The cheat sheet gives its syntax and precise naming conditions. [Keys](https://www.w3.org/TR/owl2-primer/#Keys)

(owl-negative-assertions)=
## Negative assertions and unnamed individuals

A *negative property assertion* excludes a particular pair. For example, inspection could establish that F002 does not have the material value `"steel"@en`:

```turtle
[] a owl:NegativePropertyAssertion ;
    owl:sourceIndividual id:F002 ;
    owl:assertionProperty def:hasMaterial ;
    owl:targetValue "steel"@en .
```

For a negative object-property assertion, use `owl:targetIndividual` instead of `owl:targetValue`. Missing data supplies neither negative assertion. Negative class information uses a complement: asserting F002 in `not def:SteelFrame` excludes its membership. [Assertions](https://www.w3.org/TR/owl2-syntax/#Assertions)

A blank node in an individual position can describe an unnamed component: `id:B004 def:hasComponent [ a def:Frame ]`. Blank-node labels are local to their document. Use an IRI when researchers need to refer to the component across datasets.

(owl-language-choices)=
## Language choices and reasoning boundaries

OWL 2 DL restricts the combinations of axioms to support decidable reasoning under Direct Semantics: an algorithm can finish with the correct answer for the supported reasoning tasks. RDF-Based Semantics interprets OWL directly on RDF graphs; OWL 2 Full allows combinations beyond DL's restrictions, with undecidable general reasoning. [OWL 2 semantics](https://www.w3.org/TR/owl2-overview/#Semantics)

For example, a transitive property cannot be used in an object cardinality restriction in OWL 2 DL. To count direct components while also modelling transitive parts, keep a separate hasDirectComponent property for counts and make it a subproperty of hasPart. The counting property must meet OWL's *simplicity* restrictions, which also account for chains and inverses. A profile checker tests the complete combination of axioms, including those of {ref}`imported ontologies <owl-imports>`; the cheat sheet summarises the restrictions. [Global restrictions](https://www.w3.org/TR/owl2-syntax/#Global_Restrictions_on_Axioms_in_OWL_2_DL)

OWL 2 DL also permits *punning*: a class and an individual may use the same IRI, with independent interpretations. Describing Frame as a catalogue entry then describes that entry, without applying its properties to every frame. [Metamodeling](https://www.w3.org/TR/owl2-syntax/#Metamodeling)

OWL 2 provides three restricted profiles for different reasoning needs:

| Profile | Intended setting |
|---|---|
| EL | Large class/property models using features such as intersections and existential descriptions |
| QL | Query rewriting over large instance datasets, including relational databases |
| RL | Rule-based reasoning over RDF data |

Each profile permits particular constructs in particular positions. Check both the ontology's profile and the application's support. Turtle, Manchester, Functional Syntax and OWL/XML are writing formats; choosing one does not choose a profile or semantics. [Profiles](https://www.w3.org/TR/owl2-profiles/)

The [OWL 2 Primer](https://www.w3.org/TR/owl2-primer/) provides further explanations, the [Structural Specification](https://www.w3.org/TR/owl2-syntax/) defines the language, and the [Document Overview](https://www.w3.org/TR/owl2-overview/) maps the companion specifications.
