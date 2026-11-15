# Publish your ontology

:::{admonition} Learning objectives
:class: note

By the end of this chapter, you will be able to:

- Prepare an ontology's metadata and version identifiers for publication.
- Review an askwol report and generated documentation.
- Publish RDF and documentation using stable Web identifiers.
- Check that those identifiers retrieve the intended descriptions.
:::

Our research team can now use the bicycle ontology to compare inventory records. We will prepare it for publication so other researchers can inspect its definitions and reuse its terms.

The [askwol publication guide](https://lod-4tu.tudelft.nl/askwol/guide) provides the reference explanations and application commands. Here, we apply that guidance to the bicycle ontology and work through one publishing route: GitHub Pages hosts the files, and w3id redirects the identifiers to them.

This course publishes the [bicycle ontology as Turtle](https://tdcc-nes.github.io/ontology-training/main/bicycle-ontology.ttl) alongside its [pyLODE documentation](https://tdcc-nes.github.io/ontology-training/main/bicycle-ontology.html). Both are served by the course's GitHub Pages site. The ontology retains the `example.org` identifiers used in the earlier chapters; the walkthrough below shows how to replace these placeholders and configure their resolution for a real publication.

Public deployment in this example requires a GitHub account, permission to publish a public repository and a project identifier you intend to maintain. `YOUR-ACCOUNT` and `YOUR-PROJECT` below are placeholders. Replace them throughout with your GitHub account name and an available project path chosen using [w3id's naming guidance](https://docs.w3id.org/guides/create-an-id#_1-choose-a-name).

## Metadata and licence

Save a copy of the {download}`expanded bicycle ontology <../data/bicycle-ontology.ttl>` as `bicycle-ontology.ttl`. Its ontology header already records a title, description, creators, publisher, dates, licence and version. Use the guide's [metadata](https://lod-4tu.tudelft.nl/askwol/guide#metadata) and [licence](https://lod-4tu.tudelft.nl/askwol/guide#license) sections when reviewing these values.

Retain the original attribution and CC BY 4.0 licence for this example. If you adapt it, record your contribution and update the description and modification date to reflect your changes.

Agree any additional project requirements before publication, and use the {ref}`ontology-validation method <ontology-shacl-check>` to check their presence in the RDF. For example, a project can require an ontology title and a licence IRI. [TIB's draft metadata recommendations](https://github.com/TIBHannover/terminology-metadata) provide examples for ontologies and their terms.

(owl-versioning)=
## Version identifiers

The supplied ontology records version `2.0.0`. We keep that version for this publication and add its version IRI. Use the guide's [versioning section](https://lod-4tu.tudelft.nl/askwol/guide#versioning) as a reference for the [OWL versioning convention](https://www.w3.org/TR/owl2-syntax/#Versioning_of_OWL_2_Ontologies).

Apply the {doc}`IRI strategy from chapter 3 <design-your-own-ontology>` to the publication copy: change the ontology IRI from `https://example.org/bike` to `https://w3id.org/YOUR-PROJECT/`. In the `def:` and `id:` namespace declarations, replace `https://example.org/bike/` with `https://w3id.org/YOUR-PROJECT/`. The resulting identifiers include:

| Identifies | IRI |
|---|---|
| Ontology | `https://w3id.org/YOUR-PROJECT/` |
| Version | `https://w3id.org/YOUR-PROJECT/2.0.0` |
| Bicycle class | `https://w3id.org/YOUR-PROJECT/def/Bicycle` |
| B001 | `https://w3id.org/YOUR-PROJECT/id/B001` |

Add the version statement to the existing ontology header, keeping its other metadata:

```turtle
<https://w3id.org/YOUR-PROJECT/> a owl:Ontology ;
    owl:versionIRI <https://w3id.org/YOUR-PROJECT/2.0.0> ;
    owl:versionInfo "2.0.0" .
```

The `owl:` prefix is already declared in `bicycle-ontology.ttl`. Here we replace the course's placeholder identifiers before publication; once published, keep your identifiers stable. Apply the same namespace replacement to the queries and shapes used to check this copy.

## Review with askwol

Open [askwol](https://lod-4tu.tudelft.nl/askwol/) and upload `bicycle-ontology.ttl`. Review the report and follow the guide links beside individual findings. Record which findings you resolve and the reasons for retaining any deliberate modelling or documentation choices.

The reference ontology provides English and Dutch labels. A language consistency finding on a new term can identify a missing translation. Resolution warnings for the new w3id identifiers can be checked again after their redirects are live.

Use the {ref}`checks from chapter 6 <choose-the-right-check>` to review changes that affect the model or its use. The guide describes [the coverage of askwol's reasoning checks](https://lod-4tu.tudelft.nl/askwol/guide#reasoner).

(owl-ontology-structure)=
## Generate and review documentation

Follow the guide's [pyLODE instructions](https://lod-4tu.tudelft.nl/askwol/guide#documentation), using `bicycle-ontology.ttl` as input and `index.html` as output. Local generation requires [Python](https://www.python.org/downloads/). The guide's environment commands use macOS/Linux shell syntax; Python's [environment activation instructions](https://docs.python.org/3/library/venv.html#how-venvs-work) also cover Windows.

Open `index.html` in a browser. Locate Bicycle and `hasComponent`, and compare their displayed definitions with the RDF. Check that labels and definitions display correctly and that the licence, ontology IRI and version information agree with `bicycle-ontology.ttl`. After correcting the RDF, regenerate the page. Check external term links now and your new term links after publication.

The [course's generated page](https://tdcc-nes.github.io/ontology-training/main/bicycle-ontology.html) shows the expected layout for the supplied ontology.

:::{dropdown} Annotations on statements (reference)

The {ref}`building walkthrough <owl-entity-annotations>` introduced labels and definitions as entity annotations. Annotations can also document the ontology, individual axioms or other annotations. An axiom annotation can record evidence for a particular subclass statement. A source or review note helps people assess the statement; adding it leaves the class memberships inferred in our example unchanged. [Annotations](https://www.w3.org/TR/owl2-primer/#Annotating_Axioms_and_Entities)

The {ref}`cheat sheet <owl-cheat-declarations>` gives the declaration, annotation and ontology-header patterns.
:::

## Publish RDF and documentation

### Host the files

1. On GitHub, create a public repository named `bicycle-ontology`, with a README to initialise its `main` branch. A repository stores the files and their change history. See [GitHub's site creation instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).
2. Use **Add file > Upload files** to upload the reviewed `bicycle-ontology.ttl` and generated `index.html` to the repository root. Commit the upload to save it.
3. Use **Add file > Create new file** to create `releases/2.0.0/bicycle-ontology.ttl`, pasting the reviewed Turtle into it. Create `releases/2.0.0/index.html` with the generated HTML in the same way. These two files preserve this release; the root files provide the current publication.
4. Create an empty `.nojekyll` file at the repository root. This tells GitHub Pages to skip its default website builder, Jekyll, and publish the HTML already generated by pyLODE. [Publishing prepared files](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site#static-site-generators). Under **Settings > Pages**, select **Deploy from a branch**, `main` and **/(root)**, then save. [Publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

The repository should contain:

```text
.nojekyll
README.md
index.html
bicycle-ontology.ttl
releases/
  2.0.0/
    index.html
    bicycle-ontology.ttl
```

When deployment finishes, **Settings > Pages > Visit site** opens `https://YOUR-ACCOUNT.github.io/bicycle-ontology/`. The ontology documentation should appear there. Open its `bicycle-ontology.ttl`, `releases/2.0.0/` and `releases/2.0.0/bicycle-ontology.ttl` URLs too, and confirm that all four files are available before requesting redirects. GitHub Pages determines content types from file extensions; its [MIME type guidance](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site#mime-types-on-github-pages) explains how these are assigned.

### Connect the identifiers

Follow [w3id's identifier creation instructions](https://docs.w3id.org/guides/create-an-id) to fork its repository, creating your own copy in which to propose changes. In that copy, create `ids/YOUR-PROJECT/.htaccess`. This file configures the redirects on w3id. Add the following rules, replacing the account, project and maintainer placeholders:

```apache
# Identifier: https://w3id.org/YOUR-PROJECT/
# Maintainer: YOUR-NAME
# GitHub username: YOUR-ACCOUNT

RewriteEngine On
Header always merge Vary Accept

RewriteCond %{HTTP_ACCEPT} text/turtle [NC]
RewriteRule ^2\.0\.0/?$ https://YOUR-ACCOUNT.github.io/bicycle-ontology/releases/2.0.0/bicycle-ontology.ttl [R=303,L]
RewriteRule ^2\.0\.0/?$ https://YOUR-ACCOUNT.github.io/bicycle-ontology/releases/2.0.0/ [R=303,L]

RewriteCond %{HTTP_ACCEPT} text/turtle [NC]
RewriteRule ^(?:(?:def|id)(?:/[^/]*)?)?$ https://YOUR-ACCOUNT.github.io/bicycle-ontology/bicycle-ontology.ttl [R=303,L]
RewriteRule ^(?:(?:def|id)(?:/[^/]*)?)?$ https://YOUR-ACCOUNT.github.io/bicycle-ontology/ [R=303,L]
```

These rules direct explicit Turtle requests to the RDF and other requests to the documentation. The version IRI selects the preserved release; the ontology, namespace and term IRIs select the current files. The guide explains [HTTP delivery](https://lod-4tu.tudelft.nl/askwol/guide#server-config); w3id documents the [redirect rule syntax](https://docs.w3id.org/guides/htaccess).

Use w3id's [testing instructions](https://docs.w3id.org/guides/testing) before submitting a pull request, a request for the maintainers to review and merge your rules. The identifiers become available after the accepted change is deployed. The `.htaccess` belongs in the w3id repository; the ontology and HTML files remain on GitHub Pages.

## Check Web access

Once the redirects are live, open the ontology IRI, version IRI and Bicycle class IRI in a browser. Each should lead to the documentation. Follow term links on the page and check that you can find the corresponding definitions.

To check RDF access, open a terminal and use [curl](https://curl.se/docs/manpage.html), a command-line application for making Web requests. The command is `curl` on macOS/Linux and `curl.exe` in Windows PowerShell. If it is unavailable, follow curl's [installation guidance](https://curl.se/download.html).

Replace `YOUR-PROJECT` before running:

```sh
curl -L -D headers.txt -H "Accept: text/turtle" -o retrieved.ttl "https://w3id.org/YOUR-PROJECT/def/Bicycle"
```

`-L` follows redirects, `-D` saves response headers, `-H` requests Turtle and `-o` saves the response body. Open `headers.txt` and `retrieved.ttl` in a text editor. The expected responses are:

| Requested IRI | Accept header | Redirect destination | Final response |
|---|---|---|---|
| `/` | `text/html` | `bicycle-ontology/` | `200`, `text/html` |
| `/` | `text/turtle` | `bicycle-ontology/bicycle-ontology.ttl` | `200`, `text/turtle` |
| `/def/Bicycle` | `text/turtle` | `bicycle-ontology/bicycle-ontology.ttl` | `200`, `text/turtle` |
| `/def/hasComponent` | `text/turtle` | `bicycle-ontology/bicycle-ontology.ttl` | `200`, `text/turtle` |
| `/2.0.0` | `text/turtle` | `bicycle-ontology/releases/2.0.0/bicycle-ontology.ttl` | `200`, `text/turtle` |

The request paths above follow `https://w3id.org/YOUR-PROJECT`; destinations follow `https://YOUR-ACCOUNT.github.io/`. Each listed request should first receive a `303` redirect. A final content type may include a character encoding, such as `text/html; charset=utf-8`.

Repeat the command for the other paths, using `Accept: text/html` for the HTML check. Load the retrieved Turtle in Protégé and confirm that it contains the expected ontology and version IRIs, Bicycle's definition and `hasComponent`'s domain and range. At this first publication, the current and version-specific RDF should contain the same statements.

Rerun askwol on the published RDF and review the resolution findings. If a request fails, use the recorded redirect destination to locate whether the problem is in the w3id rule or the hosted file. After the checks pass, share the ontology IRI with the research community and, where suitable, submit it to a relevant vocabulary catalogue.
