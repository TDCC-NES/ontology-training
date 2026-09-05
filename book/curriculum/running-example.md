(running-example)=
# Example: fish

Throughout this training you come back to the same example instead of a new one each chapter: one ontology growing chapter by chapter, rather than starting over every time.

## Where it comes from

The example is adapted from [ShareTrait](https://www.sharetrait.org), an open, FAIR database of *ectotherm* trait data (fish, reptiles, amphibians, and other invertebrates) {cite}`leiva2025sharetrait,martorelli2025sharetraitdb`. Where ShareTrait's SQL database can answer "which traits were measured for this species?", an ontology adds meaning on top: results generalise across the tree of life, connect automatically to related data such as taxonomy or location, and a reasoner can catch problems such as inconsistent units.

## The hero record

Rather than many species and measurements at once, this training follows one individual and one measurement of it: a juvenile **Spangled Perch** (*Leiopotherapon unicolor*, individual `TRAIND023773` in ShareTrait), a freshwater fish common in Australia, and its standard metabolic rate, recorded as part of a study on how nitrate and low pH affect fish {cite}`gomezisaza2020nitrate`.

```{figure} ../figures/spangled-perch-gschmida.jpg
:name: spangled-perch-photo
:class: dark-light
:width: 45%
:alt: A Spangled Perch (Leiopotherapon unicolor) resting near rocks.
:author: Gunther Schmida
:license: CC BY-NC-SA 3.0
:source: [Fishes of Australia](https://fishesofaustralia.net.au/home/species/694)
:placement: caption

Spangled Perch (*Leiopotherapon unicolor*)
```

| Field | Value |
|---|---|
| Individual ID | `TRAIND023773` |
| Measurement ID | `TRAMEA023773` |
| Species | *Leiopotherapon unicolor* (spangled perch) |
| Life stage | juvenile |
| Body mass | ≈ 7.4 g |
| Trait | standard metabolic rate |
| Value | 117.0165483 mgO₂/h/kgFM |
| Test temperature | 21.5 °C |
| Technique | intermittent flow-through respirometry |
| Treatment | control: 0 mg/L NO₃⁻ (nitrate), pH 7.0 |
| Source | {cite}`gomezisaza2020nitrate` |

```{admonition} Not scientifically accurate
:class: note
Adapted for teaching: a realistic stand-in for a ShareTrait record, not a citable finding.
```

Motivating research question: *does the standard metabolic rate of the spangled perch scale with body mass, and does it change under nitrate or acidity stress?* Turning a question like this into something an ontology can answer is what [](build-your-own-ontology.md) is about.

## How the example grows

- **Linked data and RDF**: written as a handful of triples.
- **Build your own ontology**: classes and relations such as `Fish`, `LifeStage`, and `TraitMeasurement`, with axioms describing them.
- **Use your ontology**: the full ShareTrait sample dataset loaded, queried, and checked with a reasoner.
- **Map to external ontologies**: species and traits linked to [NCBI Taxonomy](http://purl.obolibrary.org/obo/NCBITaxon_317033) and [GBIF](https://www.gbif.org/species/2374497).
