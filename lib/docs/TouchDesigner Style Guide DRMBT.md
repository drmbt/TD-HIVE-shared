# TouchDesigner Style Guide DRMBT  

This style guide represents the evolution of how I try to organize 
my projects in TouchDesigner. It is in no way comprehensive, nor  
do I guarantee my projects conform perfectly to these standards;  
it is a WIP meant to help me codify my everchanging concept of  
best practice for TD and Python  

For the sake of cleanliness, consistency, and legibility,  
it behooves us to create in TouchDesigner with a sense of deliberacy.  

Let's sync up on our approach to naming, styles, and best practices  
I've tried to use these conventions in an illustrative way below  
   
---

### Naming Conventions

__operator__ names should be lowercase by default, formatted as `{'optype'}_{'opname'}`.  
Ops that are intermediary can be left to their default names, but those that    
are referenced or customized should be renamed with a camelCase descriptor

_example: constant_layer1, noise_colorMap, videodevin_webcam, null_bg etc_

exceptions: It is common in TD parlance to sometimes skip the optype prefix, and just use a name like _instances_ , _bg_ etc. if its the only one of its type in a network. I try to avoid this, opting for the more verbose name because it feels more typed, and a growing network may eventually have both a _top_intstances_ and a _chop_instances_ for example, and i want to be able to reference them by name explicitly without having to think too much about what I am referencing, but this is a personal preference.

I am also rarely providing an optype prefix for base or componentCOMPs, choosing instead to name descriptively, following the below CAPSCASE conventions if it is to be a globally referenced operator, or PascalCase for components that will have a parent shortcut reference only

---

### ParentShortcuts

COMPs with a parent shortcut should be PascalCase, as are their parent Shortcuts.  
These do not require a prepended OPType.

_example: Gui, ContainerPanels, Geo, Modules, ScenesDefault etc_

COMP names that don't require a ParentShortcut may be formatted as camelCase


_example: opSnippets, extMovies, textureToolkit etc_

Lately I've been avoiding global shortcuts when referencing COMPS that act as folders,   
opting for references to inherit from a ParentShortcut such as `op.Project.op('Library')`

---

### GLOBALSHORTCUTS  

COMPs with GLOBALSHORTCUTS should be avoided when possible, 
only employed when its the kind of tool that only makes sense to exist
once per project.

When one does choose to employ global shortcuts, these COMPs get an 
all cap treatment for both name and shortcut value.  

These nodes should be single word values, and only live within  
the top two levels of your project, or explicit folders for such tools

Common uses for GLOBALSHORTCUTS are FOLDERS and reusable 
global COMPONENTS or TOXES such as LOGGER, HEARTBEAT, POPUPMENU etc.  
that function as callable modules, not unlike TDU or TDF

_example: ASSETS, LIB, DATA, OUTPUT, KEYSMAPPER, MIDI, AUDIO etc_

or for singleton locations in your project like _SCENES_, _OUTPUT_, _POSTFX_ etc. 

---

### ReplicatedOPs

If an item requires replication or is dynamically generated,
the MASTER should have an index of 0 and   
the first active operator should be 1. 

An exception is if the master needs to reference a table with `me.digits`, 
in which case sometimes an index of 1 makes sense to avoid unnecessary 
duplication of work.

I like to label MASTER loudly with caps to catch the eye quickly

_examples: ContainerMASTER0, Container1, Container2 etc_

In this scenario, the MASTER op should be inactive, and its display flag off.

In the case that the MASTER op is active,  
it should start with `{op}[1 based index]`,  and  
there is no need to indicate in the name that it is the master

_example: syphonspoutin1, syphonspoutin2, syphonspoutin3 etc_

---

### OPFAMILY

when referring to an OP family, it should be all caps

_example: DAT, TOP, COMP etc_


### OPType

whereas if you are referring to a specific OPType, the family is capitalized  
while the type is lowercased

example: fieldCOMP, rectangleTOP, stretchCHOP

---

## Code

Aim for 80 chars max per line of code before line breaks in your statements  
This isn't hard and fast, just ideal. I tend to fudge this rule when word wrap 
does it automatically, but it looks a lot cleaner in vanilla text editors if you follow it.

I also try to conform to Markdown conventions wherever possible when writing text
and can't recommend Obsidian enough for managing .README , docs, wiki etc.

---

### comments

    # Whenever possible, operations that aren't immediately obvious should
    # be stepped through in plain english at the beginning of an operation

In 2026, LLMs oftne write these, and although they tend to be a bit heavy handed, 
too much documentation is arguably better than non at all. 

My preference is for short helper text in functions that are public and not immediately 
self explanatory, and if working with LLM agents, prodding them to avoid being overly
verbose is probably a good idea

---

### extCode

Extension code should be externalized and synced to a system folder  
and named in a PamelCase format with 'Ext' appended  
I use project.folder/lib/modules for a dedicated home for this code
in projects with a global modules folder. 

