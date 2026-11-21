# Maintain your ontology

:::{admonition} Learning objectives
:class: note

By the end of this chapter, you will be able to:

- Identify responsibilities for reviewing changes and maintaining an ontology's publication.
- Compare versioning approaches for an ontology and its term IRIs.
- Assess how a proposed change affects existing data, queries and inferences.
- Describe how to prepare a documented release and retire a term while keeping its meaning available.
:::

Maintaining the bicycle ontology means reviewing changes and helping users update their inventories and queries.

## Governance

*Governance* sets out who maintains the ontology and how changes are agreed. For a small team, a named maintainer and a shared place to discuss changes may be enough.

### Agree responsibilities

When a researcher reports a problem, the team needs to know who can act on it. A record of responsibilities identifies who will:

- Review terms and definitions with researchers who collect and use the data.
- Implement agreed changes and run checks.
- Publish releases and maintain documentation, hosting and identifier redirects.
- Handle user feedback and handover.

The record also names who approves changes to meaning or scope, accepts file changes and authorises releases, and how disagreements are resolved. One person may hold several roles.

Larger collaborations can separate routine editing from wider decisions. The [Ontology for Biomedical Investigations (OBI)](https://github.com/obi-ontology/obi#making-changes) uses automated tests and developer review before a senior developer merges changes. In [EMMO](https://github.com/emmo-repo/EMMO/blob/master/doc/EMMO_governance.md#emmo-governance-committee), editors manage routine changes, while a governance committee handles key decisions. The committee seeks consensus and uses a majority vote if needed.

A contact address or issue tracker gives researchers a way to report unclear terms, request changes and discuss their needs with the maintainers. The OBO Foundry's [responsiveness guidance](https://obofoundry.org/principles/fp-020-responsiveness.html) recommends GitHub for public issue tracking.

A named successor needs the source files, release history, outstanding requests and access to hosting and redirects to continue maintenance after a handover.

If active maintenance ends, a notice and the last release date on the landing page let users know the ontology's status. Keeping releases and term descriptions accessible through their IRIs, using an archive if needed, lets researchers interpret earlier data. [OBO ontology statuses](https://obofoundry.org/docs/OntologyStatus.html), [W3C preservation guidance](https://www.w3.org/TR/dwbp/#DataPreservation)

### Review change requests

Following the {ref}`iterative workflow <ontology-development-workflow>`, a change request connects a research need and representative record to the affected terms and proposed change. Recording the decision and its reason lets later maintainers see why the change was accepted or rejected.

In the GitHub repository introduced in {doc}`chapter 7 <publish-your-ontology>`, an *issue* can record the request, discussion and decision. A linked *pull request* proposes the file changes for review, including results from the {ref}`chapter 6 checks <choose-the-right-check>`. After approval, changes can be included in a release. [Linking issues and pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)

Similar labels may name different relationships, or one property may express several. Reviewing definitions and actual statements with domain experts helps establish which terms to retain, clarify, combine or separate.

For example, adding material composition extends the bicycle ontology's scope. The decision depends on the research need, the terms available for reuse and the effects on existing records.

## Versioning and releases

A *release* is an identified version published for others to use. Separate working revisions let the team develop and check changes while published releases remain available for reuse. Chapter 7 covers {ref}`version identifiers <owl-versioning>` and {ref}`preserving releases <version-specific-publication>`. [OBO versioning guidance](https://obofoundry.org/principles/fp-004-versioning.html)

Versioning a release and versioning its terms are separate choices. Following chapter 7's publication pattern, `https://w3id.org/bicycle-ontology/1.0.0` could identify a release, while `https://w3id.org/bicycle-ontology/def/Bicycle` identifies its Bicycle class. A later release can keep that class IRI. [OWL versioning](https://www.w3.org/TR/owl2-syntax/#Versioning_of_OWL_2_Ontologies)

| Approach | Consequences for data and reuse |
|---|---|
| Version-independent term IRIs | Data keeps the same class and property identifiers across releases. The ontology release used is recorded separately so its definitions can be retrieved. |
| Release-specific term IRIs | Term IRIs include the release identifier. Updating to a new release can require changing identifiers in data, queries and mappings, even for unchanged terms. |

The Financial Industry Business Ontology (FIBO) combines version-independent term IRIs with access to each term's description in a chosen release. Its [Customer IRI](https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Customer) retrieves the current description; its [Customer IRI for release 2025 Q4](https://spec.edmcouncil.org/fibo/ontology/master/2025Q4/FND/ProductsAndServices/ProductsAndServices/Customer) includes `master/2025Q4` in the path and retrieves that release's description. In the [release RDF](https://spec.edmcouncil.org/fibo/ontology/master/2025Q4/FND/ProductsAndServices/ProductsAndServices.ttl), the class still uses the version-independent IRI.

A fixed release IRI identifies which definitions were used. An IRI containing `latest` can retrieve different content later.

### Assess compatibility

Common maintenance changes include adding terms, improving labels and definitions, revising hierarchies and logical statements, and retiring terms. [Examples from QUDT's release history](https://github.com/qudt/qudt-public-repo/releases/tag/v3.5.3) A revised class definition can change inferred classifications and the answers to queries that use those inferences, even when the recorded data stays the same. These effects matter when comparing results obtained with different ontology releases.

As in chapter 5, classifying one component as both Frame and Wheel contradicts their disjointness. Repeating the {ref}`chapter 6 checks <choose-the-right-check>` on earlier and new records can reveal changes to classifications or query answers. Reasons recorded alongside revised expected results help later reviewers understand which changes were intended.

With version-independent term IRIs, a term's IRI stays the same when correcting its label or clarifying its meaning, so existing data continues to refer to the same term. A substantial change to what it refers to calls for a new term and IRI, preserving the meaning of the earlier descriptions. [Term-stability guidance](https://obofoundry.org/principles/fp-019-term-stability.html)

The annotation `owl:deprecated true` marks a term as retired. A note alongside it explains why and links to any suggested replacements. Keeping the IRI and description available lets researchers interpret earlier data; migration instructions explain how to update existing data and queries. [OWL deprecation](https://www.w3.org/TR/owl2-syntax/#Annotation_Properties)

### Prepare a release

A documented versioning policy explains how releases are numbered or dated. Date-based identifiers such as `2026-11-19` can suit regular snapshots. Compatibility-based numbers signal the intended impact of an update. A team drawing on [Semantic Versioning](https://semver.org/spec/v2.0.0.html) could use this policy for future bicycle releases:

| Release | Example change |
|---|---|
| `1.0.1` | Correct label spelling while preserving meaning and agreed uses |
| `1.1.0` | Add terms while preserving agreed existing uses |
| `2.0.0` | Replace material text with resource links; data and queries need migration |

For this policy, an update is compatible when it preserves the agreed data patterns, query answers and inferences. The frame-material query and its expected answers are one check of that agreement.

A release brings together the agreed changes and the information users need to assess and adopt them. The preparation steps are:

1. Review the agreed changes and test results.
2. Update version metadata and write release notes with changes, reasons and migration instructions.
3. Regenerate and review documentation, then publish using the chapter 7 workflow. Preserve earlier releases unchanged.
4. Check ontology and term IRIs, and notify users.

Versioned check materials, as described in {doc}`use-and-evaluate-your-ontology`, let the team repeat earlier checks. This record includes the imported ontology versions, using version IRIs where available, and the results of checking updates before release. [OWL imports](https://www.w3.org/TR/owl2-syntax/#Imports)
