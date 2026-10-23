# Introduction

## Why ontologies?

An ontology is a formal, explicit specification of a shared conceptualization. {cite}`studer1998knowledge`

A conceptualization is a model of the things and relationships relevant to a domain, or area of interest. Shared means agreed by a community. The terms and assumptions are stated explicitly, in a formal language that software can interpret.

An ontology represents the meaning of data in a model that can be reused across applications. Shared definitions support standardisation and interoperability by helping projects interpret data consistently and link or combine datasets for further studies. Interoperability is the “I” in [FAIR](https://www.gofair.foundation/fair-principles): Findable, Accessible, Interoperable and Reusable data. People can inspect the model's assumptions and decide whether it fits their data.

Models from different fields can be connected where their concepts overlap. These links help researchers investigate questions that span disciplines. {cite}`bernerslee2004connectingsciences`

## Why OWL?

OWL, the Web Ontology Language, is an open W3C standard. This training uses OWL 2. Its public specification gives compatible tools a common language with defined meaning, so models can be exchanged across software.

OWL builds on RDF, the Resource Description Framework, which represents data as linked statements. OWL ontologies can themselves be represented as RDF, so the model can be shared and queried with the same technologies as the data. {cite}`w3c2012owl2overview`

A *reasoner* uses the ontology's statements to infer additional facts and check for logical inconsistencies. {cite}`w3c2012owl2primer`

Terms should ideally have stable web identifiers that are dereferenceable: looking one up retrieves information about the term. Publishers can provide definitions on landing pages for people and RDF descriptions for software. {cite}`sauermann2008cooluris`

## Vocabularies, taxonomies and ontologies

These approaches support different tasks:

| Approach | Main purpose | Typical use |
|---|---|---|
| Controlled vocabulary | Agree on terms or concepts and their use | Selecting keywords or recording values consistently |
| Taxonomy | Organise concepts in a hierarchy | Browsing or grouping data under broader and narrower categories |
| Ontology | Specify kinds of things and their relationships, with explicit statements about meaning | Sharing a domain model and deriving consequences from its statements |

These approaches overlap. A taxonomy can be a controlled vocabulary, and an ontology can include a taxonomy. A thesaurus is a controlled vocabulary with relationships such as “broader than”, “narrower than” and “related to” between its concepts.

Glossaries explain terms; data dictionaries document dataset fields. Both can accompany any of these approaches.

## The bicycle example

We will use a bicycle inventory. The model distinguishes a bicycle from its frame, so “steel” can describe the frame's material.

In OWL, we can define a kind of bicycle as “a bicycle that has a frame made of steel”. A reasoner can then infer that classification from the recorded facts about a bicycle and its frame.

Using the class hierarchy, we can also find bicycles when querying for vehicles.

Continue with the [bicycle example](running-example.md). We start by building a small ontology, then learn how to find, evaluate and reuse existing ones. In a research project, checking existing resources is part of deciding what to build.

Links to the relevant [W3C standards and guides](../references.md) are collected on the References page.
