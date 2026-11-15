# References

## W3C standards and guides

The training uses RDF 1.1, OWL 2 and SPARQL 1.1. Start with the primers; consult the specifications for definitions and details.

### Primers and guides

| Reference | Use it for |
|---|---|
| [RDF 1.1 Primer](https://www.w3.org/TR/rdf11-primer/) | An introduction to RDF with examples |
| [OWL 2 Primer](https://www.w3.org/TR/owl2-primer/) | An introduction to OWL with examples |
| [OWL 2 Document Overview](https://www.w3.org/TR/owl2-overview/) | A guide to the OWL specifications |
| [OWL 2 Quick Reference](https://www.w3.org/TR/owl2-quick-reference/) | A summary of OWL constructs |
| [OWL 2 Manchester Syntax](https://www.w3.org/TR/owl2-manchester-syntax/) | Readable OWL syntax used in Protégé |
| [SKOS Primer](https://www.w3.org/TR/skos-primer/) | Concept schemes, labels and mappings |
| [SPARQL 1.1 Overview](https://www.w3.org/TR/sparql11-overview/) | A guide to queries, updates, protocols and result formats |

### Specifications

| Reference | Use it for |
|---|---|
| [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf11-concepts/) | Resources, triples, graphs and datasets |
| [RDF Schema 1.1](https://www.w3.org/TR/rdf-schema/) | Classes, properties, domains and ranges |
| [RDF 1.1 Semantics](https://www.w3.org/TR/rdf11-mt/) | Interpretation and inference in RDF and RDFS |
| [OWL 2 Structural Specification and Functional-Style Syntax](https://www.w3.org/TR/owl2-syntax/) | OWL entities, expressions and axioms |
| [OWL 2 Direct Semantics](https://www.w3.org/TR/owl2-direct-semantics/); [OWL 2 RDF-Based Semantics](https://www.w3.org/TR/owl2-rdf-based-semantics/) | Formal meaning of OWL statements |
| [OWL 2 Mapping to RDF Graphs](https://www.w3.org/TR/owl2-mapping-to-rdf/) | Representing OWL as RDF |
| [OWL 2 Profiles](https://www.w3.org/TR/owl2-profiles/) | Restricted forms of OWL for different reasoning needs |
| [SKOS Reference](https://www.w3.org/TR/skos-reference/) | Concept schemes, labels, hierarchies and mappings |
| [SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/) | Querying RDF data |
| [SPARQL 1.1 Update](https://www.w3.org/TR/sparql11-update/) | Adding, changing and removing RDF data |
| [Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/) | Checking RDF data against conditions |
| [XSD 1.1 Part 2: Datatypes](https://www.w3.org/TR/xmlschema11-2/) | Datatypes for text, numbers, dates and other values |

### File formats

| Reference | Use it for |
|---|---|
| [RDF 1.1 Turtle](https://www.w3.org/TR/turtle/) | Compact graph syntax used in the training's `.ttl` files |
| [RDF/XML](https://www.w3.org/TR/rdf-syntax-grammar/) | XML syntax for RDF graphs |
| [JSON-LD 1.1](https://www.w3.org/TR/json-ld11/) | JSON-based linked data |
| [N-Triples](https://www.w3.org/TR/n-triples/) | Line-based graph syntax |
| [TriG](https://www.w3.org/TR/trig/) | Turtle-style dataset syntax, including named graphs |
| [N-Quads](https://www.w3.org/TR/n-quads/) | Line-based dataset syntax |
| [OWL 2 XML Serialization](https://www.w3.org/TR/owl2-xml-serialization/) | OWL-specific XML syntax, distinct from RDF/XML |

### Identifiers and publication

| Reference | Use it for |
|---|---|
| [Cool URIs for the Semantic Web](https://www.w3.org/TR/cooluris/) | Choosing identifiers that can be looked up on the web |
| [Best Practice Recipes for Publishing RDF Vocabularies](https://www.w3.org/TR/swbp-vocab-pub/) | Publishing ontologies and vocabularies |
| [Data on the Web Best Practices](https://www.w3.org/TR/dwbp/) | Identifiers, documentation, licensing and versioning |

(ontology-development-guidance)=
## Optional guidance on ontology development

- [Ontology Development 101](https://protege.stanford.edu/publications/ontology_development/ontology101.pdf) (2001): process guidance on scope, reuse and iterative modelling. Its examples use older tools; this course uses OWL 2.
- [OBO Academy](https://oboacademy.github.io/obook/): community training on OWL and ontology curation, with a biological and biomedical focus. Its [SubClassOf versus EquivalentTo](https://oboacademy.github.io/obook/explanation/subClassOf-vs-equivalentTo/) explanation uses diagrams to compare the two axioms.

## Related work

### Books

- [Semantic Web for the Working Ontologist](https://www.sciencedirect.com/book/monograph/9780123859655/semantic-web-for-the-working-ontologist) (Allemang and Hendler, 2nd ed., 2011): worked examples of modelling with RDF, RDFS and OWL, and querying with SPARQL.
- [An Introduction to Ontology Engineering](https://people.cs.uct.ac.za/~mkeet/OEbook/) (Keet, 2nd ed., 2025): a more technical treatment of formal foundations and ontology development methods. The author's site also provides an earlier open edition.

### Ontology development methodologies

- [METHONTOLOGY](https://cdn.aaai.org/Symposia/Spring/1997/SS-97-06/SS97-06-005.pdf) (Fernández-López et al., 1997): a lifecycle approach using evolving prototypes, with evaluation and documentation throughout development.
- [NeOn](https://doi.org/10.1007/978-3-642-24794-1_2) (Suárez-Figueroa et al., 2012): guidance for different development scenarios, particularly reusing and combining existing knowledge resources.
- [LOT (Linked Open Terms)](https://lot.linkeddata.es/) ([Poveda-Villalón et al., 2022](https://doi.org/10.1016/j.engappai.2022.104755)): an iterative workflow covering requirements, implementation, publication and maintenance, with practical guidance and workflow diagrams.

## Bibliography

:::{bibliography}
:::
