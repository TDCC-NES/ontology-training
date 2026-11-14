# Use your ontology

Our research team wants to compare recorded frame materials across bicycle inventories. We now use the ontology to represent the records as RDF and answer the competency question from chapter 3: “Which bicycles have a frame recorded as steel?”

<!-- Existing learning-outcome draft, retained for later course development:
By the end of it, you will be able to:

- Transform data into RDF using your ontology
- Connect instance data to an ontology, and query and visualise the result
- Use a reasoner to draw inferences over instance data
-->

## Transform data into RDF

Start with one representative record: write its expected RDF by hand, automate the conversion of that same record and compare the two graphs. Once the conversion produces the intended statements, apply it to the full dataset.

### Check the source data

Check data quality before designing the conversion. Look for missing or duplicate identifiers, incorrect links between records, inconsistent material names and differences in datatypes or units. For example, establish whether `steel` and `Steel` mean the same material in the source inventories, and agree a consistent output value. Preserve the original data and record any changes you make.

For our records, “Not recorded” marks a missing material value. Leave that value absent in RDF, as for F003; this preserves the distinction between a material name and missing information.

### Write a reference record by hand

Mapping data to RDF means choosing which resources the records describe and which ontology terms express their types, relationships and values. For the representative records in chapter 3:

| Inventory field | RDF representation |
|---|---|
| Bicycle identifier | Individual IRI, such as `id:B001`, with type `def:Bicycle` |
| Frame identifier | Individual IRI, such as `id:F001`, with type `def:Frame` |
| Bicycle's frame | `def:hasComponent` links the bicycle to its frame |
| Frame material | `def:hasMaterial` links the frame to language-tagged text |
| Bicycle colour | `def:hasColour` links the bicycle to language-tagged text |

Use the IRI strategy agreed in chapter 3. Reuse a resource's IRI when combining descriptions of that same resource. [RDF descriptions and identifiers](https://www.w3.org/TR/rdf11-primer/#section-data-model)

For B001, the expected data graph contains five triples. Write these in a text editor and save the file as `sample-reference.ttl`:

```turtle
@prefix def: <https://example.org/bike/def/> .
@prefix id: <https://example.org/bike/id/> .

id:B001 a def:Bicycle ;
    def:hasComponent id:F001 ;
    def:hasColour "blue"@en .

id:F001 a def:Frame ;
    def:hasMaterial "steel"@en .
```

The material describes F001, the frame; B001 links to that frame through `hasComponent`. This record uses the ontology's terms to describe the particular bicycle and frame.

### Automate the same record

