# Moving towards production

```{admonition} Under development
:class: warning
This chapter is being written.
```

(owl-ontology-structure)=
## Documentation

The {ref}`building walkthrough <owl-entity-annotations>` introduced labels and definitions as entity annotations. Annotations can also document the ontology, individual axioms or other annotations. An axiom annotation can record evidence for a particular subclass statement. A source or review note helps people assess the statement; adding it leaves the class memberships inferred in our example unchanged. [Annotations](https://www.w3.org/TR/owl2-primer/#Annotating_Axioms_and_Entities)

The {ref}`cheat sheet <owl-cheat-declarations>` gives the declaration, annotation and ontology-header patterns.

(owl-versioning)=
## Versioning

A version IRI identifies a particular ontology version while the ontology IRI stays the same across versions. The ontology IRI, version IRI and document location can differ. [Ontology versioning](https://www.w3.org/TR/owl2-syntax/#Versioning_of_OWL_2_Ontologies)

## Complete bicycle example

The {download}`complete bicycle ontology <../data/bike-ontology-complete.ttl>` illustrates the course's OWL constructs in a fictional inventory study. Component counts apply to configuration snapshots; each mass measurement has its own record. The smaller walkthrough files remain available.

The {download}`model guide <../data/bike-ontology-complete.md>` maps constructs to terms and lists expected reasoning results. The {download}`complete package <../data/bike-ontology-complete.zip>` also includes a small study ontology and local catalog for trying imports in Protégé.

The identifiers use `example.org` placeholders. Publishing a real ontology also requires maintained identifiers and working Web resolution.