_example: IconExt PresetStingExt, MoviePlayerExt, extMediaLister_

_note_: this is a break from my original styling, in which i prepended extMyExtension, 
which i found makes it tougher to search for alphabetically. 
There may be some old extensions floating around my projects that still conform to 
this convention.

---

### Methods

as per TD standards, promoted methods are PascalCase and  
methods hidden from the user are camelCase. 

This is a TD styling that breaks from python snake_case conventions, 
and is a personal preference to follow how Derivative chooses to style
	things as opposed to what might be more pythonic

_example:_   `def Inspect(self):`, `def privateMethod(self):`

---

### Classes

Classes are PascalCase, or camelCase prepended with ext to denote an  
externalized extension module

_example:_ `class ContainerPanelExt`

---

### @Properties 

@Properties are often used for attributes of a component that require a setter, or 
are referenced internally or externally in the extension. 

_example: @Table, @Targetop_ etc. 

---

### GLSL

any shadercode should be externalized to your project folder and synced if it  
is anything more then the simplest of operations. It should live in the same  
folder as your other source dependencies, unless its a particularly GLSL heavy  
project in which case a dedicated GLSL folder can be created at your discretion  

---

# Node best practices

## nulls

Add a null anytime you are creating a reference, branching to a parallel process,   
or terminating a network. These should be described in camelCase and   
prepended with 'null_' when renamed. When splitting to branches the  
default naming is fine, but when referenced pythonically, they get a custom name

_example: null_bg, null_instances, null_preFx, null_depthMap, null_normalize etc_  

### null_bg

at the end of a TOP network, the penultimate node should be null_bg followed by    
the default out1 if there is only one output in the network, and out_{label} if   
there are multiple outs. {label} should be camelCase. If there are more then     
one out best described by the same name, we can format as out_{label}{index}  

_example: out1, out_overlay, out_specular, out_scene2, outDAT, out_instanceData_   

This gives us a dependable reference of op('MyOp').op('out1') or    
op('MyOp').op('null_bg') that we can reference in our network. My preference is   
to use the former for selecting paths, and the latter for setting the bgOp for  
COMPs and panels that don't have their own icon.   

### null cooking

Nulls should only be changed from automatic cooking to selective when a static  
value is causing its reference to cook continuously. Setting a null to always  
cook should only be done as a bandaid when data fails to update outside of a  
network under default auto cooking operation


---

### placement

UI items should be arranged via me.nodeX for horizontally aligned items, and  
-me.nodeY for those arranged vertically. When created dynamically, nodes should  
be created at unity origin, offset by 150 * me.digits either horizontally or  
vertically at the users discretion.   

Lately I've been experimenting with seperating the 4 quadrants of a network   
around [0, 0] based on functionality, with extensions and code in the upperl,  
data and input sources in lowerl, rendering and compositing in upperr and data  
and processing in the lowerr quadrant  

whenever possible, aim for consistent sizing, alignment, and networks that read  
cleanly from left to right. If there are parallel branches doing similar things  
leave room to align similar stages above each other for visual cohesion and legibility

---

## Components

Any process that can be broken down into a single extendable function should  
get a feature complete COMP with its own class created and externalized for   
future use. Often when developing, this step can happen during the cleanup/  
optimization stages, or even post project completion, although there are  
benefits to kicking these out throughout a dev process, not the least of which  
is being able to reuse them elsewhere in the project where applicable 

Whenever possible, any component with logic or state information should have  
its own Class and extEnsion, with information passed to it via par and panel  
execDATs. I prefer to keep any promoted storage that a user might want access  
to or feedback from stored as a customPar, with other storage in properties,  
tdu storage manager, and unpromoted methods. Information that should only be  
feedback for the user should be set to read only

Comps such as filters or fx that require an input should also have an in par  
referenced by a select, and wired to the second input of the inTOP. This allows  
an agnostic workflow where wires or selects are both equally viable  

COMPs with many named outputs such as tables or texture maps that are meant  
for extension/reuse/recyclability shoud get an Ops customPars page with  
references to the named operators stored as parameters of the object  

Although an externalized tox could be as simple as an empty base, I consider  
a feature complete COMP as meeting some or all of the following criteria:  

- CustomName
- ParentShortcut
- GLOBALSHORTCUT (if meant to be accessible from anywhere in the project)
- relevant ins if it can accept a signal (with selectPar as second input)
- relevant outs if it can output anything
- relevant customPars Ops page for named outputs
- relevant common scripts from above list (ie drop, runCmd, extEnsion, parexec1) 
- null_bg as penultimate TOP if TOP network
- readme, help, comments, tags where applicable
- icon when relevent (see icon rules below)
- published customPars for anything that a user should have access to(see below)

---

## Parameters
If a parameter is to be accessed by the end user, it should be passed through  
a custom parameter to denote that its public

This practice allows auto GUI generation, and preset systems to filter by  
customPars, and allows built-in pars to be filtered from parameter pages

---

### Customparameters

