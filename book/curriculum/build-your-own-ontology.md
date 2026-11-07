# Build Your Own Ontology

In this chapter, we turn the bicycle example into a small ontology design. Starting from a research purpose and a few inventory records, we decide what the model should describe and work towards a shared understanding of its terms. The result is a sketch we can discuss and check against the records, using only pen and paper.

```{admonition} Reuse in practice
:class: note

In practice, check whether existing ontologies or vocabularies can be reused or extended before building your own. Here, we build a small ontology first to understand the modelling choices involved. {cite}`noy2001ontology`
```

## Define the purpose and scope

### Starting from a research purpose

The *purpose* explains why we are developing an ontology. It may come from a task researchers want to carry out, such as comparing data from different studies, or from a broader aim to describe research data consistently for future reuse. Discussing these needs with the people who collect and use the data helps establish what the ontology is for. {cite}`noy2001ontology,suarezfigueroa2009requirements`

A *use case* makes a particular intended use concrete: who will use the ontology, what they want to do with the data and why. It gives us a starting point for deciding what to represent. A detailed use case can develop as the research needs become clearer; a broader purpose and representative records can guide the initial model. {cite}`suarezfigueroa2009requirements,uschold1995methodology`

For the {ref}`bicycle example <running-example>`, imagine a research team comparing frame materials across several bicycle inventories. They want to find bicycle records with a specified frame material and bring those records together for analysis. A shared model would help them describe the relationship between each bicycle and its frame, and record the frame's material consistently.

### Working with representative records

We will work with a few *representative records*: examples chosen to show the characteristics and variation the model should cover. They make modelling decisions concrete. We can check whether the model describes the relevant information in each record and whether the same terms work across records.

These fictional inventory records extend the running example. They include the same frame material as B001, a different material and a missing value, so we can consider each situation as we develop the model:

| Bicycle | Colour | Frame | Frame material |
|---|---|---|---|
| B001 | blue | F001 | steel |
| B002 | red | F002 | aluminium |
| B003 | black | F003 | Not recorded |

“Not recorded” indicates a missing value. The {download}`Turtle file <../data/bicycle-inventory.ttl>` uses the same classes, properties and prefixes as the earlier graph.

### Deciding what to include

The *scope* describes what the model covers and in how much detail. Choosing a scope helps us concentrate on the information needed for the purpose. {cite}`suarezfigueroa2009requirements` For our frame-material comparison, we include bicycles, their frames, the relationship between them and recorded frame materials such as “steel”. We also keep the classification of bicycles as vehicles used in our example.

Other components and their materials, detailed alloy composition, material performance, and manufacturing or maintenance histories are outside this initial scope: we do not need them for the comparison.

This is enough to describe B001, its frame F001 and the frame's recorded material for the intended comparison. The bicycle's colour is already present in our example data, but it is not needed to select records by frame material.

A short shared description of the purpose, intended users and scope helps the researchers who know the domain and those who will use the data agree what to include. It can be revised as new needs emerge. {cite}`suarezfigueroa2009requirements`

## Starting with competency questions, or not

A *competency question* states something the ontology, together with relevant data, should help answer. Writing these questions is one way to make the purpose and scope more precise: each question helps identify what the model needs to represent and provides a way to check its coverage. {cite}`gruninger1995methodology,noy2001ontology`

You can also begin with a use case, representative records or an initial sketch, and develop questions as the intended use becomes clearer. Early modelling can focus on agreeing the important concepts when detailed questions would be too specific. An initial set of questions can be small and grow with discussion. {cite}`uschold1995methodology,noy2001ontology`

For research aimed at future reuse, this means agreeing which main characteristics and relationships to cover while specific research questions are still emerging. {cite}`uschold1995methodology` In the bicycle inventory, this could include colour as well as frame material. Linked Data can also support combinations across research fields that the data's publishers did not anticipate. {cite}`bernerslee2004connectingsciences` Competency questions provide examples for checking coverage; they do not need to anticipate every future use.

### Using competency questions

For the frame-material use case, one competency question is:

> Which bicycles have a frame recorded as steel?

To support this question, the model needs to represent bicycles, frames, the relationship between them and frame material. This makes our earlier scope concrete. The data needs to identify the particular bicycles and frames and record each frame's material. The expected result is a list of bicycle identifiers.

This wording identifies the relevant component. Asking about “bicycles made of steel” would leave it unclear whether the frame, wheels or another part determines the selection. Recording the intended result alongside the question helps make that requirement precise. {cite}`suarezfigueroa2009requirements`

