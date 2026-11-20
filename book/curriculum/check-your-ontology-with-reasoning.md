(owl-reasoning)=
# Check your ontology with reasoning

Reasoning checks whether the ontology's statements can hold together and identifies consequences to compare with the intended meaning. Open `owl2-reasoning.ttl` with its {ref}`separate inventory data and local catalog <reasoning-example-files>` in a new Protégé window and start HermiT. This file contains the steel-frame definitions and imports the three inventory records. After editing, use **Reasoner > Synchronize reasoner** to update the results.

In chapter 3, we used *model* for our conceptual design. In logic, a *model* is a possible interpretation in which all the ontology's axioms hold together. A statement is *entailed* when it holds in every model. F001 is a SteelFrame in every model. F003 can be a SteelFrame in some models and fall outside that class in others, so its classification remains unresolved. [Direct Semantics](https://www.w3.org/TR/owl2-direct-semantics/)

## Check consistency and class satisfiability

A reasoner can also check consistency: whether at least one model exists. Class satisfiability means that a class can have a member in some model.

For example, if Frame and Wheel are disjoint, `Frame and Wheel` is *unsatisfiable*: it must be empty. The ontology can remain consistent while that class is empty. Asserting an individual in it makes the ontology inconsistent. `owl:Nothing` is the built-in empty class; `owl:Thing` contains every individual.

Ranges can also contribute to a contradiction. This separate fragment uses the course prefixes and the Frame/Wheel disjointness introduced earlier:

```turtle
def:Frame a owl:Class ;
    owl:disjointWith def:Wheel .

def:Wheel a owl:Class .

def:hasFrame a owl:ObjectProperty ;
    rdfs:range def:Frame .

id:B001 a def:Bicycle ;
    def:hasFrame id:W001 .

id:W001 a def:Wheel .
```

The range requires W001 to be a Frame, while its asserted type is Wheel. Since those classes are disjoint, these statements make the ontology inconsistent. If W001 is the bicycle's wheel, correct the mistaken `hasFrame` link to `hasComponent`. Without the disjointness axiom, membership in both classes would be allowed. [Domains and ranges](https://www.w3.org/TR/owl2-primer/#Domain_and_Range_Restrictions)

Resolve inconsistencies before relying on classifications. A reasoner's explanation can identify axioms responsible for an inference or contradiction; researchers determine which statements match the intended meaning. The {ref}`wheel-counting demonstration <owl-restriction-demonstrations>` provides another example of a contradiction.

Once the ontology is consistent, open **Entities > Classes** and switch the hierarchy to **Inferred**. All classes defined in the supplied reasoning example are satisfiable, so none should be grouped with `owl:Nothing`. If a named class appears there in your own ontology, it is unsatisfiable. Select such a class and click **?** beside its inferred equivalence to `owl:Nothing` to inspect the responsible axioms. For classes intended to have members, revise the statements that conflict with the agreed meaning. [Class hierarchy](https://protegeproject.github.io/protege/views/class-hierarchy/), [Unsatisfiable classes in Protégé](https://oboacademy.github.io/obook/tutorial/disjointness/)

## Review and explain inferences

Compare the inferred hierarchy with the intended class relationships. The example's definitions entail that SteelFrame is a subclass of Frame and BicycleWithSteelFrame a subclass of Bicycle. Also review inferred memberships: F001 is a SteelFrame and B001 a BicycleWithSteelFrame. A consistent ontology can still express an unintended meaning, so check these results against the agreed model.

In Protégé, open **Individuals by class**, select Frame and then F001. Beside its inferred **SteelFrame** type, click **?** (**Explain inference**). The explanation should connect F001's Frame membership and material value with the SteelFrame definition. If inferred types are hidden, enable their display in the [reasoner preferences](https://protegeproject.github.io/protege/preferences/reasoner/).

OWL reasoning is *monotonic*: adding axioms preserves earlier entailments. Correcting a mistaken axiom requires removing or replacing it and reasoning again. Reasoner support for the ontology's features and datatypes matters: a timeout or unsupported construct can leave an inference unresolved. [Inference problems](https://www.w3.org/TR/owl2-direct-semantics/#Inference_Problems)

Checks such as “every record must contain a material value” concern data completeness and belong in a validation layer, such as SHACL. Calculations belong in applications or queries.

(export-inferred-assertions)=
## Export inferred assertions (optional)

To use inferred memberships in a query application, run HermiT on the supplied reasoning example, choose **File > Export inferred axioms as ontology** and select class assertions. Load the exported assertions into a triple store or open the export in a separate Protégé window. The SPARQL pattern `?bicycle a def:BicycleWithSteelFrame` can then retrieve B001 when that assertion is included. Starting HermiT alone does not add its conclusions to Protégé's standard **SPARQL Query** tab. [Exporting inferences](https://protegeproject.github.io/protege/menus/)
