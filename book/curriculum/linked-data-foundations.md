(linked-data-foundations)=
# Linked Data Foundations

## What is Linked Data?

*Linked Data* is an approach to publishing structured data on the Web so that people and applications can find related information by following links.

The approach follows four [Linked Data principles](https://www.w3.org/DesignIssues/LinkedData.html):

1. Use Web identifiers to name things.
2. Use HTTP or HTTPS identifiers that people and applications can look up.
3. When an identifier is looked up, provide useful descriptions using the Resource Description Framework (RDF).
4. Include links to other identifiers, so related information can be discovered.

Linked Data can be access-controlled. *Linked Open Data* is openly accessible under an open licence.

## RDF: the data model for Linked Data

Linked Data uses RDF, a W3C standard data model, to express descriptions and links as statements about *resources*: people, objects, documents or concepts. Each statement is a *triple* with a *subject* (what is described), a *predicate* (the property or relationship) and an *object* (what it relates to, or a value). [RDF Primer](https://www.w3.org/TR/rdf11-primer/)

In the {ref}`bicycle inventory <running-example>`, B001 is the bicycle and F001 its frame:

| Subject | Predicate | Object |
|---|---|---|
| B001 | has component | F001 |
| B001 | has colour | “blue” |
| F001 | has material | “steel” |

RDF uses *IRIs* (Internationalized Resource Identifiers) as names across datasets. The same IRI identifies the same resource wherever it appears, including across datasets. Since another inventory could also have a B001, we use `https://example.org/bike/id/B001` for our bicycle and `https://example.org/bike/id/F001` for its frame. Properties and classes have IRIs too. We use `example.org` as a placeholder domain. [RDF IRIs](https://www.w3.org/TR/rdf11-concepts/#section-IRIs)

## Connecting statements into a knowledge graph

A *knowledge graph* represents things and their relationships in a graph data model. [Hogan et al., *Knowledge Graphs*](https://www.aidanhogan.com/docs/knowledge-graphs-computing-surveys.pdf) This course covers only knowledge graphs that use RDF and follow Linked Data principles.

An *RDF graph* is a set of triples. The diagram adds three statements to those in the table: B001 is a Bicycle, F001 is a Frame, and every Bicycle is a Vehicle. In this compact view, boxes labelled with short resource names are *nodes* connected by labelled arrows. Repeated subject or object IRIs connect statements at the same node.

```mermaid
---
name: bicycle-rdf-graph
align: center
caption: Six RDF statements. Classes have square corners; instances have rounded corners.
alt: B001 has component F001 and has colour blue. F001 has material steel. B001 has type Bicycle and F001 has type Frame. Bicycle is a subclass of Vehicle.
---
%%{init: {"theme": "base", "themeVariables": {"darkMode": false, "background": "#ffffff", "lineColor": "#44546a", "textColor": "#182c3e", "primaryTextColor": "#182c3e", "edgeLabelBackground": "#ffffff"}, "themeCSS": "& { background-color: #ffffff !important; } .edgeLabel, .edgeLabel p { color: #182c3e !important; }"}}%%
block-beta
    columns 4
    Vehicle["Vehicle"] space:3
    space:4
    Bicycle["Bicycle"] space:2 Frame["Frame"]
    space:4
    B001(["<b>B001</b><br/>has colour: &quot;blue&quot;"]) space:2 F001(["<b>F001</b><br/>has material: &quot;steel&quot;"])

    Bicycle -- "subclass of" --> Vehicle
    B001 -- "type" --> Bicycle
    F001 -- "type" --> Frame
    B001 -- "has component" --> F001

    classDef resource fill:#edf3fb,stroke:#406b92,color:#182c3e,stroke-width:2px
    classDef instance fill:#e8f4ee,stroke:#36705a,color:#183c2d,stroke-width:2px
    class Vehicle,Bicycle,Frame resource
    class B001,F001 instance
```

Inside B001's box, “blue” is a text *literal*: a value in the object position of a triple. A literal's *datatype* tells applications how to interpret its written value, for example as text, a number or a date. [RDF literals](https://www.w3.org/TR/rdf11-concepts/#section-Graph-Literal)

Bicycle is a *class* representing a kind of thing, shown in a square box. B001 is a particular bicycle, an *instance* of that class, shown in a rounded box. The *type* arrow from B001 to Bicycle records this membership. [RDF types](https://www.w3.org/TR/rdf-schema/#ch_type)

RDF Schema (RDFS) provides the *subclass of* relationship between classes. Every instance of Bicycle is also an instance of Vehicle, so B001 also belongs to Vehicle. [RDF subclasses](https://www.w3.org/TR/rdf-schema/#ch_subclassof)

An ontology defines classes such as Bicycle and properties such as “has component”, and states that Bicycle is a subclass of Vehicle. The *instance data* uses the IRIs of these terms to describe B001 and F001. RDF can express both the ontology and the instance data. [Ontology terms in RDF](https://www.w3.org/TR/rdf11-primer/#section-vocabulary)

RDF is *flexible*: researchers can extend a graph with new properties and relationships as research needs develop. [RDF data model](https://www.w3.org/RDF/)

Using the same IRI for the same resource connects descriptions across datasets, even when their structures differ. For example, one dataset can link B001 to F001 while another records F001's material. When the graphs are combined, the shared IRI `https://example.org/bike/id/F001` connects these statements at the same node. [Combining RDF graphs](https://www.w3.org/TR/rdf11-concepts/#section-multigraph)

`http://example.org/bike/id/F001` and `https://example.org/bike/id/F001` are different IRIs. A browser may follow a redirect between them. SPARQL, the query language for RDF, matches IRIs exactly, so a query using one can miss data recorded with the other. [IRI comparison](https://www.w3.org/TR/rdf11-concepts/#section-IRIs), [SPARQL matching](https://www.w3.org/TR/sparql11-query/#BasicGraphPatternMatching)

## The data-centric approach

In a *data-centric approach*, domain knowledge is represented explicitly in shared data and ontologies, rather than encoded separately in each application's code. An inventory application and an analysis application can reuse the same bicycle data and the statement that Bicycle is a subclass of Vehicle. Managing data and definitions independently of individual applications can reduce repeated work to prepare data and maintain its definitions. [Data-Centric Manifesto](https://datacentricmanifesto.org/principles/), [Sharing data and domain models](https://www.w3.org/TR/sw-oosd-primer/)

## RDF serialisation: Turtle and other formats

*Serialisation* represents an RDF graph in a format for storage or exchange. Turtle, JSON-LD, RDF/XML and N-Triples are RDF serialisation formats: they can represent the same graph using different syntax. [RDF serialisation formats](https://www.w3.org/TR/rdf11-primer/#section-syntax)

Prefer *Turtle* when creating and sharing ontology files. Its compact syntax makes RDF statements easier to read, edit and check. Use RDF/XML only when no alternative format is supported by the application or publishing workflow. [Discussion of RDF format choice](https://lists.w3.org/Archives/Public/public-lod/2015Sep/0027.html)

We write the bicycle graph in Turtle. *Prefixes* abbreviate IRIs: `id:B001` expands to `https://example.org/bike/id/B001`. Here, `def:` abbreviates class and property IRIs, `id:` individual IRIs and `rdfs:` RDF Schema terms, so `def:Bicycle` expands to `https://example.org/bike/def/Bicycle`. [RDF Turtle](https://www.w3.org/TR/turtle/#simple-triples)

The `@prefix` declarations below define these abbreviations; the remaining lines express the graph's six statements.

As a predicate, `a` is Turtle shorthand for the *type* relationship shown in the diagram (the RDF property `rdf:type`). A semicolon continues statements about the same subject; a full stop ends the block. Triple order does not change the graph.

The colour and material names use `@en` to identify their language as English.

```turtle
@prefix def: <https://example.org/bike/def/> .
@prefix id: <https://example.org/bike/id/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

id:B001 a def:Bicycle ;
    def:hasComponent id:F001 ;
    def:hasColour "blue"@en .

id:F001 a def:Frame ;
    def:hasMaterial "steel"@en .

def:Bicycle rdfs:subClassOf def:Vehicle .
```

If we recorded that B001 has two wheels, `2` would represent an integer that applications can use in calculations, while `"2"` would represent a text string.

## Publishing Linked Data

Our Turtle file already expresses RDF. To publish the graph as Linked Data, make its resource IRIs *dereferenceable*: looking one up retrieves a description of what it identifies. Provide a Web page (a *landing page*) for people and RDF for applications. The description of B001 can link to F001, whose description gives the frame's material; links can also lead to other datasets. [Cool URIs](https://www.w3.org/TR/cooluris/#semweb)

The Web server can supply these RDF descriptions from static files, such as downloadable Turtle files, or retrieve them from a *triple store*, a database for storing and querying RDF. A triple store can also offer a *SPARQL endpoint* for queries over HTTP. {cite}`w3c2014linkeddata` Open-source options include [Apache Jena Fuseki with TDB](https://jena.apache.org/documentation/fuseki2/) and [Eclipse RDF4J Server](https://rdf4j.org/documentation/tools/server-workbench/).

Class and property IRIs work the same way: `def:Bicycle` can lead to its label and relationship to Vehicle. Publish descriptions for new terms and reuse existing term IRIs exactly, including `http:` in the `rdfs:` namespace. [Publishing vocabularies and ontologies](https://www.w3.org/TR/swbp-vocab-pub/#requirements)

Use *persistent identifiers (PIDs)*, managed to remain usable when descriptions move to another Web address. {cite}`w3c2017dwbp` For example, [w3id](https://w3id.org/) provides stable IRIs under `https://w3id.org/` that redirect to your published descriptions. If you move those descriptions, update the redirects while keeping the IRIs unchanged.

Prefer HTTPS for new IRIs and keep the publishing domain's TLS certificate valid for secure access. [HTTPS requirements](https://www.rfc-editor.org/rfc/rfc9110.html#section-4.3.3)

## How Linked Data can support FAIR

The [FAIR principles](https://www.gofair.foundation/fair-principles) aim to make research data and their descriptions (*metadata*) Findable, Accessible, Interoperable and Reusable. {cite}`wilkinson2016fair`

| FAIR goal | How Linked Data contributes |
|---|---|
| Findable | Identifiers and structured metadata help people and applications discover datasets. |
| Accessible | Looking up Web identifiers retrieves descriptions through HTTP(S). |
| Interoperable | RDF, shared terms and explicit relationships help applications combine and interpret data. |
| Reusable | Linked descriptions can record how data were produced and the conditions for reuse. |

FAIR also involves searchable metadata, clear access conditions and a reuse licence.
