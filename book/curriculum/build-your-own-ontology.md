# Build Your Own Ontology

We will use representative bicycle records to define what your ontology needs to describe and how to check its coverage.

In practice, check whether existing ontologies or vocabularies can be reused or extended before building your own. Here, we build a small ontology first to understand the modelling choices involved. {cite}`noy2001ontology`

## Define the purpose and scope

A *use case* describes who will use the ontology, what they want to do with the data and why. This gives you a basis for deciding what the ontology needs to represent. {cite}`suarezfigueroa2009requirements`

For the {ref}`bicycle example <running-example>`, imagine a research team comparing frame materials across several bicycle inventories. They want to find bicycle records with a specified frame material and bring those records together for analysis. A shared model would help them describe the connection between each bicycle, its frame and the recorded material consistently.

Work with representative records throughout development: choose examples that show the characteristics and variation the model should cover. Use them to check whether you can express the relevant information and whether the same terms fit across records.

These fictional inventory records extend the running example:

| Bicycle | Colour | Frame | Frame material |
|---|---|---|---|
| B001 | blue | F001 | steel |
| B002 | red | F002 | aluminium |
| B003 | black | F003 | Not recorded |

“Not recorded” indicates a missing value. The {download}`Turtle file <../data/bicycle-inventory.ttl>` uses the same classes, properties and prefixes as the earlier graph.

The *scope* sets the boundary of the model: the part of the domain it covers and the level of detail needed for the use case. {cite}`suarezfigueroa2009requirements` For this first version, the model could cover bicycles, their frames, the connection between them and recorded frame materials such as “steel”. It also includes the classification of bicycles as vehicles used in our example.

Other components and their materials, detailed alloy composition, material performance, and manufacturing or maintenance histories would fall outside the current scope.

This is enough to describe B001, its frame F001 and the frame's recorded material for the intended comparison. The bicycle's colour is already present in our example data, but it is not needed to select records by frame material. A use case helps you decide which parts of a description matter for a particular task.

Keep the purpose, intended users and scope in a short shared document. Agree these boundaries with the researchers who know the domain and those who will use the data. {cite}`suarezfigueroa2009requirements`

## Starting with competency questions, or not

A *competency question* states something the ontology, together with relevant data, should help answer. Competency questions make the required coverage of the model concrete and provide a basis for evaluating whether it serves its purpose. {cite}`gruninger1995methodology`

They are one way to establish scope. You can begin with a concrete use case, sample records or an initial sketch of the domain, and develop questions as the intended use becomes clearer. Uschold and King describe a project that began by agreeing on important concepts because detailed competency questions were too specific for the early stages. {cite}`uschold1995methodology`

For research aimed at future reuse, you may begin by agreeing which main characteristics and relationships the ontology should cover, while specific research questions are still emerging. {cite}`uschold1995methodology` In the bicycle inventory, this could include colour as well as frame material. Competency questions can then provide examples for checking that coverage.

An initial set of questions can be small. Review and refine it with domain experts as you encounter more data or clarify the research needs, adjusting the scope where needed. {cite}`noy2001ontology`

### Using competency questions

For the frame-material use case, one competency question is:

> Which bicycles have a frame recorded as steel?

To support this question, the model needs to represent bicycles, frames, the connection between them and frame material. The data needs to identify the particular bicycles and frames and record each frame's material. The expected result is a list of bicycle identifiers.

This wording identifies the relevant component. Asking about “bicycles made of steel” would leave it unclear whether the frame, wheels or another part determines the selection. Recording the intended result alongside the question helps make that requirement precise. {cite}`suarezfigueroa2009requirements`

Competency questions can also concern information inferred from the model. For example, “Which recorded objects can be classified as vehicles?” can include objects recorded as bicycles when the ontology states that every Bicycle is a Vehicle. {cite}`gruninger1995methodology,w3c2012owl2primer`

Use representative records to check whether the model supports the questions. These checks can reveal missing data as well as modelling gaps. For F003, recording its material would fill a gap in the data; the model already provides a way to represent it.
