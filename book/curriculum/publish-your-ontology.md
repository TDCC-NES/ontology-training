# Publish your ontology

```{admonition} Under development
:class: warning
This chapter is being written.
```

(owl-versioning)=
## Version identifiers

A version IRI identifies a particular ontology version while the ontology IRI stays the same across versions. The ontology IRI, version IRI and document location can differ. [Ontology versioning](https://www.w3.org/TR/owl2-syntax/#Versioning_of_OWL_2_Ontologies)

(owl-ontology-structure)=
## Documentation

The {ref}`building walkthrough <owl-entity-annotations>` introduced labels and definitions as entity annotations. Annotations can also document the ontology, individual axioms or other annotations. An axiom annotation can record evidence for a particular subclass statement. A source or review note helps people assess the statement; adding it leaves the class memberships inferred in our example unchanged. [Annotations](https://www.w3.org/TR/owl2-primer/#Annotating_Axioms_and_Entities)

The {ref}`cheat sheet <owl-cheat-declarations>` gives the declaration, annotation and ontology-header patterns.

## Check metadata and documentation

Before publication, agree the required metadata and use the {ref}`ontology-validation method <ontology-shacl-check>` to check their presence in the RDF. For example, a project can require an ontology title and a licence IRI. Choose shapes that match the project's publishing requirements; [TIB's draft metadata recommendations](https://github.com/TIBHannover/terminology-metadata) provide examples for ontologies and their terms.

Review the rendered documentation as well: check that labels and definitions display correctly, term links resolve, and the licence and version information agree with the RDF.
