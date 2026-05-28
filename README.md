---
updated: 2023-12-26 18:17
id: 01HJM8WWDDF4R183R00NEP2VN8
---

## HIVE private beta

> [!IMPORTANT] Build Version  
> built and tested in stable Build TouchDesigner 2025 32820 with most features compatible on MacOS

### LICENSE

____
> [!info]+  
> Copyright (c) 2026 [Drmbt](https://github.com/drmbt)  
> [Vincent Naples](mailto:vincent@drmbt.com)  
> [drmbt.com](https://www.drmbt.com)
> [instagram](https://instagram.com/drmbt)

This file is part of HIVE

HIVE is a family of global components and ui elements that become more powerful when they interface together. HIVE is powerful, dangerous, and quite possibly full of bugs.

As this primarily exists as a personal tool and study of TouchDesigner, git, Python, and general UI/UX design,  it is in this form being distributed in hope that others may find it useful, but WITHOUT ANY WARRANTY;  without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

I haven't figured out licensing yet. For now, please consider yourself a closed beta tester, and refer other users to me if you're compelled to share it with someone

---

#### Why I am building this

I am building a loose family of tools, UI elements and plugins that constitute an operating system and style guide for building reusable workflows in TouchDesigner. These are adapted from my own explorations, other public user contributions, and philosophies borrowed from other media servers and vj tools such as Resolume, VDMX, Quartz Composer and Madmapper, as well as inspiration from TD power users including [Darien Brito](https://darienbrito.com/), [Richard Burns](), [Jarret Smith](https://www.linkedin.com/in/jarrett-smith-b191a461), [Wieland Hilker](https://alphamoonbase.de/), [Ivan Del Sol](https://instagram.com/spiderdelsol), [Bileam Tschepe](https://www.patreon.com/elekktronaut) and many more.

The public goal is to provide an artist friendly mappable interface for performance, a helpful dashboard and toolset while editing/composing, and classes of global plugins, generators, sources and effects that function within the system, but also as standalone elements to be intigrated into other projects. Many of the features implemented stem from a desire to hack TD itself, adding a featureset that I've always found missing in TD proper

The private goal is to codify a personal workflow, styleguide, and library for my personal projects while learning best practices for extendable, reusable tools and compositions in TouchDesigner, and creating a vehicle for sharing these items with my collaborators and community while cultivating a deeper understanding of git, python, versioning and methods of extending TouchDesigner

The name refers to a swarm of tools working together, and it might be full of bugs

___________

### Installation

Download or clone the entire repo. The .toe in the top level gets you a recent *mostly stable build of the project.  
Open it on a reasonably powerful computer. (Windows i7 / GTX 1080 eq. or better. Desktop is recommended, macintosh will have some discrepancies, if it works at all. VRAM MATTERS, 8gb+ recommended)

---

### Releases

#### 2026 stable

---

### Overview

Anyone working with TD long enough will eventually discover that resources matter, big projects are hard to maintain, preset systems brick themselves when anything changes, and UI building becomes optimization hell.

Hive aims to solve these problems by extending TD's functionality, filling  gaps in TouchDesigner's editor itself, while maintaining an

___________

### Quick Start


#### Project Outline

- Hive
	1. SETTINGS  
		*ctrl*. - accesses op.SETTINGS, a global component collecting pages of the most commonly accessed components and parameters
    2. LIB
        - core components
	        - HOTKEY MANAGER
            - PARPOPUP
            - TABLEPOPUP
            - INSPECTOR GADGET
            - SHORTCUTS
            - KEYS
                - Input Table
                - Mapper
                - Input Table
                - Mapper
            - MIDI
                - Input Table
                - Mapper
                - OutputTable
            - OSC
                - Input Table
                - Mapper
                - OutputTable
                - VSCRIPT
            - TWEENER
            - PRESETSTINGER
            - RECORD  
	            *Videosource  
	            Audiosource  
	            onSaveSnapshot
            - AUDIO
            - SYPHON
    3. SCENECHANGER
    4. GUI
    5. POST FX
    6. OUTPUT
    7. local


___

### Credits

Many thanks to the following devs and artists for their contributions, examples, inspiration, consultation and beta testing:

- [Derivative](https://derivative.ca)
- [Ivan Del Sol](https://instagram.com/spiderdelsol)
- [Darien Brito](https://darienbrito.com)
- [Roy Gerritsen](https://yfxlab.com)
- [paketa12](https://patreon.com/paketa12)
- [Alpha Moonbase](https://alphamoonbase.de/)
- [Thorne Brandt](https://thornebrandt.com)
- [Charlie Otto](https://groodmusic.com)
- [Jimmy Marco](https://instagram.com/jimmymarco.exe)
- [Reese Murdock](https://instagram.com/reese.murdock)
- [Noah Schloss](https://instagram.com/noahschloss)
- [Sahar Homami](https://instagram.com/sahar.homami)
- [Keith Lostrocco](https://intentdev.io/the-team/)
- [Bileam Tschepe](https://www.patreon.com/elekktronaut)
- [Wieland Hilker](https://alphamoonbase.de/)
- [Stefan Kraus](https://mxav.net/)
- [Markus Heckmann](https://project1.net/)
- [Lucas Morgan](https://github.com/EnviralDesign)
