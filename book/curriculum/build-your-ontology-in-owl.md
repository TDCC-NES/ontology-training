# Build your ontology in OWL

We will describe B001 and its frame F001 in OWL, using the classes and properties from our sketch. We will record that the frame is made of steel and run a reasoner to infer that B001 is a Vehicle.

You can write Turtle directly in a text editor or use [Protégé](https://protege.stanford.edu/) or another ontology editor. You can also use AI assistance to draft and revise the ontology.

The walkthrough below uses Protégé as one example. If you prefer a text editor, use the {ref}`Turtle example at the end of this chapter <owl-turtle-example>` as a reference.

## Get started with Protégé desktop

For the Protégé walkthrough, open [Protégé desktop](https://protege.stanford.edu/). If you need to install it, follow the [installation instructions](https://protegeproject.github.io/protege/installation/). The steps use Protégé 5 and its bundled HermiT reasoner.

## Create an ontology: ontology IRI, term IRIs and prefixes

Choose **File > New** to create an empty ontology. If prompted, open it in a new window.

Open the **Active ontology** tab. If a tab is missing, enable it through **Window > Tabs**. [Protégé interface](https://protegeproject.github.io/protege/views/)

In **Ontology header**, replace the value in **Ontology IRI** with `https://example.org/bike`, then click outside the field. Leave **Ontology Version IRI** empty. [Setting the ontology IRI](https://protegeproject.github.io/protege/views/ontology-header/)

This is the ontology IRI agreed in our design. A class such as Bicycle has its own IRI, `https://example.org/bike/def/Bicycle`; an individual such as B001 uses `https://example.org/bike/id/B001`.

In **Active ontology**, open **Ontology Prefixes** and use **+** beside **Prefixes**. Enter `def:` under **Prefix name** and `https://example.org/bike/def/` under **Prefix**, then confirm. Add `id:` in the same way, using its mapping below. Check the standard prefixes against the table and add any that are missing.

| Prefix name | Prefix |
|---|---|
| `def:` | `https://example.org/bike/def/` |
| `id:` | `https://example.org/bike/id/` |
| `owl:` | `http://www.w3.org/2002/07/owl#` |
| `rdf:` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| `rdfs:` | `http://www.w3.org/2000/01/rdf-schema#` |

Choose **View > Render by prefixed name** to display names such as `def:Bicycle` and `id:B001`. These are the names used in the creation dialogs below.

When a creation dialog asks for a **Name**, enter the prefixed name, such as `def:Bicycle`. Protégé expands the prefix using the mapping you added. Check the IRI shown in the dialog before confirming: `def:Bicycle` should produce exactly `https://example.org/bike/def/Bicycle`. Use `def:` for classes and properties and `id:` for individuals.

## Add classes and subclass relationships

Open **Entities** and select **Classes**. Keep the class hierarchy in **Asserted** mode while editing. *Asserted* statements are those we record explicitly.

The hierarchy starts with `owl:Thing`, the built-in class containing every individual. Hover over the buttons above the hierarchy to find **Add subclass**. For each row below, select the parent, use **Add subclass**, enter the new class's prefixed name and confirm. [Creating classes](https://protegeproject.github.io/protege/views/class-hierarchy/)

| Select this parent | Create this class |
|---|---|
| `owl:Thing` | `def:Vehicle` |
| `def:Vehicle` | `def:Bicycle` |
| `owl:Thing` | `def:Component` |
| `def:Component` | `def:Frame` |

Select `def:Bicycle` and check **SubClass Of** in its description: it should contain `def:Vehicle`. For `def:Frame`, it should contain `def:Component`.

## Add individuals and class memberships

Open **Individuals by class** and select `def:Bicycle` in the class hierarchy. The individuals list shows members of that class. Use **Add Individual**, enter `id:B001` as the name and confirm. This creates B001 and records its membership in Bicycle. [Creating individuals](https://protegeproject.github.io/protege/views/instances/)

Select `def:Frame` and use the same procedure to create `id:F001` as a Frame.

Check the **Types** section for each individual: B001 should list `def:Bicycle`, and F001 should list `def:Frame`.

## Add object and datatype properties: domains, ranges and values

### Create the object property

In **Entities**, select **Object properties**. Select the built-in root `owl:topObjectProperty` and use **Add sub property** to create `def:hasComponent`.

With `def:hasComponent` selected, use **+** beside **Domains (intersection)** in its description. In the dialog, open **Class hierarchy**, select `owl:Thing` and choose **OK**. To set the range, use **+** beside **Ranges (intersection)**. In **Class hierarchy**, expand `owl:Thing` if needed, select `def:Component` and choose **OK**.

The domain `owl:Thing` includes all individuals, so it also covers objects other than bicycles. With Component as the range, a reasoner can infer from “B001 has component F001” that F001 is a Component. We record B001's Bicycle membership separately. [Property domains and ranges](https://protegeproject.github.io/protege/views/object-property-description/)

### Create the datatype property

Protégé calls datatype properties **Data properties**. Open that section in **Entities**, select `owl:topDataProperty` and use **Add sub property** to create `def:hasMaterial`.

In its description, use **+** beside **Domains (intersection)**, select `owl:Thing` in **Class hierarchy** and choose **OK**. Use **+** beside **Ranges**, open **Built in datatypes**, select `rdf:langString` and choose **OK**.

The range `rdf:langString` is the datatype for language-tagged text. The domain `owl:Thing` includes all individuals, including bicycles and frames. If we used Bicycle as the domain of `hasMaterial`, a reasoner would also classify F001 as a Bicycle when we record its material. [RDF literals](https://www.w3.org/TR/rdf11-concepts/#section-Graph-Literal)

### Enter relationships and values

Return to **Individuals by class**. Select `def:Bicycle` in the class hierarchy, then `id:B001` in the individuals list. Use **+** beside **Object property assertions**. Enter `def:hasComponent` as the property and `id:F001` as the individual, then confirm. This records the link from the bicycle to its frame.

Select `def:Frame` in the class hierarchy, then `id:F001` in the individuals list. Use **+** beside **Data property assertions** and select `def:hasMaterial` in the **Data Property** panel. Enter `steel` under **Value** and `en` under **Language Tag**, then confirm. Enter the text without Turtle quotation marks; the editor supplies the literal syntax when saving. [Property assertions](https://protegewiki.stanford.edu/wiki/Pr4_UG_rv_In_Prop_assertions)

Protégé records this as `"steel"@en`: the name is English and describes F001's material, which we want to compare across inventories.

(owl-entity-annotations)=
## Add labels, definitions and language tags

Add the labels and definitions agreed during conceptual modelling as *annotations* on the classes and properties. Use the annotation property `rdfs:label` for labels and `rdfs:comment` for definitions. {cite}`w3c2012owl2primer`

| Term | English label | English definition |
|---|---|---|
| `def:Bicycle` | bicycle | A vehicle with two wheels, designed to be propelled by pedalling, with or without electric assistance. |
| `def:hasComponent` | has component | Relates an object to one of its physical parts. |

For Bicycle:

1. Open **Entities > Classes**, select `def:Bicycle` and use **+** in its **Annotations** panel.
2. Choose `rdfs:label` as the annotation property and the **Literal** tab for its value.
3. Enter `bicycle` under **Value** and `en` under **Language Tag**, then confirm.
4. Add another annotation using `rdfs:comment`. Copy the Bicycle definition from the table and set its language tag to `en`.

The label appears as `"bicycle"@en` in Turtle. [Adding annotations](https://protegeproject.github.io/protege/views/annotations/)

Open **Entities > Object properties**, select `def:hasComponent` and add its label and definition in the same way.

Return to **Entities > Classes**, select `def:Bicycle` and add another `rdfs:label` with text `fiets` and language tag `nl`. Both labels describe the same class, with the same IRI.

Use language tags for natural-language text throughout the ontology. Our English material name, labels and definitions use `en`; the Dutch label uses `nl`.

## Run the reasoner and inspect inferred class memberships

Choose **Reasoner > HermiT**, then **Reasoner > Start reasoner**. Wait for reasoning to finish. HermiT checks whether the statements contradict one another and infers class memberships from them. After editing the ontology, use **Reasoner > Synchronize reasoner** to refresh its results. [Starting a reasoner](https://protegeproject.github.io/protege/getting-started/#reasoning)

In **Individuals by class**, select `def:Bicycle` and then `id:B001` in the individuals list. Its **Types** section lists `def:Bicycle`, its most specific class. To find all members of the broader class `def:Vehicle`, use **DL Query**. [Inferred types in Protégé](https://protegeproject.github.io/protege/views/individual-description/)

1. Open **DL Query**. If the tab is missing, enable it through **Window > Tabs > DL Query**.
2. Enter `def:Vehicle` in the query field, using the same prefixed name shown in Protégé.
3. Select **Instances** in the query options and choose **Execute**.

The results should include `id:B001`: we recorded it as a Bicycle, and Bicycle is a subclass of Vehicle. The reasoner therefore infers that B001 is also a Vehicle. [DL Query documentation](https://protegewiki.stanford.edu/wiki/DLQueryTab)

(owl-turtle-example)=
## Save and inspect the ontology in Turtle

Choose **File > Save as**. In the format dialog, select **Turtle Syntax** and choose **OK**. Choose a folder, name the file `bike-working.ttl` and choose **Save**. Use **File > Save** regularly as you make changes. Saving the file leaves the ontology IRI as `https://example.org/bike`.

Open the saved file in a text editor. The ontology itself is declared with `owl:Ontology`. The `owl:Class`, `owl:ObjectProperty` and `owl:DatatypeProperty` declarations identify the classes and properties you created. For B001, `owl:NamedIndividual` declares an individual with an IRI, and `def:Bicycle` records its Bicycle membership.

A comma groups objects with the same subject and predicate, as in `id:B001 a owl:NamedIndividual, def:Bicycle`. [Turtle object lists](https://www.w3.org/TR/turtle/#object-lists)

The ontology in Turtle:

```turtle
@prefix def: <https://example.org/bike/def/> .
@prefix id: <https://example.org/bike/id/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

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
    rdfs:comment "Relates an object to one of its physical parts."@en ;
    rdfs:domain owl:Thing ;
    rdfs:range def:Component .

def:hasMaterial a owl:DatatypeProperty ;
    rdfs:domain owl:Thing ;
    rdfs:range rdf:langString .

id:B001 a owl:NamedIndividual, def:Bicycle ;
    def:hasComponent id:F001 .

id:F001 a owl:NamedIndividual, def:Frame ;
    def:hasMaterial "steel"@en .
```

Protégé may use a different order or add declarations. Compare the full IRIs and statements with the example. **File > Save** stores the statements you entered, including B001's Bicycle membership. After reopening the file, the reasoner can infer its Vehicle membership again. [Saving and exporting inferences](https://protegeproject.github.io/protege/menus/)

You can reopen `bike-working.ttl` through **File > Open** to inspect the same model in Protégé. The {download}`expanded bicycle ontology <../data/bike-ontology.ttl>` provides the other inventory records, properties and annotations. It also includes additional bicycle types, components and publication metadata.
