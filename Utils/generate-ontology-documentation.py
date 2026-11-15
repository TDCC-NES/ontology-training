"""Generate the course's pyLODE page from its existing bicycle ontology."""

from pathlib import Path
import re

from pylode.profiles.ontpub import OntPub


project = Path(__file__).resolve().parent.parent
source = project / "book/data/bike-ontology.ttl"
destination = source.with_suffix(".html")
html = OntPub(ontology=str(source), sort_subjects=True).make_html()

# pyLODE lists class members without rendering individual sections. Keep their
# labels as text when the generated page has no matching fragment target.
targets = set(re.findall(r'\bid="([^"]+)"', html))


def retain_resolving_link(match):
    return match[0] if match[1] in targets else match[2]


html = re.sub(
    r'<a\b[^>]*href="#([^"]+)"[^>]*>(.*?)</a>',
    retain_resolving_link,
    html,
    flags=re.DOTALL,
)
html = html.replace(
    "</head>",
    '<link rel="alternate" type="text/turtle" href="bike-ontology.ttl">\n</head>',
    1,
)
html = html.replace(
    '<div id="content">',
    '<div id="content">\n'
    '<p><a href="bike-ontology.ttl" download>Download RDF (Turtle)</a> · '
    '<a href="curriculum/publish-your-ontology.html">Chapter 7</a>. '
    'This course example uses <code>example.org</code> identifiers as '
    'teaching placeholders.</p>',
    1,
)
html = "\n".join(line.rstrip() for line in html.splitlines()) + "\n"
destination.write_text(html, encoding="utf-8")
print(f"Generated {destination.relative_to(project)}")
