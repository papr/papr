"""
Based on https://github.com/willmcgugan/willmcgugan/tree/d915069a3f7460fcb8f244ce91a35ac8a53905c3
Thank you @willmcgugan
"""

from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=100)

tree = Tree(
    "🧑🏻‍🦲 [link=https://www.linkedin.com/in/pablo-prietz/]Pablo Prietz",
    guide_style="#FC7300",
)
maintainer_tree = tree.add("Maintainer of", guide_style="#BFDB38")
pupil_core_tree = maintainer_tree.add(
    "[link=https://github.com/pupil-labs/pupil]Pupil Core", guide_style="#1F8A70"
)
pupil_core = (
    "👁️  [link=https://github.com/pupil-labs/pye3d-detector]pye3d[/link] - 3d eye state estimator",
    "🎥 [link=https://github.com/pupil-labs/pyuvc]pyuvc[/link] - UVC camera access",
    "🖥️  [link=https://github.com/pupil-labs/pyglui]pyglui[/link] - OpenGL UI",
    "🔗 [link=https://github.com/pupil-labs/ndsi]ndsi[/link] - OpenGL UI",
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


# full_stack_tree = tree.add("🔧 Full-stack developer")
# tree.add("📘 Author")

about = """\
Professionally, I develop and maintain open source Python desktop software, and help \
our community to build custom solutions based on it.

In my free time, I enjoy cooking 🧑‍🍳🥘, Yoga 🧘 and to work on my handstand. 🤸\
"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="#00425A", title="[b]Hi there", width=30
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)