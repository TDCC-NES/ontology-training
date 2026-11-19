# Maintain your ontology

:::{admonition} Learning objectives
:class: note

By the end of this chapter, you will be able to:

- Agree responsibilities for reviewing changes and maintaining an ontology's publication.
- Assess how a proposed change affects existing data, queries and inferences.
- Prepare a documented release and explain how to retire a term while keeping its meaning available.
:::

```{admonition} Under development
:class: warning
This chapter is a draft.
```

Maintaining the bicycle ontology means reviewing changes and helping users update their inventories and queries.

## Governance

*Governance* sets out who maintains the ontology and how changes are agreed. For a small team, a named maintainer and a shared place to discuss changes may be enough.

### Agree responsibilities

Record who will:

- Review terms and definitions with researchers who collect and use the data.
- Implement agreed changes and run checks.
- Publish releases and maintain documentation, hosting and identifier redirects.
- Handle user feedback and handover.

Give users a contact address or issue tracker for requests and discussion. See the OBO Foundry's [responsiveness guidance](https://obofoundry.org/principles/fp-020-responsiveness.html).

At handover, transfer source files, release history, outstanding requests and hosting and redirect access to a named successor.

If active maintenance ends, state this and the last release date on the landing page. Keep releases and term descriptions accessible through their IRIs, using an archive if needed. [OBO ontology statuses](https://obofoundry.org/docs/OntologyStatus.html), [W3C preservation guidance](https://www.w3.org/TR/dwbp/#DataPreservation)

### Review change requests

Following the {ref}`iterative workflow <ontology-development-workflow>`, record the affected terms, research need, representative record, proposed change and decision with its reason.

Review definitions and actual statements with domain experts. Similar labels may name different relationships, or one property may express several. Agree which terms to retain, clarify, combine or separate.

For example, adding material composition extends the bicycle ontology's scope. Agree whether that detail is needed, which terms to reuse and how existing records are affected.

## Versioning and releases

A *release* is an identified version published for others to use. Keep working revisions separate from releases. Chapter 7 covers {ref}`version identifiers <owl-versioning>` and {ref}`preserving releases <version-specific-publication>`. [OBO versioning guidance](https://obofoundry.org/principles/fp-004-versioning.html)

### Assess compatibility

Check how a proposed change affects existing uses:

| Proposed change | What to review |
|---|---|
| Correct labels or clarify wording without changing meaning | Displays and applications that match the text |
| Add terms or axioms | Inferences, consistency and query answers |
| Replace text values with resource links | Existing RDF, conversion mappings, queries and shapes |
| Retire or replace a term | Uses of its IRI and migration instructions |

As in chapter 5, classifying one component as both Frame and Wheel contradicts their disjointness. After changes, repeat the {ref}`chapter 6 checks <choose-the-right-check>` on earlier and new records, and explain changes to expected results.

Keep a term's IRI when correcting its label or clarifying its meaning. Create a new term and IRI if what it refers to would substantially change. [Term-stability guidance](https://obofoundry.org/principles/fp-019-term-stability.html)

Mark retired terms with `owl:deprecated true`, explain why and link to any suggested replacements. Keep their IRIs and descriptions available, and provide migration instructions for existing data and queries. [OWL deprecation](https://www.w3.org/TR/owl2-syntax/#Annotation_Properties)

### Prepare a release

Choose and document a versioning policy. Date-based identifiers such as `2026-11-19` can suit regular snapshots. Compatibility-based numbers signal the intended impact of an update. A team drawing on [Semantic Versioning](https://semver.org/spec/v2.0.0.html) could use this policy for future bicycle releases:

| Release | Example change |
|---|---|
| `1.0.1` | Correct label spelling while preserving meaning and agreed uses |
| `1.1.0` | Add terms while preserving agreed existing uses |
| `2.0.0` | Replace material text with resource links; data and queries need migration |

Define compatibility against supported data patterns, queries and expected inferences, including the frame-material query and its expected answers.

For each release:

1. Review the agreed changes and test results.
2. Update version metadata and write release notes with changes, reasons and migration instructions.
3. Regenerate and review documentation, then publish using the chapter 7 workflow. Preserve earlier releases unchanged.
4. Check ontology and term IRIs, and notify users.

Retain versioned check materials as described in {doc}`use-and-evaluate-your-ontology`. Record imported versions, using version IRIs where available, and test updates before release. [OWL imports](https://www.w3.org/TR/owl2-syntax/#Imports)
