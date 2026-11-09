(owl-cheat-sheet)=
# OWL 2 cheat sheet

A reference for {doc}`logical-modelling-in-owl`, including optional constructs explained in {doc}`advanced-owl-modelling`. Examples use the bicycle model; they illustrate separate modelling choices. Manchester syntax is used for class expressions. Turtle patterns and less common features are collected below.

Short Manchester examples omit `def:`, writing `Bicycle` for `def:Bicycle`. Individual names keep `id:`.

## Class axioms and expressions

See {ref}`necessary and sufficient conditions <owl-conditions>` and {ref}`class expressions <owl-class-expressions>`.

| Concept | What it does | Bicycle example |
|---|---|---|
| SubClassOf (⊑) | States a necessary condition; the converse needs a separate axiom | `Class: Bicycle SubClassOf: Vehicle` |
| EquivalentTo (≡) | States necessary and sufficient conditions | `Class: SteelFrame EquivalentTo: Frame and (hasMaterial value "steel"@en)` |
| Disjoint classes | Excludes shared members | Frame and Wheel are disjoint |
| Covering axiom | Makes a class exactly the union of its alternatives; overlap is allowed | `Class: StudyComponent EquivalentTo: Frame or Wheel` |
| Disjoint union | Adds pairwise disjointness to a covering axiom | StudyComponent is the disjoint union of Frame and Wheel |
| Intersection (`and`, ⊓) | Requires both conditions | `Frame and (hasMaterial value "steel"@en)` |
| Union (`or`, ⊔) | Requires at least one alternative | `Frame or Wheel` |
| Complement (`not`, ¬) | Excludes membership in a class | `Bicycle and not CargoBicycle` |
| Enumeration (`{…}`) | Fixes a class's members to the listed individuals | `{id:B001, id:B002, id:B003}` |
| `owl:Thing` (⊤) | Contains every individual | Every Bicycle belongs to Thing |
| `owl:Nothing` (⊥) | Has no members | `Frame and Wheel` is unsatisfiable when those classes are disjoint |

StudyComponent is a restricted category of frames and wheels; the broader Component class also includes cargo boxes.

A union need not determine which alternative holds. A complement needs positive evidence of exclusion. Enumeration alone does not establish that all listed names denote different individuals.

## Property restrictions

See {ref}`object-property restrictions <owl-object-restrictions>`. A *filler* is an individual at the end of a property relationship.

| Restriction | What it does | Bicycle example |
|---|---|---|
| `some` (∃) | Requires at least one filler in the specified class | `hasComponent some Frame` |
| `only` (∀) | Constrains every filler; allows zero fillers | `hasComponent only Frame` |
| `value` | Requires a link to a particular individual | `hasComponent value id:F001` |
| `Self` | Requires a link to the subject itself | `sharesStorageWith Self` |
| `min n` | Counts at least n distinct fillers | `hasComponent min 2 Wheel` |
| `max n` | Counts at most n distinct fillers | `hasComponent max 2 Wheel` |
| `exactly n` | Combines the minimum and maximum | `hasComponent exactly 2 Wheel` |
| Inverse property | Follows a relationship backwards | `inverse hasComponent some Bicycle` |

The wheel counts are *qualified*: they count only Wheel fillers. `hasComponent exactly 2` is unqualified and counts every component. A maximum can infer that two names denote one individual. State known differences with `owl:differentFrom`.

A closure such as `hasWheel only {id:W001, id:W002}` limits fillers to those two individuals. Add their property assertions to require those links. The `only Frame` example above would be unsuitable for B001's components, which also include wheels and a cargo box.

Data properties use the same keywords except `Self`; their fillers are data values. For `massKg`, values represent kilograms in the study's observation context:

| Keyword | Data-property example |
|---|---|
| `some` | `massKg some xsd:decimal` |
| `only` | `massKg only xsd:decimal` |
| `value` | `hasMaterial value "steel"@en` |
| `min` | `massKg min 1 xsd:decimal` |
| `max` | `massKg max 1 xsd:decimal` |
| `exactly` | `massKg exactly 1 xsd:decimal` |

Unqualified data cardinalities count all values. `"01"^^xsd:integer` and `"1"^^xsd:integer` count as one value. Data properties have no inverse expression.

## Property axioms

See {ref}`property axioms <owl-property-axioms>`.

