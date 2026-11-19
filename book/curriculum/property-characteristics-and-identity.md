(owl-assertions)=
# Property characteristics and identity

In the initial OWL walkthrough, we recorded statements such as “B001 is a Bicycle” and “B001 has component F001”. These *assertions* describe particular individuals through class memberships, relationships and values.

Here, property axioms describe a property's behaviour across all its uses. Class restrictions describe conditions on class members. The following examples are separate modelling choices using the course prefixes; keep `bike-logical.ttl` as saved in the preceding section.

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

From B001 hasComponent F001, infer F001 isComponentOf B001. For equivalent properties, a link using either property also holds with the other. Disjoint properties cannot both link the same subject to the same object. Subproperties, equivalence and disjointness also apply to data properties, where the object is a data value. [Property axioms](https://www.w3.org/TR/owl2-syntax/#Object_Property_Axioms)

Domains and ranges apply to every use of a property. With Frame as the range of hasFrame, every object of a hasFrame relationship is inferred to be a Frame. A class restriction such as “every hasFrame value of a Bicycle is a Frame” applies to Bicycle subjects. Several domains or ranges all apply together; the {ref}`optional union example <owl-union-complement>` shows how to express alternatives. [Domains and ranges](https://www.w3.org/TR/owl2-primer/#Domain_and_Range_Restrictions)

## Characteristics and identity

For these examples, suppose the team assigns storage bays to its bicycles. Tube001 is a tube in B001's frame F001.

| Characteristic | Consequence | Bicycle example |
|---|---|---|
| Functional | Each subject has at most one filler | B001 hasAssignedStorageBay Bay01 in a fixed allocation. |
| Symmetric | A link entails its reverse | B001 sharesStorageWith B002 entails B002 sharesStorageWith B001. |
| Transitive | Two consecutive links entail a direct link | Tube001 isPartOf F001 and F001 isPartOf B001 entail Tube001 isPartOf B001. |

Functionality allows zero fillers. If B001's functional hasAssignedStorageBay property also links it to Bay02, Bay01 and Bay02 must name the same bay. Stating that the bays differ makes the ontology inconsistent. For a functional data property, distinct values cause inconsistency. Data properties support functionality but none of the other characteristics in this table. [Property characteristics](https://www.w3.org/TR/owl2-primer/#Property_Characteristics)

Identity and difference can also be stated explicitly: `owl:sameAs` states that two names identify the same individual, so class memberships and property assertions about either name apply to both. `owl:differentFrom` states difference. Similarity or matching labels alone justify neither. [Assertions](https://www.w3.org/TR/owl2-syntax/#Assertions)

For changing configurations or repeated measurements, represent the observation context explicitly before imposing functionality or cardinality limits.