Competency questions can also concern information inferred from the model. For example, “Which recorded objects can be classified as vehicles?” can include objects recorded as bicycles when the ontology states that every Bicycle is a Vehicle. {cite}`gruninger1995methodology,w3c2012owl2primer`

Checking the question against our representative records can reveal missing data as well as modelling gaps. For F003, recording its material would fill a gap in the data; the model already provides a way to represent it.

## Shared conceptualisation and drawing

With an initial scope and representative records, we can develop a *conceptual model*: a description of the kinds of things in the domain, their relationships and the data values we want to record about them. A sketch and short written explanations give people something concrete to discuss and revise. {cite}`uschold1995methodology`

Reaching a shared understanding can take a substantial part of the work in ontology engineering. People who know a domain well may still disagree about what a familiar term includes. {cite}`neuhaus2022consensus`

People who collect and interpret the data, as well as those who will reuse it, bring different examples and explanations to this discussion. These can reveal distinctions that one modeller might overlook. Involving them helps make different research practices and needs explicit. {cite}`hocker2020participatory`

For example, one colleague might use *bicycle* only for vehicles powered entirely by the rider, while another includes electric assistance. Discussing a concrete example helps them agree what belongs in the model's Bicycle class. A possible agreement is to include two-wheeled cycles designed to be pedalled, with or without electric assistance. Keeping the agreed meaning alongside the example makes the decision understandable to others.

A visible sketch helps everyone refer to the same model during discussion. Unresolved points can be noted for a later discussion. {cite}`uschold1995methodology,neuhaus2022consensus`

### Classes, properties and data values

The bicycle records give us concrete things to describe. OWL distinguishes the following elements, which we can already use when sketching the model. {cite}`w3c2012owl2primer`

| Element | What it represents | Example |
|---|---|---|
| Class | A kind of thing | Bicycle, Vehicle or Frame |
| Individual | A particular thing; an instance of a class | B001 is an instance of Bicycle; F001 is an instance of Frame |
| Object property | A property that represents a relationship between individuals | “has component” links B001 to F001 |
| Datatype property | A property that links an individual to a data value | “has material” links F001 to “steel” |
| Data value | Text, a number or another value (a *literal* in RDF) | “blue” and “steel” are text values |

Bicycle is one class used to describe B001, B002 and B003; each identifier names a particular bicycle. Frame is another class, used for F001, F002 and F003. Keeping classes and individuals distinct lets the same model describe many records.

For this use case, “steel” and “aluminium” are values of the “has material” property. Different recorded materials can be described using the same Frame class. A separate class is useful when the model needs to distinguish a kind of thing, rather than simply record a different value. {cite}`noy2001ontology`

A *subclass* is a more specific class. Bicycle is a subclass of Vehicle: every instance of Bicycle is also an instance of Vehicle. A component relationship has a different meaning. F001 is a component of B001; making Frame a subclass of Bicycle would say that every frame is itself a bicycle. {cite}`w3c2012owl2primer`

### Sketch the model

The following sketch combines the model with one record so we can see how its parts are used. We use square-cornered boxes for classes and rounded boxes for individuals. These are drawing conventions for this course; other shapes work too, as long as classes and individuals are clearly distinguishable and the arrows have clear meanings.

1. We begin with the classes Bicycle and Frame. Vehicle sits above Bicycle, with an arrow from Bicycle to Vehicle labelled “subclass of”: every bicycle is a vehicle.
2. An arrow from Bicycle to Frame labelled “has component” summarises the intended relationship between their instances: an individual bicycle can have an individual frame as a component.
3. Inside the class boxes, we list datatype properties and the kinds of values we plan to record: “has colour: text” in Bicycle and “has material: text” in Frame. The frame's material belongs with Frame because it describes that component. We keep “has colour” because it is already recorded and may serve later questions, as discussed above.
4. Below the classes, we add the example individuals B001 and F001. Arrows labelled “type” show class membership, as in the RDF graph. B001 links to F001 through “has component”; their recorded values appear inside their boxes.

