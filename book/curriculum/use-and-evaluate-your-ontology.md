(use-your-ontology)=
(evaluate-your-ontology-and-data)=
(ontology-data-checks)=
# Use and evaluate your ontology

:::{admonition} Learning objectives
:class: note

By the end of this chapter, you will be able to:

- Choose checks for intended meaning, logical consistency and data requirements.
- Transform source records into RDF using an ontology and a supplied mapping.
- Check that generated RDF preserves the intended identifiers, relationships and values.
- Use a SPARQL query to answer a competency question.
- Compare competency-query results with expected answers.
- Explain how ontology axioms and inference support affect query results.
- Validate ontology and instance data with SHACL shapes and interpret the reports.
- Use findings to decide what needs revision and repeat the relevant checks.
:::

Our research team wants to compare recorded frame materials across bicycle inventories. We now use the ontology to represent the records as RDF and answer the competency question from chapter 3: “Which bicycles have a frame recorded as steel?”

The {download}`supplied inventory RDF <../data/bicycle-inventory.ttl>` lets you follow the checks without running the conversion.

(choose-the-right-check)=
## Choose appropriate checks

The following checks apply to both ontologies and instance data:

| Check | What to review | Main explanation |
|---|---|---|
| Reading statements aloud | Whether the statements express the intended meaning, including which thing a value describes and the direction of a relationship | {ref}`Sketch review <read-model-aloud>` and {ref}`reference RDF <reference-rdf>` |
| OWL reasoning | Logical consistency, class satisfiability and whether inferred conclusions match the intended meaning | {ref}`Reasoning checks <owl-reasoning>` |
| Competency-question tests | Whether queries return the expected answers for chosen records and inference settings | {ref}`Query tests <competency-question-tests>` |
| SHACL validation | Whether selected resources satisfy chosen requirements for recorded values or documentation | {ref}`SHACL basics <shacl-basics>` |

## Transform data into RDF

We will apply the supplied mapping to the three inventory records and inspect the resulting RDF before querying it.

### Check the source data

Check data quality before designing the conversion. Look for missing or duplicate identifiers, incorrect links between records, inconsistent material names and differences in datatypes or units. For example, establish whether `steel` and `Steel` mean the same material in the source inventories, and agree a consistent output value. Preserve the original data and record any changes you make.

For our records, “Not recorded” marks a missing material value. Leave that value absent in RDF, as for F003; this preserves the distinction between a material name and missing information.

### Map the source fields

Mapping data to RDF means choosing which resources the records describe and which ontology terms express their types, relationships and values. For the representative records in chapter 3:

| Inventory field | RDF representation |
|---|---|
| Bicycle identifier | Individual IRI, such as `id:B001`, with type `def:Bicycle` |
| Frame identifier | Individual IRI, such as `id:F001`, with type `def:Frame` |
| Bicycle's frame | `def:hasComponent` links the bicycle to its frame |
| Frame material | `def:hasMaterial` links the frame to language-tagged text |
| Bicycle colour | `def:hasColour` links the bicycle to language-tagged text |

Use the IRI strategy agreed in chapter 3. Reuse a resource's IRI when combining descriptions of that same resource. [RDF descriptions and identifiers](https://www.w3.org/TR/rdf11-primer/#section-data-model)

(reference-rdf)=
### Review the reference RDF

Before running a conversion, write the expected RDF for one source record. For B001, the mapping above gives these five reference triples:

```turtle
@prefix def: <https://example.org/bike/def/> .
@prefix id: <https://example.org/bike/id/> .

id:B001 a def:Bicycle ;
    def:hasComponent id:F001 ;
    def:hasColour "blue"@en .

id:F001 a def:Frame ;
    def:hasMaterial "steel"@en .
```

As when {ref}`reviewing the sketch <read-model-aloud>`, read these triples aloud, adding connecting words where needed:

| Triple | Read as |
|---|---|
| `id:B001 a def:Bicycle .` | B001 is a Bicycle. |
| `id:B001 def:hasComponent id:F001 .` | B001 has component F001. |
| `id:B001 def:hasColour "blue"@en .` | B001 has colour blue. |
| `id:F001 a def:Frame .` | F001 is a Frame. |
| `id:F001 def:hasMaterial "steel"@en .` | F001 has material steel. |

Follow B001's component link to F001: the material describes the frame. Review the sentences yourself or with colleagues, and compare their claims with the source record. “F001 has material aluminium” reads naturally but conflicts with this record. Revise the model or mapping if it expresses a different claim from the one intended.

