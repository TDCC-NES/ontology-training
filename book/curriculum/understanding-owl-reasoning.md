(owl-reasoning)=
# Interpret inferences and check consistency

For this page, use the {download}`three-record reasoning example (owl2-reasoning.ttl) <../data/owl2-reasoning.ttl>` in Protégé with HermiT running.

## What the reasoner can infer

The class definitions also entail subclass relationships: SteelFrame is a subclass of Frame, and BicycleWithSteelFrame is a subclass of Bicycle.

A *model* is a possible interpretation in which all the ontology's axioms hold together. A statement is *entailed* when it holds in every model. F001 is a SteelFrame in every model. F003 can be a SteelFrame in some models and fall outside that class in others, so its classification remains unresolved. [Direct Semantics](https://www.w3.org/TR/owl2-direct-semantics/)

## Checking and interpreting results

A reasoner can also check consistency: whether at least one model exists. Class satisfiability means that a class can have a member in some model.

For example, if Frame and Wheel are disjoint, `Frame and Wheel` is *unsatisfiable*: it must be empty. The ontology can remain consistent while that class is empty. Asserting an individual in it makes the ontology inconsistent. `owl:Nothing` is the built-in empty class; `owl:Thing` contains every individual.

Resolve inconsistencies before relying on classifications. A reasoner's explanation can identify axioms responsible for an inference or contradiction; researchers determine which statements match the intended meaning.

In Protégé, open **Individuals by class**, select Frame and then F001. Beside its inferred **SteelFrame** type, click **?** (**Explain inference**). The explanation should connect F001's Frame membership and material value with the SteelFrame definition. If inferred types are hidden, enable their display in the [reasoner preferences](https://protegeproject.github.io/protege/preferences/reasoner/). The {ref}`wheel-counting demonstration <owl-restriction-demonstrations>` shows how an added restriction can instead produce a contradiction.

OWL reasoning is *monotonic*: adding axioms preserves earlier entailments. Correcting a mistaken axiom requires removing or replacing it and reasoning again. Choose a reasoner that supports the ontology's features and datatypes; a timeout or unsupported construct can leave an inference unresolved. [Inference problems](https://www.w3.org/TR/owl2-direct-semantics/#Inference_Problems)

Checks such as “every record must contain a material value” concern data completeness and belong in a validation layer, such as SHACL. Calculations belong in applications or queries.
