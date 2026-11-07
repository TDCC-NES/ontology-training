# Build your ontology in OWL

We now turn part of the agreed bicycle design into an OWL ontology. We use one bicycle, B001, and its frame, F001, to create classes and properties, record the frame's material and inspect an inferred class membership. A single file holds the model and these example individuals.

You can build the ontology by writing Turtle directly in a text editor, using [Protégé](https://protege.stanford.edu/), or working in another ontology tool. Choose the approach that suits your work. AI assistance is also a valid option for drafting and revising the ontology with any of these approaches.

The walkthrough below uses Protégé as one example. If you prefer a text editor, use the {ref}`Turtle example at the end of this chapter <owl-turtle-example>` as a reference.

## Get started with Protégé desktop

To follow the Protégé walkthrough, install [Protégé desktop](https://protege.stanford.edu/) for your operating system, following the [installation instructions](https://protegeproject.github.io/protege/installation/), and open the application. The steps here use the Protégé 5 desktop interface and its bundled HermiT reasoner.

Protégé organises editing into tabs containing smaller panels, called *views*. We will use:

| Tab | What we use it for |
|---|---|
| Active ontology | Set the ontology IRI and prefixes |
| Entities | Create and describe classes and properties |
| Individuals by class | Create B001 and F001 and enter their relationship and material value |

If a tab is missing, enable it through **Window > Tabs**. In a view, hover over a toolbar button to see its name; a **+** beside a section heading adds a statement to that section. [Protégé interface](https://protegeproject.github.io/protege/views/)

Choose **View > Render by prefixed name** to display names such as `def:Bicycle` and `id:B001`, matching the examples below.

## Create an ontology: ontology IRI, term IRIs and prefixes

Choose **File > New** to create an empty ontology. If asked where to open it, choose a new window. Choose **Refactor > Change ontology IRI**, enter `https://example.org/bike` as the ontology IRI and confirm. Leave the version IRI unset. The **Active ontology** tab shows the resulting identifier in its **Ontology header** view. [Ontology IRI](https://protegeproject.github.io/protege/views/ontology-header/)

This is the ontology IRI agreed in our design. A class such as Bicycle has its own IRI, `https://example.org/bike/def/Bicycle`; an individual such as B001 uses `https://example.org/bike/id/B001`.

In **Active ontology**, open **Ontology Prefixes**. In its **Prefixes** section, use **+** to add `def:` and `id:`. The prefix editor calls the two fields **Prefix name** and **Prefix**: enter `def:` in the first and `https://example.org/bike/def/` in the second, then confirm. Repeat for `id:`. Keep the standard mappings shown below, adding any that are missing.

| Prefix name | Prefix |
|---|---|
| `def:` | `https://example.org/bike/def/` |
| `id:` | `https://example.org/bike/id/` |
| `owl:` | `http://www.w3.org/2002/07/owl#` |
| `rdfs:` | `http://www.w3.org/2000/01/rdf-schema#` |
| `xsd:` | `http://www.w3.org/2001/XMLSchema#` |

When a creation dialog asks for a **Name**, enter the prefixed name, such as `def:Bicycle`. Protégé expands a registered prefix to produce the full IRI. Check the IRI shown in the dialog before confirming: `def:Bicycle` should produce exactly `https://example.org/bike/def/Bicycle`. We will use `def:` for classes and properties and `id:` for individuals.

## Add classes and subclass relationships

Open **Entities** and select **Classes**. Keep the class hierarchy in **Asserted** mode while editing. *Asserted* statements are those we record explicitly.

The hierarchy starts with `owl:Thing`, the built-in class containing every individual. For each row below, select the parent, use **Add subclass**, enter the new class's prefixed name and confirm. [Creating classes](https://protegeproject.github.io/protege/views/class-hierarchy/)

| Select this parent | Create this class |
|---|---|
| `owl:Thing` | `def:Vehicle` |
| `def:Vehicle` | `def:Bicycle` |
| `owl:Thing` | `def:Component` |
| `def:Component` | `def:Frame` |

Select `def:Bicycle` and inspect **SubClass Of** in its description: it should contain `def:Vehicle`. The four classes preserve the relationships in our sketch and provide the classes needed for the property domain and range below.

## Add individuals and class memberships

Open **Individuals by class**. Select `def:Bicycle` in the class hierarchy and use **Add Individual** in the **Instances** view. Enter `id:B001` as the name and confirm. This creates B001 and records its membership in Bicycle. [Creating individuals](https://protegeproject.github.io/protege/views/instances/)

Select `def:Frame` and use the same procedure to create `id:F001` as a Frame.

Selecting B001 should show `def:Bicycle` in the **Types** section of its description; F001 should show `def:Frame`. At this point, the individuals have class memberships. We add their relationships and values next.

## Add object and datatype properties: domains, ranges and values

### Create the object property

In **Entities**, select **Object properties**. Select the built-in root `owl:topObjectProperty` and use **Add sub property** to create `def:hasComponent`.

With `def:hasComponent` selected, use **+** beside **Domains (Intersection)** in its description to add `def:Bicycle`. Use **+** beside **Ranges (Intersection)** to add `def:Component`.

These statements implement the domain and range from our design. A reasoner can classify the subject of a `hasComponent` statement as a Bicycle and its object as a Component. For example, `B001 hasComponent F001` supports those memberships. [Property domains and ranges](https://protegeproject.github.io/protege/views/object-property-description/)

### Create the datatype property

Protégé calls datatype properties **Data properties**. Open that section in **Entities**, select `owl:topDataProperty` and use **Add sub property** to create `def:hasMaterial`.

In its description, use **+** beside **Domains (Intersection)** to add `owl:Thing`. Use **+** beside **Ranges**, open **Built in datatypes**, select `xsd:string` and confirm.

Here, `xsd:string` is the datatype for text. The broad domain `owl:Thing` lets us use `hasMaterial` to describe both vehicles and components. A Bicycle domain on `hasMaterial` would also classify a frame with a material value as a Bicycle.

### Enter relationships and values

Return to **Individuals by class** and select `id:B001`. In **Property assertions**, use **+** beside **Object property assertions**. Enter `def:hasComponent` as the property and `id:F001` as the individual, then confirm. This records the link from the bicycle to its frame.

Select `id:F001`. Use **+** beside **Data property assertions** and select `def:hasMaterial` in the **Data Property** panel. Enter `steel` under **Value**, leave **Language Tag** empty and choose `xsd:string` under **Datatype**, then confirm. Enter the text without Turtle quotation marks; the editor supplies the literal syntax when saving. [Property assertions](https://protegewiki.stanford.edu/wiki/Pr4_UG_rv_In_Prop_assertions)

We have now recorded that B001 has component F001 and that F001 has material “steel”. The material describes the frame we want to compare across inventories.

## Add labels, definitions and language tags

Carry over the wording agreed during conceptual modelling. In our example, `rdfs:label` holds a label and `rdfs:comment` holds a textual definition. Both are *annotation properties*, which attach descriptive information to ontology terms. {cite}`w3c2012owl2primer`

For Bicycle:

1. Select `def:Bicycle` and use **+** in its **Annotations** view.
2. Choose `rdfs:label` as the annotation property and the **Literal** tab for its value.
3. Enter `bicycle` under **Value** and `en` under **Language Tag**, then confirm.
4. Add another annotation using `rdfs:comment`, with the definition below and language tag `en`.

Enter the text and language tag in their separate fields. Protégé will write the label as `"bicycle"@en` in Turtle. [Adding annotations](https://protegeproject.github.io/protege/views/annotations/)

Use the same procedure for `hasComponent`. The table gives the wording for both terms:

| Term | English label | English definition |
|---|---|---|
| `def:Bicycle` | bicycle | A vehicle with two wheels, designed to be propelled by pedalling, with or without electric assistance. |
| `def:hasComponent` | has component | Relates a bicycle to a physical part of that bicycle. |

For Bicycle, also add an `rdfs:label` with text `fiets` and language tag `nl`. Both labels describe the same class, with the same IRI.

Keep the recorded material value as an `xsd:string` literal. The language tags here belong to the labels and definitions we are providing in English and Dutch.

## Run the reasoner and inspect inferred class memberships

Choose **Reasoner > HermiT**, then **Reasoner > Start reasoner**. Wait for reasoning to finish. HermiT checks logical consistency and computes memberships implied by the recorded statements. After editing the ontology, use **Reasoner > Synchronize reasoner** to refresh its results. [Starting a reasoner](https://protegeproject.github.io/protege/getting-started/#reasoning)

The **Types** section for an individual focuses on its most specific class memberships. To inspect broader memberships, such as B001 belonging to Vehicle, use **DL Query**. [Inferred types in Protégé](https://protegeproject.github.io/protege/views/individual-description/)

This tab lists individuals belonging to a class, including those reached through subclass relationships:

1. Open **DL Query**. If the tab is missing, enable it through **Window > Tabs > DL Query**.
2. Enter `def:Vehicle` as the class expression. With prefixed-name rendering, this is the name used for the Vehicle class.
3. Select **Individuals** in the query options and choose **Execute**.

The result should include `id:B001`. We recorded B001 as a Bicycle and Bicycle as a subclass of Vehicle, so the reasoner infers that B001 is also a Vehicle. Here, DL Query uses only a class name to retrieve its instances. [DL Query documentation](https://protegewiki.stanford.edu/wiki/DLQueryTab)

(owl-turtle-example)=
## Save and inspect the ontology in Turtle

Choose **File > Save as**, select the Turtle format and save the ontology as `bike-working.ttl`. Use **File > Save** regularly as you make changes. The local filename is the location of this copy; the ontology IRI remains `https://example.org/bike`.

Open the saved file in a text editor. The OWL declarations identify each entity's role: `owl:Class`, `owl:ObjectProperty` and `owl:DatatypeProperty` declare our classes and properties; `owl:NamedIndividual` declares an individual with an IRI. Its additional type, such as `def:Bicycle`, records its class membership. The ontology itself is declared with `owl:Ontology`.

The following compact Turtle brings together the declarations, annotations and statements entered in this walkthrough:

```turtle
@prefix def: <https://example.org/bike/def/> .
@prefix id: <https://example.org/bike/id/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/bike> a owl:Ontology .

def:Vehicle a owl:Class .

def:Bicycle a owl:Class ;
    rdfs:subClassOf def:Vehicle ;
    rdfs:label "bicycle"@en, "fiets"@nl ;
    rdfs:comment "A vehicle with two wheels, designed to be propelled by pedalling, with or without electric assistance."@en .

def:Component a owl:Class .

def:Frame a owl:Class ;
    rdfs:subClassOf def:Component .

def:hasComponent a owl:ObjectProperty ;
    rdfs:label "has component"@en ;
    rdfs:comment "Relates a bicycle to a physical part of that bicycle."@en ;
    rdfs:domain def:Bicycle ;
    rdfs:range def:Component .

def:hasMaterial a owl:DatatypeProperty ;
    rdfs:domain owl:Thing ;
    rdfs:range xsd:string .

id:B001 a owl:NamedIndividual, def:Bicycle ;
    def:hasComponent id:F001 .

id:F001 a owl:NamedIndividual, def:Frame ;
    def:hasMaterial "steel" .
```

Protégé may use a different order, add declarations or write explicit datatypes such as `"steel"^^xsd:string`. Compare the full IRIs and statements with the example. The saved ontology records our assertions; running the reasoner again computes the inferred memberships from them. [Saving and exporting inferences](https://protegeproject.github.io/protege/menus/)

You can reopen `bike-working.ttl` through **File > Open** to inspect the same model in Protégé. The {download}`expanded bicycle ontology <../data/bike-ontology.ttl>` provides the other inventory records, properties and annotations. It also includes additional bicycle types, components and publication metadata.