Customparameters get a Singlecapital letter on the front end of the name, as  
per TouchDesigners default convention (built in pars are always lowercase). We  
will expose user accessible parameters here, as well as pulses for common  
methods, resetpulse() and reloadpulse() type messages, common Names, Labels,   
Paths and other strings, and when applicable, metadata such as Artist, Url,   
Version, Resolution(wh), Framerate etc. A robust tox may Promote pars such as  
menus, pixelformat, interpolation or style settings, or any other parameter   
that you might anticipate wanting external/GUI control over, or access to via  
preset systems and similar storage mechanisms.  

While Parameternames must be a single Capitalizedword, Parameter Labels (info)  
should be cleanly read english with spaces and capitilazation of each discrete  
word, with parenthesis to delineate other information such as (unit).   

If a COMP has exactly two states, a toggle will suffice for storing this data,  
i.e. an Active switch. When states > 2, a menu for the named states is   
preferable, accessed by either name or index.  

---
### selects

Whenever possible, both selects and COMPinputs should be available as an option  
to get information into a COMP. 

Inside of a network, selects should be used to maintain nodal tidiness  
if a cluster of wires is becoming difficult to maintain or to delineate  
discrete functionality in a different part of the same network   

---
### binding

Expression Binding (non bindCHOP) should only be used when driving a customPar  
from a GUI element or external controller. This should be done in such a way as  
to keep the Custompar the bindMaster, so that if the UI were to be completely   
removed from the project, the functionality of any process it was driving   
remains completely functional, and no errors result from missing dependencies  

---


### reference

All major references should happen via python expressions. These days the  
performance between refs and exports is pretty negligable, and python offers  
the ability to further process the expression in-line.  

Best practice for probably to reference a parCHOP from within your network  
although more often then not, I find myself directly referencing parent().pars  
or pushing values from Custompars via parexec>extension Method > local.par  

A COMP should never affect functionality inside another COMP, but should be  
limited to affecting change at the parent Parameter and Methods level  

---

### export

I'm pretty much never ever using exports these days, except for when passing  
dynamic data to GLSL. References are just as fast, with more flexibility for  
processing/massaging the data in-line. One situation where exports could be   
desirable is in situations where multiple channels of CHOP data need to be  
disabled at once with the export flag. Another is when you have a single   
channel of CHOP data that has a dynamic name, in which case the export doesn't  
break where the expression does. I'm still more likely to use a chop referring  
to index in this situation

---

### tags

tags are a useful way to create custom filters or flags for finding ops and   
COMPs throughout your network, or to associate meta information about style or  
content with an operator. Because at the time of this writing there is not yet  
a GitDiffable format for TD, tags should be used sparingly for major  
functionality. Lately I'll prefer storing filter information in a   
ParentShortcut for filtering or opFinding, as opposed to tagging with that same  
information, but there are times when a tag is the best identifier for a class  
of operator that you need to find dispersed throughout a network  

My most common usecase for a tag is when it becomes necessary to create smart  
filtered lists that might have many descriptive qualities. The ability to sort  
by keyword becomes more necessary as a library of components grows. Tags I find  
useful may include broad descriptors, fx, styles or tropes such as:  

_blue, UI, filter, geo, lofi, ultrawide, 80s, b&w, fluid, texture, still, fx etc_

---

### comments

This oft neglected field should never be functional, but if there is relevant  
data or instructions that are associated with the operator, it can be left here  
For readability I prefer help or readme files in the tox, but if it must be  
accessible from the op object itself, a good practice might be to double it.  
Common comments might be descriptors of a mood, common parameters to tweak  
key center information for audio files, or other descriptive plain english  
that may be valuable to store with the file

---

### thumbnail icons

COMPs that are tools or modules, or containers representing an effect or ext  
file should get a locked null named 'icon' that can be loaded quitely into the  
preview panel of the palette browser. 

Best practice is to disable the viewer for ops that aren't providing  
essential pieces of visual feedback while working in your network.  
I typically do this last, during optimization passes  before a project deploys

---

### Font Considerations

Finding fonts that will consistently render cross platform, are distributable,  
and scale well is tricky. For this reason, Arial and Open Sans are your friends

### UI Icons
I'm a big fan of using [Material Design Icons](https://docs.derivative.ca/Widgets#Adding_Material_Design_Icons) from Google for reliable UI Icons


---

### Color  

I don't use much color coding in my projects, but when diverging from below,    
I like to indicate my key in a top level style guide or readme  

- <span style="color:red">*red*</span>  - functional code, script/extension, important shit  
- <span style="color:grey">*black*</span>  - externalized TOX 
- <span style="color:violet">*violet*</span>  - delineate DAT as mutable
- <span style="color:orange">*orange*</span> - Base full o' code for cleanliness
- <span style="color:yellow">*yellow*</span>. - misc highlighter for an op of interest within a network  
- <span style="color:lightblue">some *blue* </span> - readme, license, accreditation




