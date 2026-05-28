
## Resources

[workshop repository](https://github.com/drmbt/TD-HIVE-shared)
[TD Launcher](https://github.com/function-store/TD-Launcher-Plus)
[[TouchDesigner Style Guide DRMBT]]
[Shutter Encoder](https://www.shutterencoder.com/)

## Intros
- name
- TD experience level
- interests (visuals, VJ, interaction design, music, commercial, projection mapping etc.)
- how long have you been using TD
- MAC / PC
- Do you python at all?
- are you familiar / comfortable using github?

## Setup

- download resources if you haven't already, if only one, grab the [workshop repository](https://github.com/drmbt/TD-HIVE-shared)
## Intro to HIVE

## Custom Parameters
- using Custom Parameters to publish control and build simple UI
	- parameters COMP, CHOP, DAT
	- palette (user)
		- [TD Search-Palette](https://github.com/yeataro/TD-SearchPalette/releases)
		- git practices
		- symlinks
			- Mac https://github.com/nickzman/symboliclinker
			- https://github.com/ololx/create-symlink/
			- Windows https://schinagl.priv.at/nt/hardlinkshellext/linkshellextension.html
## Scalable GUI
- container vs base
	- container has panel
	- panel attributes
- bg top vs op viewer
- stretch, fill, fit best, fit outside (confusing nomenclature in comp vs top)
- understanding children alignment
- fixed, fill, anchor
- dynamic reordering from network position
- draggable edges

## Cook Optimization
- pull based cooking in TD
- no no chops (Logic, trigger, lag, filter) 
	- [optimeister](https://github.com/dylanroscover/TDComponents) 
- [cookbar](https://forum.derivative.ca/t/cook-bar-cook-times-visualized/7541/7)
- selective cooking
- GPU optimized media (HAP)
	- convert media formats to HAP with [Shutter Encoder](https://www.shutterencoder.com/)

# Stretch Goals

### Tags
- opfind and tags
- DATASOURCE components
	- datasource
	- audiosource
	- videosource
### Logging
- LOGGER
- `log = op.TDResources.op('TDAppLogger')if not hasattr(op, 'LOGGER') else op.LOGGER`
	- portability when using dependencies

