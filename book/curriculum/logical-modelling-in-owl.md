# Logical modelling in OWL 2

In the preceding chapter, the reasoner inferred that B001 is a Vehicle. Here, we define classes using logical conditions so it can recognise bicycles whose frames are recorded as steel. We also explore property axioms and identity, interpret inferences and check consistency.

{doc}`advanced-owl-modelling` covers optional constructs and language choices. The {doc}`OWL 2 cheat sheet <owl2-cheat-sheet>` provides the syntax reference.

<!-- Existing learning-outcome draft, retained for later course development:
By the end of it, you will be able to:

- Read and write OWL 2 axioms, restrictions, and expressions
- Use the cheat sheet to look up OWL 2 syntax while modelling
-->

```{tableofcontents}
```

:::{dropdown} Complete bicycle example (reference)

The {download}`complete bicycle ontology <../data/bike-ontology-complete.ttl>` illustrates the course's OWL constructs in a fictional inventory study. Component counts apply to configuration snapshots; each mass measurement has its own record. The smaller walkthrough files remain available.

The {download}`model guide <../data/bike-ontology-complete.md>` maps constructs to terms and lists expected reasoning results. The {download}`complete package <../data/bike-ontology-complete.zip>` also includes a small study ontology and local catalog for trying imports in Protégé.

The identifiers use `example.org` placeholders. Publishing a real ontology also requires maintained identifiers and working Web resolution.
:::
