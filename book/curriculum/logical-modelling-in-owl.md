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

The {download}`complete bicycle ontology <../data/bicycle-ontology-complete.ttl>` illustrates the course's OWL constructs in a fictional inventory study. Component counts apply to configuration snapshots; each mass measurement has its own record. The smaller walkthrough files remain available.

The {download}`model guide <../data/bicycle-ontology-complete.md>` maps constructs to terms and lists expected reasoning results. The {download}`complete package <../data/bicycle-ontology-complete.zip>` also includes a small study ontology and local catalog for trying imports in Protégé.

The identifiers use `example.org` placeholders. Publishing a real ontology also requires maintained identifiers and working Web resolution.
:::
