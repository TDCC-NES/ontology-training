# Working with Ontologies

An open training on designing, building and publishing OWL ontologies for researchers. Developed by the [TDCC-NES Ontology Engineers](https://tdcc.nl/nes/ontology-engineers/).

[Read the training](https://tdcc-nes.github.io/ontology-training/). The training is a work in progress.

Built with [TeachBooks](https://teachbooks.io/), using the [TeachBooks template](https://github.com/TeachBooks/template) and [deployment workflow](https://github.com/TeachBooks/deploy-book-workflow).

## Build locally

From the repository root, with Python installed:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
teachbooks build book
python -m http.server 8000 --directory book/_build/html
```

Open <http://localhost:8000>. Rebuild after editing the source files.

## Ontology documentation

The ontology publication consists of `book/data/bicycle-ontology.ttl` and its generated `book/data/bicycle-ontology.html`, served at `bicycle-ontology.ttl` and `bicycle-ontology.html`. The ontology contains definitions only. Teaching datasets remain separate course resources. The ontology uses the `https://w3id.org/bicycle-ontology/` namespace; w3id redirects the ontology and term IRIs to the published RDF and documentation.

After editing the ontology, regenerate the HTML with [pyLODE](https://github.com/RDFLib/pyLODE) 3.6.1, then rebuild the book:

```sh
python -m pip install pylode==3.6.1
pylode book/data/bicycle-ontology.ttl -o book/data/bicycle-ontology.html
```

The `bicycle:` prefix in the RDF lets pyLODE recognise the ontology namespace. Use the Turtle file to inspect the full logical class definitions.

## Ontology validation history

The original combined model was checked on 9 November 2026 with the course's installed OWLAPI 4.5.29 and HermiT 1.4.3.456:

- The combined model and the imported study passed the OWL 2 DL profile check, were consistent, and all their internally defined classes were satisfiable.
- The combined model passed 60 expected inference/non-inference checks. The imported study passed 66, including the cohort's membership and B004's exclusion.
- Protégé's bundled catalog resolver loaded the local import and matched its version IRI.
- Six invalid test variations produced the expected contradictions, covering component roles, functional values, inventory-code ranges and tag-based identity.
- Ask Wol's offline checks reported no errors, warnings or recommendations. Namespace and HTTP import checks were skipped; Web publication was not tested.

After separating definitions and data on 15 November 2026, 70 checks passed using HermiT and Protégé's XML catalog resolver. They covered OWL 2 DL compliance, consistency, class satisfiability, local imports and the expected classifications and identity inferences. At that stage, the published ontology contained no instance assertions, and combining the separated files preserved the original model statements.

The simplified reference model was checked on 19 November 2026 with the same OWLAPI/HermiT versions and catalog resolver. All 40 checks passed, covering OWL 2 DL compliance, consistency, class satisfiability, local imports, expected inferences and a contradictory wheel-count variation. The steel-frame query and SHACL checks retained their expected results.

The installed tools support the RDF 1.1 `rdf:langString` datatype used throughout the course. This extends OWL 2's original 2012 datatype map.

## Contribute

Keep internal working documents in `Utils/`, which is ignored by Git. Shared project helpers and publication configurations belong in `scripts/`.

[Open an issue](https://github.com/TDCC-NES/ontology-training/issues) or submit a pull request. Curriculum pages are in `book/curriculum/`; navigation is configured in `book/_toc.yml`.

For authoring and publishing instructions, see the [TeachBooks manual](https://teachbooks.io/manual/). The original demos and authoring exercises are available in the [TeachBooks template](https://github.com/TeachBooks/template/tree/main/book).

## Branding

Configure the logo and browser icon in `book/_config.yml`. Store images in `book/figures/`.

## Licence

Unless otherwise stated, the training content is licensed under [CC BY 4.0](LICENSE). You may share and adapt it, including commercially, with attribution, a link to the licence and an indication of changes. See [Credits and licence](https://tdcc-nes.github.io/ontology-training/credits.html) for attribution and third-party material.
