# Introduction to ontologies

## Why ontologies?

Making the meaning of research data explicit can help researchers describe, publish, find, integrate and reuse it. This includes recording domain knowledge independently of individual applications: what the data represents and how the things it describes relate to each other. 

In this training, we use the following definition: "*An ontology is a formal, explicit specification of a shared conceptualisation*". {cite}`studer1998knowledge` A conceptualisation is a model of the things and relationships relevant to a domain, or area of interest. Shared means agreed by a community. The terms and assumptions are stated explicitly, in a formal language that applications can interpret.

Researchers can use an ontology to describe their data, helping others inspect the model's assumptions and assess whether the data fits their own work. Shared definitions help researchers interpret data consistently across projects, supporting standardisation and interoperability, the “I” in [FAIR](https://www.gofair.foundation/fair-principles): Findable, Accessible, Interoperable and Reusable data.

Models from different fields can be connected where their concepts overlap. These links help researchers investigate questions that span multiple disciplines. {cite}`bernerslee2004connectingsciences`

## Ontologies and related approaches

These approaches serve different purposes and can be combined. 

| Approach | What it provides |
|---|---|
| Glossary | Explanations of the meanings of terms |
| Data dictionary | Descriptions of dataset fields, including their meanings, data types and permitted values |
| Controlled vocabulary | Agreed terms or concepts for consistent description and indexing |
| Taxonomy | Concepts organised in a hierarchy of broader and narrower categories |
| Thesaurus | Hierarchical and associative relationships between concepts, with preferred and alternative labels |
| Ontology | Classes (kinds of things), properties (attributes and relationships), and formal statements describing them |

These approaches are not muntually exclusive. For example, taxonomies and thesauri are forms of controlled vocabulary. {cite}`isaac2009skosprimer` And an ontology typically includes a taxonomy of classes. {cite}`w3c2012owl2primer`

## Why OWL?

Ontologies can be represented in different ways. This training focuses on OWL 2 (Web Ontology Language), an open W3C standard for representing ontologies on the Web. Its public specification gives tools a common language with defined meaning, so models can be exchanged. Applications can use an OWL ontology to infer additional facts and check for logical inconsistencies. {cite}`w3c2012owl2primer`

OWL builds on RDF, the Resource Description Framework, which is also an open W3C standard and expresses information as statements about things and their relationships. Every OWL 2 ontology has a standard RDF representation, so the model can be shared and queried with the same technologies as the data. {cite}`w3c2012owl2overview`

(running-example)=
## The bicycle example

We will use a bicycle inventory as a running example throughout the training.

B001 is our fictional blue cargo bicycle, or *bakfiets* in Dutch. It has two wheels, a cargo box and a steel frame, identified as F001. Cargo bicycles are designed to carry loads in addition to the rider, such as passengers or goods.

![B001, a blue two-wheeled cargo bicycle with a cargo box in front of the rider.](../figures/b001-cargo-bicycle.svg)

To answer a question such as “Which bicycles have steel frames?”, we need to record which bicycle has which frame and the frame's material. An ontology can define bicycles, frames and their properties and relationships in a shared model, so different inventories can describe them consistently.

Links to the relevant [W3C standards and guides](../references.md) are collected on the References page.
