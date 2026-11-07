# Reuse Existing Ontologies and Vocabularies

Reusing existing ontologies and vocabularies, and connecting your ontology to them.

```{admonition} Under development
:class: warning
This chapter is being written. By the end of it, you will be able to:

- Explain why and when to map an ontology to external ontologies and vocabularies
- Find suitable ontologies and vocabularies, and suitable terms within them, using standard resources
- Compare mapping approaches and choose one that fits, including [SHACL-AF rules](https://www.w3.org/TR/shacl-af/#rules) for deriving RDF triples with terms from another ontology
```

## Reuse, extend or build

Before creating a new ontology, check which ontologies your research community uses and which terms the datasets you want to use already refer to. In RDF data, the class and property IRIs can identify those terms. You can reuse suitable terms, extend an existing ontology with missing concepts, or create new terms where existing models do not express the meaning you need. These choices can be combined. {cite}`noy2001ontology`

When assessing an existing ontology, check:

- Whether its definitions, relationships and logical statements fit your intended meaning and level of detail.
- Whether relevant research communities or collaborating projects use it.
- Whether documentation, a licence and information about maintenance and versions are available.

Read the definitions and logical statements behind a promising term: matching labels alone do not establish a match in meaning. {cite}`w3c2017dwbp,w3c2014linkeddata`

In this training, building a small ontology helps you understand these modelling choices. In a research project, evaluating existing ontologies belongs at the beginning.