We will use [RML (RDF Mapping Language)](https://rml.io/specs/rml/), a mapping language with a published specification, to express the mapping as reusable rules. The mapping itself is an RDF graph, written here in Turtle, so you can also inspect its rules with RDF tools and query them with SPARQL. An RML processor applies those rules to the source data.

Download the {download}`source CSV <../data/bicycle-inventory.csv>` and {download}`RML mapping <../data/bicycle-inventory.rml.ttl>` into the same folder as `sample-reference.ttl`. The CSV contains the three records from chapter 3; F003's material cell is empty.

The mapping has two *triples maps*: one creates bicycles, their component links and colours; the other creates frames and their materials. `rr:template` builds IRIs from identifier columns, `rr:class` assigns a type, and `rml:reference` reads a column value. Both literal mappings use `rr:language "en"`. Source spellings are preserved; empty material cells produce no material statement in this example.

:::{dropdown} Set up RMLMapper

This example was tested with [RMLMapper 8.1.0](https://github.com/RMLio/rmlmapper-java/releases/tag/v8.1.0). Download its standalone JAR (the file ending in `-all.jar`), rename it `rmlmapper.jar` and install the Java version required by that release. Put the JAR beside the downloaded files and open a terminal in that folder.

The mapping uses the original RML vocabulary, which RMLMapper supports. [RMLMapper instructions](https://github.com/RMLio/rmlmapper-java#usage)
:::

For the first run, keep a copy of the full CSV elsewhere and leave only the header and B001 row in `bicycle-inventory.csv`. Run:

```sh
java -jar rmlmapper.jar -m bicycle-inventory.rml.ttl -o sample-generated.ttl -s turtle
```

The output should contain the same five triples as your reference record.

:::{dropdown} Conversion methods (optional)

Choose a method that suits the source format, required transformations and the team's experience.

| Method | How it applies the mapping |
|---|---|
| Scripts | Use code to prepare source data and create IRIs, literals and triples, with custom logic where needed. |
| [RML](https://rml.io/specs/rml/) | Express reusable mapping rules in RDF; an RML processor applies them to sources such as CSV, JSON or XML. |
| [SPARQL Anything](https://sparql-anything.readthedocs.io/stable/) | Access sources such as CSV, JSON or spreadsheets through an RDF view, then use a SPARQL `CONSTRUCT` query to generate triples. |

These methods can be combined: scripts can clean material names before an RML conversion, run the conversion when records change and load the results into a triple store.

Use the same IRI patterns, links, datatypes, language tags and rules for missing values as in your reference record.
:::

### Compare the graphs

Compare the five reference triples with the generated record: check full IRIs, the direction of links, literal values and language tags. For example, `hasMaterial "steel"@en` belongs on F001, the frame. Compare the record triples only, leaving out class and property declarations. Prefixes, formatting and triple order can differ while expressing the same graph. Inspect the sample in Protégé's [individual views](https://protegeproject.github.io/protege/getting-started/#navigation) or the graph views from chapter 4, and correct any differences against the source record.

### Convert all records

Resolve differences in the sample conversion, then check records with other materials and missing values. Restore the full `bicycle-inventory.csv` and run the same mapping with a new output filename:

```sh
java -jar rmlmapper.jar -m bicycle-inventory.rml.ttl -o inventory-data.ttl -s turtle
```

The output contains 14 record triples. F003 is recorded as a Frame, with no material value. Review any conversion errors and unexpected omissions, and keep the source data, mapping and reference examples so the process can be repeated when records change.

You can query `inventory-data.ttl` below. The supplied {download}`bicycle inventory <../data/bicycle-inventory.ttl>` contains the same record triples and adds the statement that Bicycle is a subclass of Vehicle.

## Query with SPARQL (with or without inferences)

*SPARQL* is a query language for RDF. A query describes a pattern of statements to match and specifies what information to return. We will use it to answer: “Which bicycles have a frame recorded as steel?”

### Load and query the data in a triple store

For repeated querying and use by applications, load the converted data into a *triple store*, a database for storing and querying RDF. Researchers can use its query interface; applications can send queries over HTTP to its *SPARQL endpoint*.

1. Select or create a dataset in a triple store available to your team.
2. Load `inventory-data.ttl` or the supplied `bicycle-inventory.ttl` into its *default graph*, which the query below searches.
3. Open the SPARQL query editor and run the query below. It needs no reasoning.

:::{dropdown} Triple-store applications (optional)

Options include [QLever](https://docs.qlever.dev/quickstart/), [Apache Jena Fuseki with TDB](https://jena.apache.org/documentation/fuseki2/fuseki-quick-start.html) and [Eclipse RDF4J Server and Workbench](https://rdf4j.org/documentation/tools/server-workbench/). Follow the chosen application's setup and loading instructions: QLever builds an index from RDF files; Fuseki also offers file uploads.
:::

`PREFIX` defines the same IRI abbreviation as `@prefix` in Turtle. Names beginning with `?` are variables whose values will be found by matching the patterns:

```sparql
PREFIX def: <https://example.org/bike/def/>

SELECT DISTINCT ?bicycle
WHERE {
    ?bicycle a def:Bicycle ;
        def:hasComponent ?frame .
    ?frame a def:Frame ;
        def:hasMaterial "steel"@en .
}
```

The patterns inside `WHERE` use the familiar Turtle forms `a` and `;`. The same `?frame` in both patterns connects each bicycle to its frame's material. `SELECT` chooses the variable to return, and `DISTINCT` returns each matching bicycle once, even if several frames match. The result is `https://example.org/bike/id/B001`; the query interface may display an abbreviated name. [SPARQL basic queries](https://www.w3.org/TR/sparql11-query/#WritingSimpleQueries)

The material pattern matches the language-tagged value `"steel"@en`. `"Steel"@en`, `"steel"@nl` and the untagged string `"steel"` are different RDF terms. Consistent source-data preparation and conversion make these matches reliable.

B002 and B003 have no matching steel-frame statements in this graph. This result identifies recorded matches; it does not establish that those bicycles have no steel frames.

Query results can also feed the graph views introduced in chapter 4; return the identifiers, links or values needed by the chosen view.

### Querying inferred information

To query inferred information, load the relevant ontology axioms and enable reasoning supported by the store, or load previously inferred statements. Using ontology term IRIs in the data does not load the axioms. Check which RDFS or OWL features the store supports. [RDF4J configuration](https://rdf4j.org/documentation/programming/repository/), [Jena inference support](https://jena.apache.org/documentation/inference/)

For example, with Bicycle declared a subclass of Vehicle, RDFS reasoning lets `?bicycle a def:Vehicle` retrieve B001 from its Bicycle membership. The frame-material query above matches the recorded statements directly. [SPARQL entailment regimes](https://www.w3.org/TR/sparql11-entailment/)

:::{dropdown} Try the small example in Protégé (optional)

You can also try the query on a few records in Protégé:

1. Download `bicycle-inventory.ttl` above and open it through **File > Open** in a separate Protégé window, keeping the chapter 5 working ontology separate.
2. Enable **Window > Tabs > SPARQL Query** and select the tab. This is the SPARQL editor; **DL Query** uses the Manchester expressions introduced in chapter 5.
3. Replace the example query with the frame-material query above and click **Execute**. The result appears in the table beneath the editor. [Protégé SPARQL plugin](https://github.com/protegeproject/sparql-query-plugin)

The standard **SPARQL Query** tab queries recorded axioms. To query HermiT's conclusions there, first {ref}`export the inferred assertions <export-inferred-assertions>` and open the export separately.
:::
