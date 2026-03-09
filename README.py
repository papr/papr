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
backend_tree = tree.add("Backend experience with", guide_style="#BFDB38")
backend_tree.add("Domain-driven development")
backend_tree.add("FastAPI + Pydantic")
backend_tree.add("SQLAlchemy")

frontend_tree = tree.add("Frontend experience with", guide_style="#BFDB38")
frontend_tree.add("Vue and its reactivity system")
frontend_tree.add("Primevue, vue-query, and vee-validate")

tree.add("Expert for head-mounted\nappearance-based eye-tracking")
maintainer_tree = tree.add("Previous maintainer of", guide_style="#BFDB38")
pupil_core_tree = maintainer_tree.add(
    "[link=https://github.com/pupil-labs/pupil]Pupil Core", guide_style="#1F8A70"
)
pupil_core = (
    "👁️ [link=https://github.com/pupil-labs/pye3d-detector]pye3d[/link] - 3d eye state estimator",
    "🎥 [link=https://github.com/pupil-labs/pyuvc]pyuvc[/link] - UVC camera access",
    "🔗 [link=https://github.com/pupil-labs/ndsi]ndsi[/link] - Network State\n"
    "Synchronization Protocol",
    "...",
)
for item in pupil_core:
    pupil_core_tree.add(item)

integrations_tree = pupil_core_tree.add("3rd-party integrations", guide_style="#00425A")
integrations_tree.add(
    "[link=https://github.com/labstreaminglayer/App-PupilLabs/]LabStreamingLayer"
)
integrations_tree.add(
    "[link=https://psychopy.org/api/iohub/device/eyetracker_interface/"
    "PupilLabs_Core_Implementation_Notes.html#pupil-labs-core]PsychoPy"
)

pupil_invisible = ()
pupil_invisible_tree = maintainer_tree.add("Pupil Invisible", guide_style="#1F8A70")
pupil_invisible_tree.add(
    "[link=https://pupil-labs-realtime-api.readthedocs.io/en/latest/]"
    "REST+RTSP Realtime API"
)
pupil_invisible_tree.add(
    "[link=https://pupil-invisible-lsl-relay.readthedocs.io/en/stable/]"
    "LabStreamingLayer Relay"
)
maintainer_tree.add("...")

tree.add("🎩🪄📦 Python Packaging Wizard")
tree.add("Discord Community Moderator")
tree.add("Student Group Volunteer")

about = """\
Having been the first senior software engineer at [link=https://www.uneos.io/]UNEOS[/link], \
I shaped the development of our early prototypes and became lead of the core services.

At Pupil Labs, I developed and maintained open source Python desktop software, starting mid 2016. \
Having built a community on [link=https://pupil-labs.com/chat]Discord[/link], I helped \
our users build their custom solutions based on it.

During my Cognitive Science BSc. in Osnabrück and Computer Science MSc. in Berlin, I \
got a solid under- standing of the wide variety of Machine Learning algorithms and \
categories, and learned when to apply them.

In my free time, I enjoy cooking, Yoga, and to ride my bike. From time to time, \
you can find me hiking in the mountains.\
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
