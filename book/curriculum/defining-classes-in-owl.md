(owl-defining-classes)=
# Defining classes

We use class expressions to state conditions and define classes that a reasoner can recognise from the recorded facts.

For the Protégé steps, open `bike-working.ttl` from the preceding chapter and use **File > Save as** to save a Turtle copy as `bike-logical.ttl`. Keep the prefixed-name display.

(owl-axioms)=
## Axioms, expressions and restrictions

Our model already contains a subclass statement and B001's class membership:

```turtle
def:Bicycle rdfs:subClassOf def:Vehicle .
id:B001 a def:Bicycle .
```

These are *axioms*: statements the ontology asserts to hold. [OWL building blocks](https://www.w3.org/TR/owl2-primer/#Modeling_Knowledge:_Basic_Notions)

We use the prefixes from the {ref}`previous Turtle example <owl-turtle-example>`. For readable expressions, we also use *Manchester syntax*, the notation used in Protégé's class descriptions and DL Query:

```text
def:hasComponent some def:Frame
```

Read this as “has at least one component that is a Frame”. `some` is a keyword; the property and class use our existing IRIs. Parentheses group expressions. The cheat sheet provides the corresponding Turtle patterns and links to the specification's construct names. [Manchester syntax](https://www.w3.org/TR/owl2-manchester-syntax/)

An *expression* describes a class, property or range of data values. `def:Frame` is a simple class expression. The expression above is a *restriction*: it describes individuals through a property. An axiom can use that expression to describe or define a class.

(owl-class-expressions)=
## Combining and separating classes

Class expressions combine conditions with `and`, `or` and `not`. For these examples, Wheel groups wheel components, CargoBicycle describes bicycles designed to carry extra loads, and Fatbike describes bicycles with unusually wide tyres.

| Manchester expression | Meaning |
|---|---|
| `def:CargoBicycle and def:Fatbike` | Individuals in both classes; an intersection |
| `def:Frame or def:Wheel` | Individuals in either class or both; an inclusive union |
| `def:Bicycle and not def:CargoBicycle` | Bicycles outside CargoBicycle; uses a complement |

Membership in a union need not establish which alternative holds. A complement expresses non-membership: absence of CargoBicycle membership alone does not establish `not CargoBicycle`.

Classes may overlap: a bicycle can be both a CargoBicycle and a Fatbike. Use *disjointness* when shared membership would contradict the model:

```turtle
def:Frame owl:disjointWith def:Wheel .
```

No individual can then be both a Frame and a Wheel. [Class axioms](https://www.w3.org/TR/owl2-syntax/#Class_Expression_Axioms)

(owl-object-restrictions)=
## Describing relationships with restrictions

An object-property restriction describes individuals through their related individuals, called *fillers*.

| Manchester expression | What it says about a member |
|---|---|
| `def:hasComponent some def:Frame` | It has at least one Frame component |
| `def:hasComponent only def:Frame` | Every component it has is a Frame |
| `def:hasComponent value id:F001` | It has the particular component F001 |

`only` restricts all fillers, including any not yet recorded. It also holds for an individual with no fillers. To require at least one Frame and allow only Frames, combine both:

```text
(def:hasComponent some def:Frame) and (def:hasComponent only def:Frame)
```

Using `hasComponent only Frame` for B001 would require its wheels and cargo box to be Frames too. A dedicated `def:hasFrame` property can express conditions about its frames alone. [Object restrictions](https://www.w3.org/TR/owl2-syntax/#Object_Property_Restrictions)

Data-property restrictions describe individuals through their data values. For example, `def:hasMaterial value "steel"@en` describes individuals with that recorded material value.

(owl-conditions)=
## Necessary and sufficient conditions

Introduce `def:SteelFrame` for Frames with the recorded material value `"steel"@en`. Following the {ref}`iterative workflow <ontology-development-workflow>`, we choose an axiom that expresses the agreed meaning and check its consequences on the example records.

Use `SubClassOf` to state necessary conditions. In **Entities > Classes**, keep **Asserted** mode, select `owl:Thing` and create `def:SteelFrame`. With it selected, use **+** beside **SubClass Of** and choose **Class expression editor**. Enter only the expression after `SubClassOf:` below, then confirm. [Editing class descriptions](https://protegeproject.github.io/protege/views/class-description/)

```text
Class: def:SteelFrame
    SubClassOf: def:Frame and (def:hasMaterial value "steel"@en)
```

Every SteelFrame must be a Frame and have this material value. These are *necessary conditions*: asserting that F001 is a SteelFrame lets the reasoner infer both facts. Having those facts alone does not establish SteelFrame membership from this axiom.

Start HermiT, or synchronise it if already running. In **DL Query**, enter `def:SteelFrame`, select **Instances** and **Execute**: F001 should not appear.

If being a Frame with that recorded material value is also sufficient for SteelFrame membership, use `EquivalentTo`. Remove the expression from **SubClass Of** and add it under **Equivalent To**, again using **Class expression editor**. The reasoner can then recognise matching frames:

```text
Class: def:SteelFrame
    EquivalentTo: def:Frame and (def:hasMaterial value "steel"@en)
```

This works in both directions. Every SteelFrame satisfies the expression, and every individual satisfying it is a SteelFrame. Together, the conditions are *necessary and sufficient*. The {ref}`cheat sheet <owl-steelframe-turtle>` shows the same definition in Turtle.

Synchronise HermiT and repeat the query: F001 should now appear.

Create `def:BicycleWithSteelFrame` under `owl:Thing`. Under **Equivalent To**, enter only the expression after `EquivalentTo:` below:

```text
Class: def:BicycleWithSteelFrame
    EquivalentTo: def:Bicycle and (def:hasComponent some def:SteelFrame)
```

A BicycleWithSteelFrame is a Bicycle with at least one SteelFrame component. F001 is a Frame with material `"steel"@en`, so the reasoner classifies it as a SteelFrame. B001 is a Bicycle with F001 as a component, so it is a BicycleWithSteelFrame.

Synchronise HermiT and query `def:BicycleWithSteelFrame` with **Instances** selected: B001 should appear. Save `bike-logical.ttl`.

To inspect all three inventory records, open the {download}`completed reasoning example <../data/owl2-reasoning.ttl>` through **File > Open** in a new window. Run HermiT and query `def:BicycleWithSteelFrame`: B001 should appear. Query `def:Bicycle and not def:BicycleWithSteelFrame`: no instances should appear.

B002 has Frame component F002 with the value `"aluminium"@en`; B003 has Frame component F003 with no material recorded. Neither frame is inferred to be a SteelFrame, and neither is inferred to be outside that class. B002 and B003 likewise remain unclassified as BicycleWithSteelFrame: other material values or frames remain possible.

`some` requires a relationship to exist, even if its filler is unnamed. Asserting that B003 has some SteelFrame does not identify F003 as that frame; another frame could satisfy the condition.

This definition matches recorded wording: `"Steel"@en` and `"steel"@nl` are different values from `"steel"@en`.

(owl-cardinality)=
## Cardinality

*Cardinality* counts distinct fillers. A *qualified* cardinality counts only fillers in a specified class:

| Manchester expression | Meaning |
|---|---|
| `def:hasComponent min 2 def:Wheel` | At least two distinct Wheel components |
| `def:hasComponent max 2 def:Wheel` | At most two distinct Wheel components |
| `def:hasComponent exactly 2 def:Wheel` | Both the minimum and maximum conditions |

These can describe an assembled study bicycle in its observation context. An *unqualified* restriction, such as `def:hasComponent exactly 2`, counts all components, including its frame and cargo box.

For B001's wheels W001 and W002, the two names establish a minimum of two only when their difference is known, for example with `id:W001 owl:differentFrom id:W002`. A minimum can also require further, unnamed wheels. Conversely, a maximum of one Frame makes two Frame fillers identical; asserting that they differ creates a contradiction. [Cardinality restrictions](https://www.w3.org/TR/owl2-syntax/#Object_Property_Cardinality_Restrictions)

(owl-restriction-demonstrations)=
For each demonstration, reopen `bike-logical.ttl` and save a separate Turtle copy. Start HermiT, then synchronise after each change; use **DL Query > Instances** for queries. Return to `bike-logical.ttl` afterwards.

:::{dropdown} In Protégé: what only infers (optional)

Restrict B001's hasFrame links to members of Frame.

1. Create the object property `def:hasFrame`, leaving its domain and range unset. In **Individuals by class**, select B001 and use **+** beside **Types**, then **Class expression editor**, to add `def:hasFrame only def:Frame`.
2. Query `def:hasFrame some def:Frame`: B001 does not appear. `only` alone establishes no frame's existence.
3. Create `id:F004` under `owl:Thing` and add B001's object property assertion `def:hasFrame id:F004`. Query `def:Frame`: F004 now appears, although we never asserted its Frame membership. The `some` query now includes B001 too.

The restriction supplies F004's classification. It applies to this bicycle's hasFrame links; other components remain unrestricted by it.
:::

:::{dropdown} In Protégé: count distinct wheels and find a contradiction (optional)

1. Create `def:Wheel` under Component, then W001 and W002 as Wheel individuals with the `id:` prefix. Link B001 to both through `def:hasComponent`.
2. Query `def:hasComponent min 2 def:Wheel`: B001 does not appear yet. Select W001 and add W002 under **Different Individuals**. Repeat the query: B001 now appears. Two IRIs alone did not establish two distinct wheels.
3. Add `def:hasComponent max 1 def:Wheel` to B001's **Types** using **Class expression editor**. Synchronising now reports an inconsistent ontology: two known-different wheels cannot satisfy this maximum. Remove that last restriction and synchronise to restore consistency.

The two recorded wheels still do not establish `exactly 2`: additional wheels remain possible.
:::
