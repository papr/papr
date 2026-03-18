"""
Based on https://github.com/willmcgugan/willmcgugan/tree/d915069a3f7460fcb8f244ce91a35ac8a53905c3
Thank you @willmcgugan

Color palette: https://colorhunt.co/palette/00425a1f8a70bfdb38fc7300
"""

from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree(
    "[link=https://www.linkedin.com/in/pablo-prietz/]Pablo Prietz",
    guide_style="#FC7300",
)

practices_tree = tree.add("Best practices & knowledge transfer", guide_style="#BFDB38")
practices_tree.add("Domain-driven development")
practices_tree.add("Cross-team standards & mentoring")

backend_tree = tree.add("Backend", guide_style="#BFDB38")
backend_tree.add("FastAPI + Pydantic + SQLAlchemy")

frontend_tree = tree.add("Frontend", guide_style="#BFDB38")
frontend_tree.add("TypeScript + Vue")

oss_tree = tree.add("Previous maintainer of", guide_style="#BFDB38")
oss_tree.add(
    "[link=https://github.com/pupil-labs/pupil]Pupil Core[/link] - open-source\n"
    "eye-tracking platform (1.7k ⭐)",
    guide_style="#1F8A70",
)
oss_tree.add(
    "[link=https://github.com/pupil-labs/pl-realtime-api]pl-realtime-api[/link] -\n"
    "async real-time eye-tracking client",
    guide_style="#1F8A70",
)

tree.add("🎩🪄📦 Python Packaging Wizard")

about = """\
Senior software engineer with a decade of \
experience across open-source tooling, \
real-time systems, and full-stack web \
development. Passionate about establishing \
best practices, mentoring teams, and \
driving knowledge transfer.

Currently building domain-driven SaaS systems at \
[link=https://www.uneos.io/]UNEOS[/link].
Previously maintained \
[link=https://github.com/pupil-labs/pupil]\
Pupil Core[/link], an \
open-source eye-tracking platform.\
"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="#00425A", title="[b]Hi there", width=40
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

args = dict(inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
file = "README.md"

console.save_html(file, **args)