```mermaid
---
name: bicycle-conceptual-model
align: center
caption: A conceptual model with the B001 example. Class boxes show the model; rounded boxes show the individuals described by one record.
alt: Vehicle is above its subclass Bicycle. Bicycle lists has colour with text values; Frame lists has material with text values. A has component arrow links Bicycle to Frame. Below, B001 is an instance of Bicycle with colour blue, and F001 is an instance of Frame with material steel. B001 has component F001.
---
%%{init: {"theme": "base", "themeVariables": {"darkMode": false, "background": "#ffffff", "lineColor": "#44546a", "textColor": "#182c3e", "primaryTextColor": "#182c3e", "edgeLabelBackground": "#ffffff"}, "themeCSS": "& { background-color: #ffffff !important; } .edgeLabel, .edgeLabel p { color: #182c3e !important; }"}}%%
block-beta
    columns 4
    Vehicle["Vehicle"] space:3
    space:4
    Bicycle["Bicycle<br/>has colour: text"] space:2 Frame["Frame<br/>has material: text"]
    space:4
    B001(["<b>B001</b><br/>has colour: &quot;blue&quot;"]) space:2 F001(["<b>F001</b><br/>has material: &quot;steel&quot;"])

    Bicycle -- "subclass of" --> Vehicle
    Bicycle -- "has component" --> Frame
    B001 -- "type" --> Bicycle
    F001 -- "type" --> Frame
    B001 -- "has component" --> F001

    classDef resource fill:#edf3fb,stroke:#406b92,color:#182c3e,stroke-width:2px
    classDef instance fill:#e8f4ee,stroke:#36705a,color:#183c2d,stroke-width:2px
    class Vehicle,Bicycle,Frame resource
    class B001,F001 instance
```

### Check the shared sketch against the records

A useful check is to read each arrow as a sentence. For example: “B001 is a Bicycle”, “every Bicycle is a Vehicle” and “B001 has component F001”. We can follow the link to F001 to find the frame's material. This *sentence test* helps check that the arrows express the intended meaning and that the information describes the right thing. It works when reviewing a sketch yourself or discussing it with colleagues.

The same classes and properties should also describe B002 and F002, with their different colour and material values. F003 remains a Frame while its material is unrecorded. Its example box can show the class membership and leave the material value absent.

Comparing two sketches using the same record helps explain the consequences of each choice. For example, writing “has material: steel” inside B001's box would leave the relevant component unspecified. Keeping F001 as a separate individual makes the frame and its material explicit. When a record exposes a missing distinction, we can revise the sketch. {cite}`noy2001ontology` Marking changes in another colour can help others follow the revision.

The agreed sketch is most useful alongside short explanations of its concepts and relationships, the reasons for important choices, and any unresolved points. These notes preserve the reasoning behind the model for the people who will use or change it. {cite}`uschold1995methodology`

## Lexicalisation: labels, definitions and language tags

Clear labels and definitions are essential for other researchers to understand and reuse an ontology. Giving its classes and properties clear wording in natural language is called *lexicalisation*. Develop and refine labels and definitions together with domain experts as part of the shared conceptualisation, alongside the sketch. Drafting, discussing and refining that wording can take a substantial part of ontology development: it makes the agreed meaning explicit and can reveal differences in understanding that still need to be resolved. {cite}`uschold1995methodology,neuhaus2022consensus`

### Choose clear labels and definitions

Choose short, recognisable labels using words familiar to the intended users. Use the same naming conventions throughout the model. Here, class labels are singular nouns such as “bicycle” and “frame”; property labels such as “has component” express how they are used in a statement. {cite}`noy2001ontology`

Write a concise definition for each class and property. A useful class definition starts with a broader kind of thing and states what distinguishes members of the class. Use other, already understood terms to explain the meaning; repeating the label, as in “a bicycle is a type of bicycle”, leaves the reader with the same uncertainty. [Textual definitions](https://obofoundry.org/principles/fp-006-textual-definitions.html)

For a property, explain what it relates or records. For a relationship, make its direction clear. The following definitions describe one class and one property from our sketch:

| Label | Definition |
|---|---|
| bicycle | A vehicle with two wheels, designed to be propelled by pedalling, with or without electric assistance. |
| has component | Relates a bicycle to a physical part of that bicycle. |

The Bicycle definition preserves our agreement about electric assistance. The property definition tells us how to read the link from B001 to F001. Use the sketch and representative records to discuss the wording and agree its meaning together. Where a definition is taken or adapted from an existing source, record that source alongside it.

### Add language tags

Add a *language tag* to each label and textual definition to identify the language of the text. In Turtle, `"bicycle"@en` is an English label and `"fiets"@nl` is a Dutch label. Both can label the same Bicycle class. Applications can use these tags to select text in a user's preferred language. [RDF labels and language tags](https://www.w3.org/TR/rdf-schema/#ch_label)

Choose the languages needed by the intended users. When providing translations, keep the intended meaning consistent across languages.