| Concept | What it does | Bicycle example |
|---|---|---|
| Subproperty | A specific relationship entails a broader one | hasFrame is a subproperty of hasComponent |
| Equivalent properties | Gives two properties the same pairs | Two inventory terms can be declared equivalent when their meanings match |
| Disjoint properties | Excludes the same pair from both properties | A component cannot be both installed and spare for one bicycle in the study's fixed configuration |
| Inverse properties | Reverses the direction of each pair | hasComponent / isComponentOf |
| Domain / range | Infers subject and object classes; specifies data ranges | hasFrame has range Frame |
| Functional | Each subject has at most one filler | hasFrame, if the study permits at most one frame per bicycle |
| Inverse-functional | Each filler has at most one subject | A physical inventory tag assigned to one bicycle |
| Reflexive | Every individual relates to itself | isPartOfOrSelf |
| Irreflexive | No individual relates to itself | isDirectComponentOf |
| Symmetric | Each link entails its reverse | sharesStorageWith |
| Asymmetric | Each link excludes its reverse | isDirectComponentOf |
| Transitive | Two consecutive links entail the same relationship | A part of a part is a part |
| Property chain | A specified path entails a relationship | recordedIn followed by maintainedBy entails hasInventoryMaintainer |
| Key | Shared values identify named members of a class | Bicycle identified by recordedIn together with inventoryCode |

Data properties also support subproperties, equivalence, disjointness, domain, range and functionality. Their pairs contain an individual and a data value. Other characteristics and chains apply to object properties.

Functionality allows zero fillers. For a functional object property, all fillers for the same subject must be the same individual; distinct data values on a functional data property cause inconsistency. Several domains or ranges all apply, giving an intersection.

