# Publish your ontology

:::{admonition} Learning objectives
:class: note

By the end of this chapter, you will be able to:

- Prepare an ontology's metadata and version identifiers for publication.
- Assess askwol findings and check generated documentation against the ontology's RDF.
- Publish RDF and documentation using stable Web identifiers.
- Check that ontology and term IRIs retrieve the intended RDF and documentation.
:::

Our research team can now use the bicycle ontology to compare inventory records. We will prepare it for publication so other researchers can inspect its definitions and reuse its terms.

The [askwol publication guide](https://askwol.net/guide) provides the reference explanations and application commands. Here, we apply that guidance to the bicycle ontology and work through one publishing route: GitHub Pages hosts the files, and w3id redirects the identifiers to them.

This course publishes the [bicycle ontology as Turtle](https://tdcc-nes.github.io/ontology-training/main/bicycle-ontology.ttl) alongside its [pyLODE documentation](https://w3id.org/bicycle-ontology/). Both are served by the course's GitHub Pages site. The ontology contains definitions only. It uses the `https://w3id.org/bicycle-ontology/` namespace throughout the course, with w3id redirects to these files. The walkthrough below shows how to prepare your own publication and configure identifier resolution.

Public deployment in this example requires a GitHub account, permission to publish a public repository and a project identifier you intend to maintain. Replace `YOUR-OWNER` below with the repository owner's GitHub username or organisation name, and `YOUR-PROJECT` with an available project path chosen using [w3id's naming guidance](https://docs.w3id.org/guides/create-an-id#_1-choose-a-name).

## Metadata and licence

Save a copy of the {download}`bicycle reference ontology <../data/bicycle-ontology.ttl>` as `bicycle-ontology.ttl`. Its ontology header already records a title, description, creators, publisher, dates, licence and version. Use the guide's [metadata](https://askwol.net/guide#metadata) and [licence](https://askwol.net/guide#license) sections when reviewing these values.

Retain the original attribution and CC BY 4.0 licence for this example. If you adapt it, record your contribution and update the description and modification date to reflect your changes.

Agree any additional project requirements before publication, and use the {ref}`ontology-validation method <ontology-shacl-check>` to check their presence in the RDF. For example, a project can require an ontology title and a licence IRI. [TIB's draft metadata recommendations](https://github.com/TIBHannover/terminology-metadata) provide examples for ontologies and their terms.

If you also publish research data described using your ontology, provide metadata for the dataset and its downloadable files. See the W3C's [guidance on descriptive metadata](https://www.w3.org/TR/dwbp/#DescriptiveMetadata), which recommends the [Data Catalog Vocabulary (DCAT)](https://www.w3.org/TR/vocab-dcat-3/).

(owl-versioning)=
## Version identifiers

The supplied ontology records version `1.0.0` with `owl:versionInfo`. A separate version IRI is optional; the {ref}`version-specific publication instructions <version-specific-publication>` show how to preserve a release at its own IRI. Use the guide's [versioning section](https://askwol.net/guide#versioning) as a reference for the [OWL versioning convention](https://www.w3.org/TR/owl2-syntax/#Versioning_of_OWL_2_Ontologies).

For your own publication, apply the {doc}`IRI strategy from chapter 3 <design-your-own-ontology>`: replace `https://w3id.org/bicycle-ontology/` with `https://w3id.org/YOUR-PROJECT/` throughout the publication copy. This updates the ontology IRI and its namespace declarations. The resulting identifiers include:

| Identifies | IRI |
|---|---|
| Ontology | `https://w3id.org/YOUR-PROJECT/` |
| Bicycle class | `https://w3id.org/YOUR-PROJECT/def/Bicycle` |
| hasComponent property | `https://w3id.org/YOUR-PROJECT/def/hasComponent` |

The publication copy's ontology header retains its other metadata and version information:

```turtle
<https://w3id.org/YOUR-PROJECT/> a owl:Ontology ;
    owl:versionInfo "1.0.0" .
```

The `owl:` prefix is already declared in `bicycle-ontology.ttl`. Apply the same namespace replacement to copies of the data, mappings, queries and shapes used to check this ontology. Update any `owl:imports` IRIs and local catalog entries that use the old namespace.

Before publishing, check that the ontology and term IRIs are spelled correctly and follow your chosen IRI strategy, since users will rely on these identifiers remaining stable. Changing them later can require time-consuming updates to datasets and queries and leave users unsure which IRIs to use. See the W3C's guidance on [identifier persistence](https://www.w3.org/TR/webarch/#URI-persistence) and [the costs of multiple identifiers for the same resource](https://www.w3.org/TR/webarch/#uri-aliases).

## Review with askwol

Open [askwol](https://askwol.net/) and upload the prepared `bicycle-ontology.ttl` to review its contents before generating documentation. Follow the guide links beside individual findings as you review the report, and record which findings you resolve and the reasons for retaining any deliberate modelling or documentation choices.

The reference ontology provides English and Dutch labels. A language consistency finding on a new term can identify a missing translation.

Because askwol also checks whether namespaces resolve on the Web, a warning for your new namespace is expected until its w3id redirects are live. Investigate findings about existing external vocabularies now, and recheck your new namespace after deployment.

Use the {ref}`checks from chapter 6 <choose-the-right-check>` to review changes that affect the model or its use. The guide describes [the coverage of askwol's reasoning checks](https://askwol.net/guide#reasoner).

(owl-ontology-structure)=
## Generate and review documentation

Local generation requires [Python 3.12 or newer](https://www.python.org/downloads/). Open a terminal and use `cd` to select the folder containing `bicycle-ontology.ttl`, as in the {ref}`conversion setup <rmlmapper-setup>`.

On macOS/Linux, use the environment creation and activation commands in the guide's [setup instructions](https://askwol.net/guide#documentation). On Windows PowerShell, use:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Python's [environment instructions](https://docs.python.org/3/library/venv.html#how-venvs-work) cover activation on other shells and PowerShell execution settings. With the environment activated, install the tested pyLODE version and generate the documentation:

```sh
python -m pip install pylode==3.6.1
pylode bicycle-ontology.ttl -o index.html
```

Open `index.html` in a browser. Locate Bicycle and `hasComponent`, and compare their displayed definitions with the RDF. Check that labels and definitions display correctly and that the licence, ontology IRI and version information agree with `bicycle-ontology.ttl`. Inspect the steel-frame class expressions in the Turtle file as well: pyLODE does not render every construct. After correcting the RDF, regenerate the page. Check external term links now and your new term links after publication.

In pyLODE 3.6.1, bilingual labels appear joined in headings and navigation, for example “bicyclefiets”. Preserve the separate language-tagged labels in the RDF.

The [course's generated page](https://w3id.org/bicycle-ontology/) shows the expected layout for the supplied ontology.

:::{dropdown} Annotations on statements (reference)

The {ref}`building walkthrough <owl-entity-annotations>` introduced labels and definitions as entity annotations. Annotations can also document the ontology, individual axioms or other annotations. An axiom annotation can record evidence for a particular subclass statement. A source or review note helps people assess the statement; adding it leaves the class memberships inferred in our example unchanged. [Annotations](https://www.w3.org/TR/owl2-primer/#Annotating_Axioms_and_Entities)

The {ref}`cheat sheet <owl-cheat-declarations>` gives the declaration, annotation and ontology-header patterns.
:::

## Publish RDF and documentation

### Host the files

1. On GitHub, create a public repository named `bicycle-ontology`, with a README to initialise its `main` branch. A repository stores the files and their change history. See [GitHub's site creation instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).
2. Use **Add file > Upload files** to upload the reviewed `bicycle-ontology.ttl` and generated `index.html` to the repository root. Commit the upload to save it.
3. Create an empty `.nojekyll` file at the repository root. This tells GitHub Pages to skip its default website builder, Jekyll, and publish the HTML already generated by pyLODE. [Publishing prepared files](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site#static-site-generators). Under **Settings > Pages**, select **Deploy from a branch**, `main` and **/(root)**, then save. [Publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

The repository should contain:

```text
.nojekyll
README.md
index.html
bicycle-ontology.ttl
```

When deployment finishes, **Settings > Pages > Visit site** opens `https://YOUR-OWNER.github.io/bicycle-ontology/`. The ontology documentation should appear there. Open `https://YOUR-OWNER.github.io/bicycle-ontology/bicycle-ontology.ttl` too, and confirm that both files are available before requesting redirects. GitHub Pages determines content types from file extensions; its [MIME type guidance](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site#mime-types-on-github-pages) explains how these are assigned.

### Connect the identifiers

Follow [w3id's identifier creation instructions](https://docs.w3id.org/guides/create-an-id) to fork its repository, creating your own copy in which to propose changes. In that copy, create `ids/YOUR-PROJECT/.htaccess`. This file configures the redirects on w3id. Add the following rules, replacing `YOUR-NAME` with the maintainer's name and `YOUR-USERNAME` with their personal GitHub username. `YOUR-OWNER` remains the account or organisation that owns the ontology repository.

```apache
# Identifier: https://w3id.org/YOUR-PROJECT/
# Maintainer: YOUR-NAME
# GitHub username: YOUR-USERNAME

RewriteEngine On
Header always merge Vary Accept

RewriteCond %{HTTP_ACCEPT} text/turtle [NC]
RewriteRule ^(?:def(?:/[^/]*)?)?$ https://YOUR-OWNER.github.io/bicycle-ontology/bicycle-ontology.ttl [R=303,L]
RewriteRule ^(?:def(?:/[^/]*)?)?$ https://YOUR-OWNER.github.io/bicycle-ontology/ [R=303,L]
```

These rules direct explicit Turtle requests to the RDF and other requests to the documentation. The ontology, namespace and term IRIs select the current files. The guide explains [HTTP delivery](https://askwol.net/guide#server-config); w3id documents the [redirect rule syntax](https://docs.w3id.org/guides/htaccess).

(version-specific-publication)=
:::{dropdown} Version-specific publication (optional)

To preserve version `1.0.0` at `https://w3id.org/YOUR-PROJECT/1.0.0`:

1. Add `owl:versionIRI` to the publication copy's existing ontology header, keeping its other metadata:

   ```turtle
   <https://w3id.org/YOUR-PROJECT/> a owl:Ontology ;
       owl:versionIRI <https://w3id.org/YOUR-PROJECT/1.0.0> ;
       owl:versionInfo "1.0.0" .
   ```

2. Regenerate `index.html` and upload both updated root files. Use **Add file > Create new file** to create `releases/1.0.0/bicycle-ontology.ttl`, pasting the reviewed Turtle into it. Create `releases/1.0.0/index.html` with the generated HTML in the same way. Confirm that both release URLs are available on GitHub Pages.
3. Insert these rules before the current-file rules in your proposed w3id `.htaccess`:

   ```apache
   RewriteCond %{HTTP_ACCEPT} text/turtle [NC]
   RewriteRule ^1\.0\.0/?$ https://YOUR-OWNER.github.io/bicycle-ontology/releases/1.0.0/bicycle-ontology.ttl [R=303,L]
   RewriteRule ^1\.0\.0/?$ https://YOUR-OWNER.github.io/bicycle-ontology/releases/1.0.0/ [R=303,L]
   ```

In pyLODE 3.6.1, the generated link for `owl:versionIRI` points to a missing `#1.0.0` fragment. Use the full version IRI for the checks below.

The version IRI selects the preserved release; the root files provide the current publication. Keep the release files unchanged when publishing a later version. After deployment, check the version IRI with both Accept headers: expect a `303` redirect to the release's Turtle or HTML, followed by `200` with the corresponding content type. At this first publication, the current and version-specific RDF should contain the same statements.
:::

Use w3id's [testing instructions](https://docs.w3id.org/guides/testing) before submitting a pull request, a request for the maintainers to review and merge your rules. The identifiers become available after the accepted change is deployed. The `.htaccess` belongs in the w3id repository; the ontology and HTML files remain on GitHub Pages.

## Check Web access

Once the redirects are live, open the ontology IRI and Bicycle class IRI in a browser. Each should lead to the documentation. Follow term links on the page and check that you can find the corresponding definitions.

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

The request paths above follow `https://w3id.org/YOUR-PROJECT`; destinations follow `https://YOUR-OWNER.github.io/`. Each listed request should first receive a `303` redirect. A final content type may include a character encoding, such as `text/html; charset=utf-8`.

Repeat the command for the other paths, using `Accept: text/html` and `-o retrieved.html` for the HTML check. Load the retrieved Turtle in Protégé and confirm that it contains the expected ontology IRI, version information, Bicycle's definition and `hasComponent`'s domain and range.

Upload `retrieved.ttl` to askwol to review the published RDF, checking that your new namespace now resolves. If a request fails, use the recorded redirect destination to locate whether the problem is in the w3id rule or the hosted file. If you correct the RDF, regenerate its documentation and republish the affected files. Repeat the affected checks once any file or redirect corrections are deployed.

After the checks pass, share the ontology IRI with the research community and, where suitable, submit it to a relevant vocabulary catalogue.
