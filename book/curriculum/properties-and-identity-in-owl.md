(owl-assertions)=
# Property axioms and identity

In the initial OWL walkthrough, we recorded statements such as “B001 is a Bicycle” and “B001 has component F001”. These *assertions* describe particular individuals through class memberships, relationships and values.

Here, property axioms describe a property's behaviour across all its uses. Class restrictions describe conditions on class members. The following examples are separate modelling choices.

(owl-property-axioms)=
## Relationships between properties

Make hasFrame a more specific relationship than hasComponent:

```turtle
def:hasFrame a owl:ObjectProperty ;
    rdfs:subPropertyOf def:hasComponent ;
    rdfs:range def:Frame .

id:B001 def:hasFrame id:F001 .
```

This entails B001 hasComponent F001. A general component link alone does not entail the more specific hasFrame link. An inverse axiom supplies the opposite direction:

```turtle
def:hasComponent owl:inverseOf def:isComponentOf .
```

From B001 hasComponent F001, infer F001 isComponentOf B001. Equivalent properties have the same pairs; disjoint properties cannot relate the same pair. Subproperties, equivalence and disjointness also apply to data properties, where the pair contains an individual and a value. [Property axioms](https://www.w3.org/TR/owl2-syntax/#Object_Property_Axioms)

Domains and ranges apply to every use of a property. With Frame as the range of hasFrame, every object of a hasFrame relationship is inferred to be a Frame. A class restriction such as “every hasFrame value of a Bicycle is a Frame” applies to Bicycle subjects. Several domains or ranges all apply together; use a union when alternatives are intended. [Domains and ranges](https://www.w3.org/TR/owl2-primer/#Domain_and_Range_Restrictions)

## Property characteristics

| Characteristic | Consequence | Possible relationship |
|---|---|---|
| Functional | Each subject has at most one filler | hasAssignedStorageBay in a fixed allocation |
| Symmetric | A link entails its reverse | sharesStorageWith |
| Transitive | Two consecutive links entail a direct link | isPartOf |

Functionality allows zero fillers. If a functional object property links one subject to two names, both names must identify the same individual. Stating that they differ makes the ontology inconsistent. For a functional data property, distinct values cause inconsistency. Data properties support functionality but none of the other characteristics in this table. [Property characteristics](https://www.w3.org/TR/owl2-primer/#Property_Characteristics)

Identity and difference can also be stated explicitly: `owl:sameAs` states that two names identify the same individual, so class memberships and property assertions about either name apply to both. `owl:differentFrom` states difference. Similarity or matching labels alone justify neither. [Assertions](https://www.w3.org/TR/owl2-syntax/#Assertions)

For changing configurations or repeated measurements, represent the observation context explicitly before imposing functionality or cardinality limits.
