# OWL Ontology Training

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

## Contribute

[Open an issue](https://github.com/TDCC-NES/ontology-training/issues) or submit a pull request. Curriculum pages are in `book/curriculum/`; navigation is configured in `book/_toc.yml`.

For authoring and publishing instructions, see the [TeachBooks manual](https://teachbooks.io/manual/). The original demos and authoring exercises are available in the [TeachBooks template](https://github.com/TeachBooks/template/tree/main/book).

## Branding

Configure the logo and browser icon in `book/_config.yml`. Store images in `book/figures/`.

## Licence

Unless otherwise stated, the training content is licensed under [CC BY 4.0](LICENSE). You may share and adapt it, including commercially, with attribution, a link to the licence and an indication of changes. See [Credits and licence](https://tdcc-nes.github.io/ontology-training/credits.html) for attribution and third-party material.