Dean Allemang and Jim Hendler discuss reading triples aloud (p. 39) and avoiding misleading readings through clear labels (p. 310). {cite}`allemang2011semantic` For complex OWL axioms, read the connected triples together to express the complete logical statement. [OWL-to-RDF mapping](https://www.w3.org/TR/owl2-mapping-to-rdf/)

### Convert the records with RML

We will use [RML (RDF Mapping Language)](https://rml.io/specs/rml/), a mapping language with a published specification, to express the mapping as reusable rules. The mapping itself is an RDF graph, written here in Turtle, so you can also inspect its rules with RDF tools and query them with SPARQL. An RML processor applies those rules to the source data.

Download the {download}`source CSV <../data/bicycle-inventory.csv>` and {download}`RML mapping <../data/bicycle-inventory.rml.ttl>` into the same folder. The CSV contains the three records from chapter 3; F003's material cell is empty.

The mapping has two *triples maps*: one creates bicycles, their component links and colours; the other creates frames and their materials. `rr:template` builds IRIs from identifier columns, `rr:class` assigns a type, and `rml:reference` reads a column value. Both literal mappings use `rr:language "en"`. Source spellings are preserved; empty material cells produce no material statement in this example.

:::{dropdown} Set up RMLMapper

This example was tested with [RMLMapper 8.1.0](https://github.com/RMLio/rmlmapper-java/releases/tag/v8.1.0), which requires Java 21 or newer. A JAR file packages a Java application; a terminal lets you run commands by typing them.

1. Install [Java 21 or newer](https://learn.microsoft.com/en-us/java/openjdk/install) for your operating system.
2. Download RMLMapper's standalone JAR (the file ending in `-all.jar`), rename it `rmlmapper.jar` and put it beside the CSV and mapping.
3. Open **Terminal** on macOS or Linux, or **PowerShell** on Windows. Type `java -version` and press Enter. It should report version 21 or newer. If the command is unavailable after installation, close and reopen the terminal.

Use `cd` to select the folder containing your files. Replace the example path below with that folder's full path, keeping the quotation marks:

```sh
cd "path/to/your/folder"
```

Type `ls` on macOS or Linux, or `dir` on Windows, to list the files. You should see `rmlmapper.jar`, `bicycle-inventory.csv` and `bicycle-inventory.rml.ttl`. Run the conversion command below in this same terminal.

The mapping uses the original RML vocabulary, which RMLMapper supports. [RMLMapper instructions](https://github.com/RMLio/rmlmapper-java#usage)
:::

Run the mapping on the full CSV:

```sh
java -jar rmlmapper.jar -m bicycle-inventory.rml.ttl -o inventory-data.ttl -s turtle
```

:::{dropdown} Conversion methods (optional)

Choose a method that suits the source format, required transformations and the team's experience.

| Method | How it applies the mapping |
|---|---|
| Scripts | Use code to prepare source data and create IRIs, literals and triples, with custom logic where needed. |
| [RML](https://rml.io/specs/rml/) | Express reusable mapping rules in RDF; an RML processor applies them to sources such as CSV, JSON or XML. |
| [SPARQL Anything](https://sparql-anything.readthedocs.io/stable/) | Access sources such as CSV, JSON or spreadsheets through an RDF view, then use a SPARQL `CONSTRUCT` query to generate triples. |

These methods can be combined: scripts can clean material names before an RML conversion, run the conversion when records change and load the results into a triple store.

Use consistent IRI patterns, links, datatypes, language tags and rules for missing values across conversion methods.
:::

(check-the-converted-rdf)=
(rdf-conversion-checks)=
### Check the converted RDF against source records

The output contains 14 record triples. Open it in a text editor and check the identifiers, component links, values and language tags against the source records. Read the generated statements as sentences too. For example, B001 should link to F001, whose material is `"steel"@en`; F003 should be recorded as a Frame with no material value. Review any conversion errors and unexpected omissions, and keep the source data and mapping so the process can be repeated when records change.

You can query `inventory-data.ttl` below. The supplied {download}`bicycle inventory <../data/bicycle-inventory.ttl>` contains the same record triples and adds the statement that Bicycle is a subclass of Vehicle.

:::{dropdown} Test a mapping on one record (optional)

When developing or adapting a mapping, test it first on B001 using the {ref}`reference RDF <reference-rdf>`.

In a separate folder, save those five triples, including the prefix declarations, as `sample-reference.ttl` using a text editor. Put a copy of the CSV, mapping and `rmlmapper.jar` in that folder. In this CSV copy, keep only the header and B001 row. Open a terminal in that folder and run:

```sh
java -jar rmlmapper.jar -m bicycle-inventory.rml.ttl -o sample-generated.ttl -s turtle
```

Compare `sample-generated.ttl` with `sample-reference.ttl`: check full IRIs, the direction of links, literal values and language tags. For example, `hasMaterial "steel"@en` belongs on F001, the frame. Compare the record triples only, leaving out class and property declarations. Prefixes, formatting and triple order can differ while expressing the same graph. Inspect the sample in Protégé's [individual views](https://protegeproject.github.io/protege/getting-started/#navigation) or the graph views from chapter 4, and correct any differences against the source record.

You can also compare graphs programmatically. For example, Python's [RDFLib graph-comparison utilities](https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.compare/) can check whether two graphs match and identify differing triples.

Once the sample matches, check records with other materials and missing values before applying the adapted mapping to the full dataset. Keep the reference examples with the source data and mapping for later checks.
:::

(query-with-sparql-with-or-without-inferences)=
## Query with SPARQL and test competency questions

(competency-question-tests)=
### Test competency questions against expected answers

Use the {ref}`frame-material query from Chapter 2 <sparql-basics>` on the converted inventory to test the competency question from Chapter 3. Record the question, query, data and ontology versions, inference settings and expected answers together as a repeatable check of the ontology's coverage. {cite}`noy2001ontology,gruninger1995methodology`

Establish the expected answers from the source records before running the query:

| Bicycle | Recorded frame material | Expected in the steel-frame result |
|---|---|---|
| B001 | steel | Yes |
| B002 | aluminium | No |
| B003 | Not recorded | No matching recorded value |

(query-inventory)=
### Load and query the data in Protégé

Use Protégé from Chapter 4 to query the small inventory:

1. Choose **File > Open** and open `inventory-data.ttl` or the supplied `bicycle-inventory.ttl` in a separate Protégé window, keeping the chapter 5 working ontology separate.
2. Enable **Window > Tabs > SPARQL Query** and select the tab. If it is absent from the **Tabs** menu, install **SPARQL Query** through **File > Check for plugins**, restart Protégé and reopen the data file.
3. Paste the {ref}`frame-material query <sparql-basics>` and click **Execute**. It needs no reasoning. [Protégé SPARQL plugin](https://github.com/protegeproject/sparql-query-plugin)

**SPARQL Query** is the SPARQL editor; **DL Query** uses the Manchester expressions introduced in chapter 5.

The result table below the editor should contain only `https://example.org/bike/id/B001`. Compare the returned identifiers with the expected set, checking both missing and unexpected answers. Result order does not matter for this query.

If B001 is missing, inspect the loaded graph, full IRIs, component link and exact material literal, including its language tag. B002 and B003 have no matching steel-frame statements in this graph; B003's frame material remains unknown. These absences do not establish that the bicycles have no steel frames.

Repeat the comparison after relevant changes, and record the reason for any change to the expected answers.

You can also use SPARQL to generate Mermaid diagram text from selected relationships in your data, as described in {ref}`Visualise your ontology <visualise-ontology>`.

(load-and-query-the-data-in-a-triple-store)=
:::{dropdown} Query in a triple store (optional)

To query the inventory in a {ref}`triple store introduced in Chapter 2 <triple-stores>`, obtain your team's dataset and query-editor addresses. For a local installation, follow the setup instructions linked there first.

1. Select or create a dataset in a triple store available to your team.
2. Load or index `inventory-data.ttl` or the supplied `bicycle-inventory.ttl` so its statements are available in the dataset's *default graph*, which the query searches.
3. Open the SPARQL query editor, paste the {ref}`frame-material query <sparql-basics>` and run it.
:::

(query-inferences)=
### Querying inferred information

For Protégé, open the supplied `bicycle-inventory.ttl`, start HermiT and {ref}`export the inferred class assertions <export-inferred-assertions>`. Open the export in a separate window and use **SPARQL Query** there. The export records HermiT's conclusions as assertions for this tab; starting the reasoner alone leaves the tab querying the asserted statements.

For example, with Bicycle declared a subclass of Vehicle, RDFS reasoning lets `?bicycle a def:Vehicle` retrieve B001 from its Bicycle membership. The frame-material query matches the recorded statements directly. [SPARQL entailment regimes](https://www.w3.org/TR/sparql11-entailment/)

In a triple store, load the relevant ontology axioms and enable reasoning supported by the store, or load previously inferred statements. Using ontology term IRIs in the data does not load the axioms. Check which RDFS or OWL features the store supports. [RDF4J configuration](https://rdf4j.org/documentation/programming/repository/), [Jena inference support](https://jena.apache.org/documentation/inference/)

:::{dropdown} Test inferred answers (optional)

For the vehicle-classification question from Chapter 3, use the same inventory and run:

```sparql
PREFIX def: <https://example.org/bike/def/>

SELECT DISTINCT ?item
WHERE {
    ?item a def:Vehicle .
}
```

On the supplied inventory, this query gives no results: it contains no explicit Vehicle memberships. Follow the instructions to {ref}`export the inferred class assertions and open the export in Protégé <query-inferences>`, then run the query again. B001, B002 and B003 should now match through the Bicycle-to-Vehicle subclass statement. Compare their full IRIs with the result. A triple store with RDFS inference enabled can produce the same answers. Keep the inference or export settings with the test. [SPARQL entailment regimes](https://www.w3.org/TR/sparql11-entailment/)
:::

(shacl-validation)=
## Apply SHACL checks

### Agree the requirements

Extend the {ref}`material check from Chapter 2 <shacl-basics>` to the three inventory records. The team also wants recorded material names to use language-tagged text, so add a datatype requirement: `rdf:langString`.

This completeness requirement is a choice for this check. F003 can have a material that has not been recorded; the shape will flag the missing recorded value.

### Extend the shape

Download {download}`bicycle-shapes.ttl <../data/bicycle-shapes.ttl>`. It keeps the earlier shape's target, property and minimum count, and adds `sh:datatype`:

```turtle
@prefix def: <https://example.org/bike/def/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix shape: <https://example.org/bike/shape/> .

shape:FrameMaterial a sh:PropertyShape ;
    sh:targetClass def:Frame ;
    sh:path def:hasMaterial ;
    sh:minCount 1 ;
    sh:datatype rdf:langString .
```

The shape now checks F001, F002 and F003. The added `sh:datatype rdf:langString` requires every recorded material value to be language-tagged text. [Datatype constraint](https://www.w3.org/TR/shacl/#DatatypeConstraintComponent)

### Run validation and read the report

For these fictional records, use [SHACL Play!](https://shacl-play.sparna.fr/play/validate) in a browser:

1. Under **Input Data**, choose **Copy/paste RDF content** and paste the entire inventory Turtle file, including its prefixes.
2. Under **Shapes**, choose **Copy/paste SHACL Rules content** and paste the shape above, including its prefixes.
3. Under **Options**, select **Avoid resolving targets** to disable the application's extra coverage checks. Leave the other options unchecked, including OWL-Micro inference.
4. Choose **VALIDATE**.

Expect one violation: the focus node (the resource being checked) is `id:F003`, the property is `def:hasMaterial`, and the constraint is `sh:MinCountConstraintComponent`, corresponding to `sh:minCount`. F003 has no recorded material value; F001 and F002 satisfy both conditions.

Save the report using its **Turtle** download link. The RDF report records `sh:conforms false` and identifies the affected node, property and constraint. Keep it with the data and shapes used for the check. [Validation reports](https://www.w3.org/TR/shacl/#validation-report)

(ontology-shacl-check)=
### Check an ontology requirement

Apply the same method to a documentation requirement: for this check, the Bicycle class must have a label. Use the {download}`expanded bicycle ontology <../data/bicycle-ontology.ttl>` as **Input Data** and replace the shapes with:

```turtle
@prefix def: <https://example.org/bike/def/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix shape: <https://example.org/bike/shape/> .

shape:BicycleLabel a sh:PropertyShape ;
    sh:targetNode def:Bicycle ;
    sh:path rdfs:label ;
    sh:minCount 1 .
```

`sh:targetNode` selects the class resource `def:Bicycle` itself; `sh:path` now identifies its label property. [Node targets](https://www.w3.org/TR/shacl/#targetNode)

Keep the same options and validate. The supplied ontology conforms because Bicycle has labels. Removing both its labels from a copy produces one minimum-count violation, with focus node `def:Bicycle` and property `rdfs:label`. Review the label wording with domain experts as well as checking its presence.

## Review findings and repeat the checks

For the inventory, F003's finding identifies a gap in the source information that the conversion correctly preserved. Obtain the material from an appropriate source if possible, and record where it came from. If missing material is acceptable for the intended use, remove `sh:minCount 1` from a copy of `bicycle-shapes.ttl` and rerun validation on the inventory RDF. It then conforms to the remaining datatype condition. Document why that requirement changed.

Replacing F001's `"steel"@en` with `"aluminium"@en` would satisfy both material conditions for that frame while disagreeing with our source record. The {ref}`source comparison above <rdf-conversion-checks>` and expected steel-frame answer would expose that difference. Use the findings to locate the cause in the model, source data, mapping, query or validation requirements before making changes.

Retain the source data, mapping where used, ontology, queries, expected answers, shapes and reports with their versions or dates. After a revision, repeat the affected checks on the earlier examples as well as any new records. Recheck logical consistency and intended inferences when changing OWL axioms.
