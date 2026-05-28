
### HIVE

HIVE is powerful, sometimes dangerous network of global components that extend the interface and experience of creating with TouchDesigner. There's a whole swarm of em, and it might be full of bugs

#### Why I am building this:

I am building a loose family of tools, UI elements and plugins that constitute an operating system and style guide for building reusable workflows in TouchDesigner. These are adapted from my own explorations, other public user contributions, and philosophies borrowed from other media servers and vj tools such as Resolume, VDMX, Quartz Composer and Madmapper, as well as inspiration from TD power users including [Darien Brito](https://darienbrito.com/), [Richard Burns](), [Jarret Smith](https://www.linkedin.com/in/jarrett-smith-b191a461), [Wieland Hilker](https://alphamoonbase.de/), [Ivan Del Sol](https://instagram.com/spiderdelsol), [Bileam Tschepe](https://www.patreon.com/elekktronaut), * [Lucas Morgan](https://github.com/EnviralDesign)and many many more

These tools and primarily focus on areas of the the UI/UX that I've found lacking and have decided to patch around it, while helping create a standardized style guide and operating procedure for managing large projects


### GLOBAL COMPONENTS

#### LISTERUI (TABLEPOPUP) 2.5 min
- working with big DATs kind of sucks in TD
- DATs are a really nice way to store preferences, and a lot of config on Derivative's side seems to push us in this direction
- generalized a LISTER based GUI that works on any table (that has headers) bi-directionally
- localized config options are a bit overkill, but allow tables to format themselves and can be updated

_build a demo table_

new thing
#### KEYMACROS (hotkeys) 6 min
- needed a way to map my own shortcuts (ctrl.h table)
- found myself needing keyboardinCHOPS/DATS lots of places in every project, decided to centralize
- wanted ways to directly acces TDs interface and rolloverpars, gadgets, panels etc. and operate on them globally
- needed way to deactivate built in TD shortcuts non-destructively by offlining (ctrl.g table)

*map a debug statement*

#### PARPOPUP
- Generic module for a suped up floating parameter window
#### SETTINGS
- global SETTINGS compoent has pages of the most important parameters from global components in one place. 
- uses KEYMACROS common hotkey 'ctrl.,' to access top level project settings
#### INSPECTORGADGET 3 min
- a way to access what is going on in TD interface
- rolloverPars
- selectedOPs
- gadgets (panels)
- parsing Tscript was fastest way to get everything when I built it
- Accessing this DATA makes it available to call TWEENER methods via rolloverPar

#### TWEENER
- fork of Wieland's OLIB tweener module to execute timed fades between one state and another 
- has a few extra features like: 
	- fadekill 
	- global default fade time
	- startexpr and endexpr callbacks that can execute scripts synchronized with each fade

#### SCENECHANGER
- based on a fork of [Jarret Smith's](https://www.linkedin.com/in/jarrett-smith-b191a461) palette SceneChanger
- prevents anything that doesn't need to be cooking from cooking with pull based gate system
- suped up with callbacks and some template stuff to make it go
- dataGate system stores dummy data in table/constant so that connections don't break, but animation data doesn't force a cook
#### MAPPER class
- inspired by  [Darien Brito's](https://darienbrito.com/) [TDMorph](https://github.com/DarienBrito/TDMorph) mappers for KEYS, OSC and MIDI
- can work with any kind of CHOP data
- uses MapperBeacons panel in UI elements
- Global component with table based storage (can be externalized/loaded) 
- maps directly to par values anywhere in the program
- LISTERUI features make batch renaming, editing easy

#### PresetSting
- stores all preset data locally in easily backed up / imported / exported tables
- uses LISTERUI with some custom menu commands to edit and design presets
- remove missing functionality, and batch renaming makes keeping presets from breaking easy
- *enable* column allows you to operate on groups of parameters within a preset to design a performable premise

#### GUI
- GUIs are often a bottleneck in TD. building a great UI with animated parameters causes problematic observer effect issues. solutions: 
	- use paramCOMPs
	- go headless when possible
	- [Lucas Morgan's](https://github.com/EnviralDesign) UBERGUI can render many parameters into a webpage thread. My fork restores typical drag/drop functionality, adds collapsability
- manage and launch scenes
- tempo and transport bar, quick feedback from DOCK
- access Preset Dashboard and editor
- FUZZYEVAL for testing and VSCRIPT execution


#### VSCRIPT
- simple string parsing format for OSC payloads
- flag system allows for few keystrokes to control Scene, Preset, Fades and PostFX externally

#### TDAbleon wrapper
- abletonNormTime
- parse Vscript commands externally
- TDResolume controller coming soon

#### POST FX
- import/export local Fx tagged ops
- store and recall global changes to all postFX

#### OUTPUT
- single place to manage outputs
- SPOUT and NDI server