For a key, two named class members need a common value for every listed property; shared object-property fillers must also be named. Keys allow additional values and require neither existence nor functionality. [Key semantics](https://www.w3.org/TR/owl2-direct-semantics/#Keys)

## Assertions and reasoning

See {ref}`assertions <owl-assertions>` and {ref}`reasoning <owl-reasoning>`.

| Concept | What it does | Bicycle example |
|---|---|---|
| Class assertion | Assigns an individual to a class expression | `id:B001 a def:Bicycle` |
| Object-property assertion | Relates individuals | `id:B001 def:hasComponent id:F001` |
| Data-property assertion | Records a value | `id:F001 def:hasMaterial "steel"@en` |
| Negative property assertion | Excludes a particular object or data-value pair | F002 does not have material `"steel"@en` |
| Same / different individuals | States identity / difference | B001 and C17 identify one bicycle; W001 and W002 identify different wheels |
| Anonymous individual | Represents an individual without an IRI | `id:B004 def:hasComponent [ a def:Frame ]` |
| Classification | Derives the class hierarchy | BicycleWithSteelFrame is a subclass of Bicycle |
| Realisation | Finds an individual's most specific named classes | B001 is a BicycleWithSteelFrame |
| Entailment | A statement follows in every model | F001's type and material entail SteelFrame membership |
| Consistency | All axioms can hold together | Distinct fillers contradict an applicable maximum of one |
| Class satisfiability | A class can have a member | Frame and Wheel cannot overlap when disjoint |

A class may be unsatisfiable while the ontology is consistent: it can stay empty. Asserting a member makes the ontology inconsistent. Missing facts establish neither negative assertions nor universal restrictions. Existential requirements can hold without named fillers.

## Turtle syntax reference

These are fragments using the existing course prefixes. Prepend this block when copying them into a separate file:

```turtle
@prefix def: <https://example.org/bike/def/> .
@prefix id: <https://example.org/bike/id/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
```

:::{dropdown} Class expressions and restrictions
| Expression | Turtle pattern |
|---|---|
| Intersection | `[ a owl:Class; owl:intersectionOf (def:Frame def:Wheel) ]` |
| Union | `[ a owl:Class; owl:unionOf (def:Frame def:Wheel) ]` |
| Complement | `[ a owl:Class; owl:complementOf def:Frame ]` |
| Enumeration | `[ a owl:Class; owl:oneOf (id:B001 id:B002) ]` |
| Object restriction | `[ a owl:Restriction; owl:onProperty def:hasComponent; owl:someValuesFrom def:Frame ]` |
| Universal / individual value | Replace `owl:someValuesFrom def:Frame` with `owl:allValuesFrom def:Frame` or `owl:hasValue id:F001` |
| Self | `[ a owl:Restriction; owl:onProperty def:sharesStorageWith; owl:hasSelf true ]` |
| Qualified object cardinality | `[ a owl:Restriction; owl:onProperty def:hasComponent; owl:minQualifiedCardinality "2"^^xsd:nonNegativeInteger; owl:onClass def:Wheel ]` |
| Data restriction | `[ a owl:Restriction; owl:onProperty def:massKg; owl:someValuesFrom xsd:decimal ]` |
| Universal data restriction | Replace `owl:someValuesFrom xsd:decimal` with `owl:allValuesFrom xsd:decimal` |
| Literal value | `[ a owl:Restriction; owl:onProperty def:hasMaterial; owl:hasValue "steel"@en ]` |
| Qualified data cardinality | `[ a owl:Restriction; owl:onProperty def:massKg; owl:minQualifiedCardinality "1"^^xsd:nonNegativeInteger; owl:onDataRange xsd:decimal ]` |
| Inverse expression | `[ owl:inverseOf def:hasComponent ]` |

For maximum or exact qualified counts, use `owl:maxQualifiedCardinality` or `owl:qualifiedCardinality`. For unqualified counts, use `owl:minCardinality`, `owl:maxCardinality` or `owl:cardinality` and omit `owl:onClass` / `owl:onDataRange`.

| Class axiom | Turtle |
|---|---|
| Subclass | `def:Bicycle rdfs:subClassOf def:Vehicle .` |
| Equivalence | `def:SteelFrame owl:equivalentClass [ a owl:Class; owl:intersectionOf (def:Frame [ a owl:Restriction; owl:onProperty def:hasMaterial; owl:hasValue "steel"@en ]) ] .` |
| Disjointness | `def:Frame owl:disjointWith def:Wheel .` |
| Disjoint union | `def:StudyComponent owl:disjointUnionOf (def:Frame def:Wheel) .` |
| Several disjoint classes | `[] a owl:AllDisjointClasses; owl:members (def:Frame def:Wheel def:CargoBox) .` |

A covering axiom uses `owl:equivalentClass` with an `owl:unionOf` expression.
:::

(owl-steelframe-turtle)=
:::{dropdown} SteelFrame in Turtle
```turtle
def:SteelFrame a owl:Class ;
    owl:equivalentClass [ a owl:Class ;
        owl:intersectionOf (
            def:Frame
            [ a owl:Restriction ;
              owl:onProperty def:hasMaterial ;
              owl:hasValue "steel"@en ]
        ) ] .
```

`[]` introduces a blank node describing the expression. `( ... )` writes an RDF list: here, the two conditions combined by `owl:intersectionOf`. The `owl:equivalentClass` statement makes the expression a definition of SteelFrame. [Complex classes](https://www.w3.org/TR/owl2-primer/#Complex_Classes)
:::

:::{dropdown} Property axioms and assertions
| Axiom | Turtle pattern |
|---|---|
| Subproperty | `def:hasFrame rdfs:subPropertyOf def:hasComponent .` |
| Equivalent / disjoint properties | Use `owl:equivalentProperty` / `owl:propertyDisjointWith` between the properties |
| Several disjoint properties | `[] a owl:AllDisjointProperties; owl:members (def:hasInstalledComponent def:hasSpareComponent def:hasRemovedComponent) .` |
| Inverse | `def:hasComponent owl:inverseOf def:isComponentOf .` |
| Domain / range | `def:hasFrame rdfs:domain def:Bicycle; rdfs:range def:Frame .` |
| Characteristic | `def:hasFrame a owl:ObjectProperty, owl:FunctionalProperty .` |
| Chain | `def:hasInventoryMaintainer owl:propertyChainAxiom (def:recordedIn def:maintainedBy) .` |
| Key | `def:Bicycle owl:hasKey (def:recordedIn def:inventoryCode) .` |
| Same / different | `id:B001 owl:sameAs id:C17 .` / `id:W001 owl:differentFrom id:W002 .` |
| Several different individuals | `[] a owl:AllDifferent; owl:distinctMembers (id:B001 id:B002 id:B003) .` |

Other characteristic types are `owl:InverseFunctionalProperty`, `owl:ReflexiveProperty`, `owl:IrreflexiveProperty`, `owl:SymmetricProperty`, `owl:AsymmetricProperty` and `owl:TransitiveProperty`. Data properties use the same subproperty, equivalence, disjointness, domain, range and functional vocabulary.

Negative assertions use `owl:NegativePropertyAssertion` with `owl:sourceIndividual`, `owl:assertionProperty` and either `owl:targetIndividual` or `owl:targetValue`:

```turtle
[] a owl:NegativePropertyAssertion ;
    owl:sourceIndividual id:B001 ;
    owl:assertionProperty def:hasComponent ;
    owl:targetIndividual id:F002 .

[] a owl:NegativePropertyAssertion ;
    owl:sourceIndividual id:F002 ;
    owl:assertionProperty def:hasMaterial ;
    owl:targetValue "steel"@en .
```
:::

(owl-cheat-datatypes)=
## Data ranges and datatypes

See {ref}`data ranges <owl-data-ranges>`.

:::{dropdown} Data-range expressions and definitions
| Range | Turtle pattern |
|---|---|
| Intersection | `[ a rdfs:Datatype; owl:intersectionOf (xsd:integer xsd:nonNegativeInteger) ]` |
| Union | `[ a rdfs:Datatype; owl:unionOf (xsd:integer xsd:string) ]` |
| Complement | `[ a rdfs:Datatype; owl:datatypeComplementOf xsd:positiveInteger ]` |
| Enumeration | `[ a rdfs:Datatype; owl:oneOf ("steel"@en "aluminium"@en) ]` |
| Facet restriction | `[ a rdfs:Datatype; owl:onDatatype xsd:decimal; owl:withRestrictions ([ xsd:minExclusive "0"^^xsd:decimal ]) ]` |

A data complement includes all values outside the range, including other kinds of value. Intersect it with a numeric datatype when the intended range is numeric.

A datatype definition names a reusable range. This one contains decimal values greater than 0 and at most 100:

```turtle
def:StudyMassKg a rdfs:Datatype ;
    owl:equivalentClass [ a rdfs:Datatype ;
        owl:onDatatype xsd:decimal ;
        owl:withRestrictions (
            [ xsd:minExclusive "0"^^xsd:decimal ]
            [ xsd:maxInclusive "100"^^xsd:decimal ]
        ) ] .
```

Use built-in datatypes on literals, such as `"23.5"^^xsd:decimal`, and as the bases of facet restrictions. Custom datatypes supply value ranges, with one acyclic definition; they supply no new lexical forms or facets. Standard data ranges are unary. [Data ranges and definitions](https://www.w3.org/TR/owl2-syntax/#Data_Ranges)
:::

:::{dropdown} Complete OWL 2 datatype and facet inventory
| Group | Datatypes in the 2012 OWL 2 map |
|---|---|
| Real / rational | `owl:real`, `owl:rational` |
| Decimal / integer | `xsd:decimal`, `xsd:integer`, `xsd:nonNegativeInteger`, `xsd:nonPositiveInteger`, `xsd:positiveInteger`, `xsd:negativeInteger` |
| Bounded integer | `xsd:long`, `xsd:int`, `xsd:short`, `xsd:byte`, `xsd:unsignedLong`, `xsd:unsignedInt`, `xsd:unsignedShort`, `xsd:unsignedByte` |
| Floating-point | `xsd:float`, `xsd:double` |
| Text | `rdf:PlainLiteral`, `xsd:string`, `xsd:normalizedString`, `xsd:token`, `xsd:language`, `xsd:Name`, `xsd:NCName`, `xsd:NMTOKEN` |
| Boolean | `xsd:boolean` |
| Binary | `xsd:hexBinary`, `xsd:base64Binary` |
| URI value | `xsd:anyURI` |
| Date-time | `xsd:dateTime`, `xsd:dateTimeStamp` |
| XML | `rdf:XMLLiteral` |

`rdfs:Literal` contains all data values. `owl:real` has no direct literal forms. Integers are included in decimals; floating-point, URI and binary values have their own identity rules.

| Facets | Apply to |
|---|---|
| `xsd:minInclusive`, `xsd:maxInclusive`, `xsd:minExclusive`, `xsd:maxExclusive` | Numeric and date-time datatypes |
| `xsd:length`, `xsd:minLength`, `xsd:maxLength` | Text, binary data and URI values |
| `xsd:pattern` | Text and URI values |
| `rdf:langRange` | `rdf:PlainLiteral` |

Several facet conditions all apply. OWL 2 does not include every XSD datatype or facet; for example, `xsd:date`, `xsd:duration`, `xsd:totalDigits` and `xsd:fractionDigits` are outside this inventory. Consult the [datatype map](https://www.w3.org/TR/owl2-syntax/#Datatype_Maps) for lexical forms, value identity and facet rules.

The earlier chapters use RDF 1.1's `rdf:langString`. OWL 2's 2012 map uses `rdf:PlainLiteral`; the same `"steel"@en` notation remains usable. The reasoning download leaves the material range open to avoid requiring the newer datatype as an extension. [Language-tagged literals](https://www.w3.org/TR/rdf-plain-literal/)
:::

(owl-cheat-declarations)=
## Ontology structure and language choices

See {ref}`entity annotations <owl-entity-annotations>`, {ref}`documentation <owl-ontology-structure>`, {ref}`versioning <owl-versioning>`, {ref}`imports <owl-imports>` and {ref}`language choices <owl-language-choices>`.

:::{dropdown} Declarations, annotations and ontology headers
| Entity | Turtle declaration |
|---|---|
| Class | `def:Frame a owl:Class .` |
| Datatype | `def:StudyMassKg a rdfs:Datatype .` |
| Object property | `def:hasComponent a owl:ObjectProperty .` |
| Data property | `def:hasMaterial a owl:DatatypeProperty .` |
| Annotation property | `def:reviewNote a owl:AnnotationProperty .` |
| Named individual | `id:F001 a owl:NamedIndividual .` |

Annotations can describe entities, anonymous individuals, ontologies, axioms or other annotations. Values can be IRIs, literals or anonymous individuals. Under Direct Semantics, annotations and annotation-property axioms do not affect logical entailments.

| Annotation-property axiom | Turtle |
|---|---|
| Assertion | `def:Frame rdfs:label "frame"@en .` |
| Subproperty | `def:reviewNote rdfs:subPropertyOf rdfs:comment .` |
| Domain / range | `def:reviewNote rdfs:domain owl:Class; rdfs:range xsd:string .` |

Axiom annotations use `owl:Axiom` with `owl:annotatedSource`, `owl:annotatedProperty` and `owl:annotatedTarget`, alongside the axiom's triple. Nested annotations use `owl:Annotation`. [Annotation patterns](https://www.w3.org/TR/owl2-mapping-to-rdf/#Translation_of_Axioms_with_Annotations)

Built-in annotation properties: `rdfs:label`, `rdfs:comment`, `rdfs:seeAlso`, `rdfs:isDefinedBy`, `owl:deprecated`, `owl:versionInfo`, `owl:priorVersion`, `owl:backwardCompatibleWith`, `owl:incompatibleWith`.

```turtle
<https://example.org/bike/reasoning> a owl:Ontology ;
    owl:versionIRI <https://example.org/bike/reasoning/1.0> ;
    owl:imports <https://example.org/inventory/1.0> ;
    owl:versionInfo "1.0" .
```

The ontology IRI, version IRI and document location can differ. An ontology can omit its IRI. Imports include the imported ontologies' axioms and their imports; version annotations describe the publisher's compatibility claims.
:::

:::{dropdown} OWL 2 DL restrictions and profiles
| Built-in terms | Meaning |
|---|---|
| `owl:topObjectProperty` / `owl:bottomObjectProperty` | Every pair of individuals / no pairs |
| `owl:topDataProperty` / `owl:bottomDataProperty` | Every individual–value pair / no pairs |

OWL 2 DL supports decidable reasoning under Direct Semantics. OWL 2 Full uses RDF-Based Semantics with unrestricted RDF combinations; general complete reasoning is undecidable.

Object cardinalities, Self, functional/inverse-functional/irreflexive/asymmetric characteristics and object-property disjointness require *simple* properties. Transitive properties, chain superproperties, their inverses and superproperties are non-simple, as are the top and bottom object properties. Chains need a regular hierarchy; controlled recursion, including transitivity, is permitted.

Punning permits separate uses of one IRI, such as class and individual. It excludes class–datatype overlap and overlap between property types. Anonymous individuals have restricted tree-like assertion patterns and cannot occur in object enumerations/value restrictions, identity/difference axioms or negative property assertions. `owl:topDataProperty` can occur only as the superproperty in data-subproperty axioms. Apply DL checks across imports. [Global restrictions](https://www.w3.org/TR/owl2-syntax/#Global_Restrictions_on_Axioms_in_OWL_2_DL)

| Profile | Intended setting |
|---|---|
| EL | Large class/property models |
| QL | Query rewriting over large datasets |
| RL | Rule-based reasoning |

Each profile restricts allowed constructs and their positions. Check the ontology and the chosen reasoner's support. [Profiles](https://www.w3.org/TR/owl2-profiles/)
:::

For the specification's construct names and complete mappings, consult the [OWL 2 Quick Reference](https://www.w3.org/TR/owl2-quick-reference/).
