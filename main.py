# World news, Friday 20 November 2026, in one image (v4).
# The image is entry.png in this repository: a dense 1024x1024
# newspaper front page with 33 stories from Friday 20 November
# 2026 only, across 6 regions. Leads: Cyclone Akvan coming
# ashore in Odisha, 100+ missiles hitting Kyiv, and Asia's
# markets plunging on the AI sell-off. Also on the page: 10
# small cards, a world map, 20 briefs, and a DATE CHECK box
# that deliberately excludes 19 November stories (the
# Shenzhen summit, Anthropic's IPO debut, the Myanmar
# ruling, the GTA VI launch, Voyager 1).
# Typeset with Noto Serif Display / Noto Serif / Liberation Sans.
# This program only copies that image to the output path.
# It uses only the Python standard library, needs no network,
# and writes exactly the same bytes on every run.
# The copy is byte-for-byte: no re-encoding, no resizing,
# so the program's two runs always write identical bytes.
import os
import shutil
from pathlib import Path

def main():
    here = Path(__file__).resolve().parent
    source = here / 'entry.png'
    out_dir = Path(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / 'entry.png')

if __name__ == '__main__':
    main()
