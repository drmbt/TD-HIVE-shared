shortcut	execute	comment	delay	perform	Active
`	op.GESTURE.par.Clear.pulse()			0	1
`	op.AUDIO.op('audiofilein_metronome').par.cuepulse.pulse()			0	1
`	op.AUDIO.op('audiofilein1').par.cuepulse.pulse()			0	0
`	clear()	Clear the textport		0	1
`	op.FNS_RPLS.par.Reset.pulse()	Clear the textport		0	1
alt.,	op.PARAMETERS.Open()	Open Settings		0	1
alt.i	op.INSPECTORGADGET.openParameters()	open inspector gadget parameters		1	1
alt.r	op.INSPECTORGADGET.ParSet(val='random')	Call INSPECTORGADGET ParSet() to set rolloverPar val to a random value		1	1
alt.s 	op.SEARCHREPLACE.par.Winopen.pulse()	open SEARCHREPLACE dialog		0	0
alt.shift.v	op.INSPECTORGADGET.PasteOpAttributes()	"paste all parameters attributes from ""Copy"" op to rolloverPar.owner or selected op"		0	1
alt.v	op.INSPECTORGADGET.ParSet(val='paste')	Call INSPECTORGADGET ParSet() to set rolloverPar to ui clipboard value		0	1
ctrl.0	op.SCENECHANGER.par.Nextscene = int(op.SCENECHANGER.par.Nextscene) + 1% op.SCENES.NumScenes	PresetSting | Overwriteselectedpreset(0) to rolloverPar.owner or Current scene		0	0
ctrl.1	op.SCENECHANGER.Current.Overwriteselectedpreset(1) if not ui.rolloverPar else op(ui.rolloverPar.owner).Overwriteselectedpreset(1)	PresetSting | Overwriteselectedpreset(0) to rolloverPar.owner or Current scene		0	0
ctrl.2	op.SCENECHANGER.Current.Overwriteselectedpreset(2) if not ui.rolloverPar else op(ui.rolloverPar.owner).Overwriteselectedpreset(2)	PresetSting | Overwriteselectedpreset(0) to rolloverPar.owner or Current scene			0
ctrl.3	op.SCENECHANGER.Current.Overwriteselectedpreset(3) if not ui.rolloverPar else op(ui.rolloverPar.owner).Overwriteselectedpreset(3)	PresetSting | Overwriteselectedpreset(0) to rolloverPar.owner or Current scene			0
ctrl.4	op.SCENECHANGER.Current.Overwriteselectedpreset(4) if not ui.rolloverPar else op(ui.rolloverPar.owner).Overwriteselectedpreset(4)	PresetSting | Overwriteselectedpreset(0) to rolloverPar.owner or Current scene			0
ctrl.5	op.SCENECHANGER.Current.Overwriteselectedpreset(5) if not ui.rolloverPar else op(ui.rolloverPar.owner).Overwriteselectedpreset(5)	PresetSting | Overwriteselectedpreset(0) to rolloverPar.owner or Current scene			0
ctrl.6	op.SCENECHANGER.Current.Overwriteselectedpreset(6) if not ui.rolloverPar else op(ui.rolloverPar.owner).Overwriteselectedpreset(6)	PresetSting | Overwriteselectedpreset(0) to rolloverPar.owner or Current scene			0
ctrl.7	op.SCENECHANGER.Current.Overwriteselectedpreset(7) if not ui.rolloverPar else op(ui.rolloverPar.owner).Overwriteselectedpreset(7)	PresetSting | Overwriteselectedpreset(0) to rolloverPar.owner or Current scene			0
ctrl.8	op.SCENECHANGER.Current.Overwriteselectedpreset(8) if not ui.rolloverPar else op(ui.rolloverPar.owner).Overwriteselectedpreset(8)	PresetSting | Overwriteselectedpreset(0) to rolloverPar.owner or Current scene			0
ctrl.9	op.SCENECHANGER.Current.Overwriteselectedpreset(9) if not ui.rolloverPar else op(ui.rolloverPar.owner).Overwriteselectedpreset(9)	PresetSting | Overwriteselectedpreset(0) to rolloverPar.owner or Current scene			0
ctrl.=	op.PRESETSTINGER.Sting(ui.rolloverPar.owner)	Add PresetSting to the ownerComp of current rolloverPar			1
ctrl.`	op.TWEENER.StopAllFades()	Cancel all active TWEENER fades			1
ctrl.,	op.PARPOPUP.Open(Op=op.SETTINGS.path, Label='Global Settings')	Cancel all active TWEENER fades			1
ctrl.alt.5	op.SCENECHANGER.Current.Tween(5, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(5, time=0)	PresetSting | Tween(5, time=0) to rolloverPar.owner or Current scene			1
ctrl.alt.6	op.SCENECHANGER.Current.Tween(6, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(6, time=0)	PresetSting | Tween(6, time=0) to rolloverPar.owner or Current scene			1
ctrl.alt.7	op.SCENECHANGER.Current.Tween(7, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(7, time=0)	PresetSting | Tween(7, time=0) to rolloverPar.owner or Current scene			1
ctrl.alt.8	op.SCENECHANGER.Current.Tween(8, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(8, time=0)	PresetSting | Tween(8, time=0) to rolloverPar.owner or Current scene			1
ctrl.alt.9	op.SCENECHANGER.Current.Tween(9, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(9, time=0)	PresetSting | Tween(9, time=0) to rolloverPar.owner or Current scene			1
ctrl.alt.`	op.BROWSER.openViewer()	Open Browser			1
ctrl.alt.`	op('/local/time').frame = 1	Clear the textport		0	1
ctrl.alt.a	op.SCENECHANGER.Current.SetPresetPars(val='half', tween="tween", time=0) if not ui.rolloverPar else op.INSPECTORGADGET.PageParsSet(val='half ', tween='tween', time=0)	Call ParSet jump to random values for each par in in rolloverPar ownerComp customPage, or current Scene preset			1
ctrl.alt.b	op(f"/ui/panes/panebar/{ui.panes.current}/back/button").click()	network back			1
ctrl.alt.c	op.COLORPICKER.Openui()	"selected op path stored as ""Copy"" in parent parameters"			1
ctrl.alt.f	op(f"/ui/panes/panebar/{ui.panes.current}/forward/button").click()	network back			1
ctrl.alt.g	op.KEYMACROS.Editsysshortcuts()	Edit and override default system shortcuts/hotkeys			1
ctrl.alt.i	op.INSPECTORGADGET.openViewer(unique=False, borders=True)	Open a parameters window associated with Inspect objects			1
ctrl.alt.k	op.KEYMAPPER.Editmappings()	open KEYSMAPPER Mapping Editor			1
ctrl.alt.l	ui.panes.createFloating(type=PaneType.NETWORKEDITOR).owner = op.LIB.op('components')	Open LIB / Components working folder			1
ctrl.alt.l	op.INSPECTORGADGET.CopyAttributesToTable()	Copy OP Pars attributes to DAT table			1
ctrl.alt.m	op.MIDIMAPPER.Editmappings()	open MIDI Mappings Editor			1
ctrl.alt.m	debug()	open MIDI Mappings Editor			1
ctrl.alt.o	op.OSCMAPPER.Editmappings()	open OSC Mappings Editor			1
ctrl.alt.p	op.PRESETSTINGER.openViewer()	open PRESETSTINGER editor			1
ctrl.alt.r	op.SCENECHANGER.Current.SetPresetPars(val='random', tween="tween", time=0) if not ui.rolloverPar else op.INSPECTORGADGET.PageParsSet(val='random', tween='tween', time=0)	Call ParSet jump to random values for each par in in rolloverPar ownerComp customPage, or current Scene preset			1
ctrl.alt.s	op.SOCKETOSC.openViewer()	open KEYSMAPPER Mapping Editor			1
ctrl.alt.shift.-	op.TIME.op('time').frame = op.TIME.op('time').frame -1				1
ctrl.alt.shift.=	op.TIME.op('time').frame = op.TIME.op('time').frame +1				1
ctrl.alt.shift.h	op.KEYMACROS.Editusershortcuts()	Open KeyMacros User Shortcuts Table			1
ctrl.alt.shift.m	op.MIDIINPUTLIST.Editmidiinputlist()	Open MIDIinputList dialog			1
ctrl.alt.shift.o	op.OSC.Editinputtable()	Open MIDIinputList dialog			1
ctrl.alt.shift.r	op.RECORD.par.Arm = not op.RECORD.par.Arm	Toggle Record			1
ctrl.alt.shift.s	op.RECORD.par.Stillimage.pulse()	Take Still Image			1
ctrl.alt.t	op.TIMEEXEC.par.Edittable.pulse()	open timeline_exec table editor			1
ctrl.alt.v	op.SCENECHANGER.Current.SetPresetPars(val='paste', tween="tween", time=0) if not ui.rolloverPar else op.INSPECTORGADGET.PageParsSet(val='paste', tween='tween', time=0)	Call ParSet jump to clipboard values for each par in in rolloverPar ownerComp customPage			1
ctrl.alt.x	op.SCENECHANGER.Current.SetPresetPars(val='max', tween="tween", time=0) if not ui.rolloverPar else op.INSPECTORGADGET.PageParsSet(val='max', tween='tween', time=0)	Call ParSet jump to max values for each par in in rolloverPar ownerComp customPage, or current Scene preset			1
ctrl.h	op.TABLEPOPUP.Open(Table=op(op.INSPECTORGADGET.par.Smartselect), Default=False)	Open a Table Editor for selected tableDAT			1
ctrl.i	op.INSPECTORGADGET.par.Inspecting = op.INSPECTORGADGET.par.Smartrollover	Update 'Inspected' op with Smartrollover			1
ctrl.n	mod.HF.OpenNetwork(op(op.INSPECTORGADGET.par.Smartrollover))	open new floating network pane at  Selected operator			1
ctrl.p	op.PARPOPUP.Open(Op =op(op.INSPECTORGADGET.par.Smartselect).path, Label=op(op.INSPECTORGADGET.par.Smartselect).name)	open floating parameter window for selected op			1
ctrl.shift.a	op.SCENECHANGER.Current.SetPresetPars(val='half', tween="tween") if not ui.rolloverPar else op.INSPECTORGADGET.PageParsSet(val='half', tween='tween')	Set all customPar values in rolloverPar customPage to their default value			1
ctrl.shift.b	op(op(f"/ui/panes/panebar/{ui.panes.current}/back/button").click()	network alternate			1
ctrl.shift.c	op.INSPECTORGADGET.par.Copy = op.INSPECTORGADGET.par.Smartselect	"selected op path stored as ""Copy"" in parent parameters"			1
ctrl.shift.i	op.PARPOPUP.Open(Op=op.INSPECTORGADGET.path, label='INSPECTORGADGET',  header=False)	open inspector gadget parameters			1
ctrl.shift.k	op.KEYMAPPER.par.Learn = not op.KEYMAPPER.par.Learn	Toggle KEYSMAPPER Learn Mode			1
ctrl.shift.m	op.MIDIMAPPER.par.Learn = not op.MIDIMAPPER.par.Learn	Toggle MIDIMAPPER Learn Mode			1
ctrl.shift.o	op.OSCMAPPER.par.Learn = not op.OSCMAPPER.par.Learn	Toggle OSCMAPPER Learn Mode			1
ctrl.shift.space	op.FUZZYEVAL.par.Open.pulse()	open FUZZYEVAL window			1
ctrl.shift.t	op.TIMEEXEC.par.Active = not op.TIMEEXEC.par.Active	toggle timeline_exec Active status			1
ctrl.t	op.TABLEPOPUP.Open(Table=op(op.INSPECTORGADGET.par.Smartselect), Default=True)	Open a Table Editor for selected tableDAT			1
ctrl.u	mod.HF.Customize(op(op.INSPECTORGADGET.par.Smartselect))	open the Component Editor Dialog for current rolloverOp			1
ctrl.v	op.INSPECTORGADGET.PasteValue()	Inspector Gadget paste clipboard [Value] to rollover Par. duplicate of alt.v, don't use over network			1
ctrl.w	op(op.INSPECTORGADGET.par.Smartrollover).openViewer()	open the viewer for current smart rolloverOp			1
F1	op.SETTINGS.par.Bordersperform = False	toggle perform mode			0
F1	op('/ui/dialogs/bookmark_bar/perform/button').click()	toggle perform mode			0
F5	op.SETTINGS.par.Bordersperform = True	toggle perform mode			0
F5	op('/perform').par.winopen.pulse()				1
F6	op.COOKBAR.par.Active = not op.COOKBAR.par.Active	Toggle cook_bar probe overlay			1
F7	op.SETTINGS.par.Headless = not op.SETTINGS.par.Headless	toggle headless perform mode		1	1
F8	op.OUTPUT.par.Winopen.pulse()				1
lalt.-	op.SCENECHANGER.Current.Prevpreset(time=0)	Current Scene Prevpreset()		1	1
lalt./	op.SCENECHANGER.Current.Randompreset(time=0)	Call PresetSting Randompreset Jump on current Scene		1	1
lalt.0	op.SCENECHANGER.Current.Tween(0, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(0, time=0)	Call PresetSting Tween to preset index 0 of current/rolloverPar owner Comp		1	1
lalt.1	op.SCENECHANGER.Current.Tween(1, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(1, time=0)	Call PresetSting Tween to preset index 1 of current/rolloverPar owner Comp		1	1
lalt.2	op.SCENECHANGER.Current.Tween(2, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(2, time=0)	Call PresetSting Tween to preset index 2 of current/rolloverPar owner Comp		1	1
lalt.3	op.SCENECHANGER.Current.Tween(3, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Jump(3)	Call PresetSting Tween to preset index 3 of current/rolloverPar owner Comp		1	1
lalt.4	op.SCENECHANGER.Current.Tween(4, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(4, time=0)	Call PresetSting Tween to preset index 4 of current/rolloverPar owner Comp		1	1
lalt.5	op.SCENECHANGER.Current.Tween(5, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(5, time=0)	Call PresetSting Tween to preset index 5 of current/rolloverPar owner Comp		1	1
lalt.6	op.SCENECHANGER.Current.Tween(6, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(6, time=0)	Call PresetSting Tween to preset index 6 of current/rolloverPar owner Comp		1	1
lalt.7	op.SCENECHANGER.Current.Tween(7, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(7, time=0)	Call PresetSting Tween to preset index 7 of current/rolloverPar owner Comp		1	1
lalt.8	op.SCENECHANGER.Current.Tween(8, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(8, time=0)	Call PresetSting Tween to preset index 8 of current/rolloverPar owner Comp		1	1
lalt.9	op.SCENECHANGER.Current.Tween(9, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(9, time=0)	Call PresetSting Tween to preset index 9 of current/rolloverPar owner Comp		1	1
lalt.=	op.SCENECHANGER.Current.Nextpreset(time=0)	Call PresetSting Tween to preset prev index current/rolloverPar owner Comp		1	1
lalt.d	op.SCENECHANGER.Current.SetPresetPars(val='default', tween="tween", time=0) if not ui.rolloverPar else op.INSPECTORGADGET.ParSet(val='default')	Call ParSet jump to default values for each par in in rolloverPar ownerComp customPage			1
lalt.h	op.SCENECHANGER.Current.Tween( 'selected', time=0)	tween to most recently fired scene Preset		1	1
lalt.n	op.SCENECHANGER.Current.SetPresetPars(val='min', tween="tween", time=0) if not ui.rolloverPar else op.INSPECTORGADGET.ParSet(val='min')	Call INSPECTORGADGET ParSet() to set rolloverPar to its normMin value		1	1
lalt.r	op.SCENECHANGER.Current.SetPresetPars(val='random', tween="tween", time=0) if not ui.rolloverPar else op.INSPECTORGADGET.ParSet(val='random', tween='tween', time = 0)	Call INSPECTORGADGET to instigate TWEENER methods to interpolate a random value for ui rolloverPar		1	1
lalt.shift.-	op.SCENECHANGER.Fireprevsceneindex()	SceneChanger | Fireprevsceneindex()		1	1
lalt.shift.0	op.SCENECHANGER.SceneChange(0)	SceneChanger | Tween(9) SceneChange to TDScene index: 0		1	1
lalt.shift.1	op.SCENECHANGER.SceneChange(1)	SceneChanger | Tween(1) SceneChange to TDScene index: 1		1	1
lalt.shift.2	op.SCENECHANGER.SceneChange(2)	SceneChanger | Tween(2) SceneChange to TDScene index: 2		1	1
lalt.shift.3	op.SCENECHANGER.SceneChange(3)	SceneChanger | Tween(3) SceneChange to TDScene index: 3		1	1
lalt.shift.4	op.SCENECHANGER.SceneChange(4)	SceneChanger | Tween(4) SceneChange to TDScene index: 4		1	1
lalt.shift.5	op.SCENECHANGER.SceneChange(5)	SceneChanger | Tween(5) SceneChange to TDScene index: 5		1	1
lalt.shift.6	op.SCENECHANGER.SceneChange(7)	SceneChanger | Tween(7) SceneChange to TDScene index: 7		1	1
lalt.shift.6	op.SCENECHANGER.SceneChange(6)	SceneChanger | Tween(6) SceneChange to TDScene index: 6		1	1
lalt.shift.8	op.SCENECHANGER.SceneChange(8)	SceneChanger | Tween(9) SceneChange to TDScene index: 9		1	1
lalt.shift.9	op.SCENECHANGER.SceneChange(9)	SceneChanger | Tween(8) SceneChange to TDScene index: 8		1	1
lalt.shift.=	op.SCENECHANGER.Firenextsceneindex()	SceneChanger | Firenextsceneindex()		1	1
lalt.x	op.SCENECHANGER.Current.SetPresetPars(val='max', tween="tween", time=0) if not ui.rolloverPar else op.INSPECTORGADGET.ParSet(val='max')	Call INSPECTORGADGET ParSet() to set rolloverPar to its normMax value		1	1
lctrl.-	op.SCENECHANGER.par.Nextscene = int(op.SCENECHANGER.par.Nextscene) - 1% op.SCENES.NumScenes	Pre selected Scene		0	1
lctrl.0	op.SCENECHANGER.par.Nextscene = 0	SCENECHANGER Nextscene = 0		1	1
lctrl.1	op.SCENECHANGER.par.Nextscene = 1	SCENECHANGER Nextscene= 1		1	1
lctrl.2	op.SCENECHANGER.par.Nextscene = 2	SCENECHANGER Nextscene = 2		1	1
lctrl.3	op.SCENECHANGER.par.Nextscene = 3	SCENECHANGER Nextscene= 3		1	1
lctrl.4	op.SCENECHANGER.par.Nextscene = 4	SCENECHANGER Nextscene = 4		1	1
lctrl.5	op.SCENECHANGER.par.Nextscene = 5	SCENECHANGER Nextscene = 5		1	1
lctrl.6	op.SCENECHANGER.par.Nextscene = 6	SCENECHANGER Nextscene = 6		1	1
lctrl.7	op.SCENECHANGER.par.Nextscene = 7	SCENECHANGER Nextscene = 7		1	1
lctrl.8	op.SCENECHANGER.par.Nextscene = 8	SCENECHANGER Nextscene = 8		1	1
lctrl.9	op.SCENECHANGER.par.Nextscene = 9	SCENECHANGER Nextscene = 9		1	1
lctrl.=	op.SCENECHANGER.par.Nextscene = (int(op.SCENECHANGER.par.Nextscene) + 1)%(op.SCENES.NumScenes)	Next selected Scene		0	1
lctrl.alt.0	op.SCENECHANGER.Current.Tween(0, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(0, time=0)	PresetSting | Tween(0, time=0) to rolloverPar.owner or Current scene			1
lctrl.alt.d	op.SCENECHANGER.Current.SetPresetPars(val='default', tween="tween", time=0) if not ui.rolloverPar else op.INSPECTORGADGET.PageParsSet(val='default', tween='tween', time=0)	Call ParSet jump to default values for each par in in rolloverPar ownerComp customPage			1
lctrl.alt.n	op.SCENECHANGER.Current.SetPresetPars(val='min', tween="tween", time=0) if not ui.rolloverPar else op.INSPECTORGADGET.PageParsSet(val='min', tween='tween', time=0)	Call ParSet jump to min values for each par in in rolloverPar ownerComp customPage, or current Scene preset			1
lctrl.alt.shift.-	op.SCENECHANGER.Current.Deleteselectedpreset()	Delete Selectepreset from playing Scene		0	1
lctrl.alt.shift.=	op.SCENECHANGER.Current.Addpreset()	Add preset to playing Scene		0	1
lctrl.shift.d	op.SCENECHANGER.Current.SetPresetPars(val='default', tween="tween") if not ui.rolloverPar else op.INSPECTORGADGET.PageParsSet(val='default', tween='tween')	Set all customPar values in rolloverPar customPage to their default value else current Scene		1	1
lctrl.shift.r	op.SCENECHANGER.Current.SetPresetPars(val='random', tween="tween") if not ui.rolloverPar else op.INSPECTORGADGET.PageParsSet(val='random', tween='tween')	Call random morph on all values in rollover comp customPage else SetPresetPars on current scene		1	1
lctrl.shift.v	op.SCENECHANGER.Current.SetPresetPars(val='paste', tween="tween") if not ui.rolloverPar else op.INSPECTORGADGET.PageParsSet(val='paste', tween='tween')	Call tween to clipboard value on all values in rollover comp customPage else SetPresetPars on current scene		1	1
lshift.-	op.SCENECHANGER.Current.Prevpreset()	Tween Current Scene Prevpreset()		1	1
lshift./	op.SCENECHANGER.Current.Randompreset()	Call PresetSting Randompreset Tween on current Scene		1	1
lshift.0	op.SCENECHANGER.Current.Tween(0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(0)	Call PresetSting Tween to preset index 0 of current /olloverPar owner Comp or current Scene		1	1
lshift.1	op.TWEENER.par.Time = op.TWEENER.par.Time/2	halve tween time			0
lshift.1	op.SCENECHANGER.Current.Tween(1) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(1)	Call PresetSting Tween to preset index 1 of current /olloverPar owner Comp or current Scene		1	1
lshift.2	op.SCENECHANGER.Current.Tween(2) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(2)	Call PresetSting Tween to preset index 2 of current /olloverPar owner Comp or current Scene		1	1
lshift.3	op.SCENECHANGER.Current.Tween(3) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(3)	Call PresetSting Tween to preset index 3 of current /olloverPar owner Comp or current Scene		1	1
lshift.4	op.SCENECHANGER.Current.Tween(4) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(4)	Call PresetSting Tween to preset index 4 of current /olloverPar owner Comp or current Scene		1	1
lshift.5	op.SCENECHANGER.Current.Tween(5) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(0)	Call PresetSting Tween to preset index 5 of current /olloverPar owner Comp or current Scene		1	1
lshift.6	op.SCENECHANGER.Current.Tween(6) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(0)	Call PresetSting Tween to preset index 6 of current /olloverPar owner Comp or current Scene		1	1
lshift.7	op.SCENECHANGER.Current.Tween(7) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(0)	Call PresetSting Tween to preset index 7 of current /olloverPar owner Comp or current Scene		1	1
lshift.7	op.OSC.Editinputtable()	edit OSC input table		0	0
lshift.8	op.SCENECHANGER.Current.Tween(8) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(0)	Call PresetSting Tween to preset index 8 of current /olloverPar owner Comp or current Scene		1	1
lshift.9	op.SCENECHANGER.Current.Tween(9) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(0)	Call PresetSting Tween to preset index 9 of current /olloverPar owner Comp or current Scene		1	1
lshift.=	op.SCENECHANGER.Current.Nextpreset()	Tween Current Scene Nextpreset()		1	1
lshift.`	op.SCENECHANGER.Current.Randompreset()				1
lshift.d	op.SCENECHANGER.Current.SetPresetPars(val='default', tween="tween") if not ui.rolloverPar else op.INSPECTORGADGET.ParSet(val='default', tween="tween")	Set all customPar values in rolloverPar customPage to their default value else current Scene		1	1
lshift.h	op.SCENECHANGER.Current.Tween( 'selected', curve="lin")	tween to most recently fired scene Preset		1	1
lshift.n	op.SCENECHANGER.Current.SetPresetPars(val='min', tween="tween") if not ui.rolloverPar else op.INSPECTORGADGET.ParSet(val='min', tween='tween')	Call min morph on all values in rollover comp customPage else SetPresetPars on current scene		1	1
lshift.r	op.SCENECHANGER.Current.SetPresetPars(val='random', tween="tween", curve="lin") if not ui.rolloverPar else op.INSPECTORGADGET.ParSet(val='random', tween='tween')	Call INSPECTORGADGET to instigate TWEENER methods to interpolate a random value for ui rolloverPar		1	1
lshift.x	op.SCENECHANGER.Current.SetPresetPars(val='max', tween="tween") if not ui.rolloverPar else op.INSPECTORGADGET.ParSet(val='max', tween='tween')	Call max morph on all values in rollover comp customPage else SetPresetPars on current scene		1	1
ralt.-	op.POSTFX.Current.Prevpreset(time=0)	Current FX Prevpreset()		1	1
ralt./	op.POSTFX.Current.Randompreset(time=0)	Call PresetSting Randompreset Jump on current Fx		1	1
ralt.0	op.POSTFX.Current.Tween(0, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(0, time=0)	Call PresetSting Tween to preset index 0 of current/rolloverPar owner Comp POSTFX		1	1
ralt.1	op.POSTFX.Current.Tween(1, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(1, time=0)	Call PresetSting Tween to preset index 1 of current/rolloverPar owner Comp POSTFX		1	1
ralt.2	op.POSTFX.Current.Tween(2, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(2, time=0)	Call PresetSting Tween to preset index 2 of current/rolloverPar owner Comp POSTFX		1	1
ralt.3	op.POSTFX.Current.Tween(3, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Jump(3)	Call PresetSting Tween to preset index 3 of current/rolloverPar owner Comp POSTFX		1	1
ralt.4	op.POSTFX.Current.Tween(4, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(4, time=0)	Call PresetSting Tween to preset index 4 of current/rolloverPar owner Comp POSTFX		1	1
ralt.5	op.POSTFX.Current.Tween(5, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(5, time=0)	Call PresetSting Tween to preset index 5 of current/rolloverPar owner Comp POSTFX		1	1
ralt.6	op.POSTFX.Current.Tween(6, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(6, time=0)	Call PresetSting Tween to preset index 6 of current/rolloverPar owner Comp POSTFX		1	1
ralt.7	op.POSTFX.Current.Tween(7, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(7, time=0)	Call PresetSting Tween to preset index 7 of current/rolloverPar owner Comp POSTFX		1	1
ralt.8	op.POSTFX.Current.Tween(8, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(8, time=0)	Call PresetSting Tween to preset index 8 of current/rolloverPar owner Comp POSTFX		1	1
ralt.9	op.POSTFX.Current.Tween(9, time=0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(9, time=0)	Call PresetSting Tween to preset index 9 of current/rolloverPar owner Comp POSTFX		1	1
ralt.=	op.POSTFX.Current.Nextpreset(time=0)	Current FX Nextpreset()		1	1
ralt.`	op.POSTFX.par.Clear.pulse()	Clear Drywet for all POSTFX Fx children		1	1
ralt.d	op.POSTFX.Current.SetPresetPars(val='default', tween="jump") if not ui.rolloverPar else op.INSPECTORGADGET.ParSet(val='default', tween='jump')	Set all customPar values in rolloverPar customPage to their default value else current POSTFX		1	1
ralt.h	op.POSTFX.Current.Tween( 'selected', time=0)	jump to most recently fired FX Preset		1	1
ralt.n	op.POSTFX.Current.SetPresetPars(val='min', tween="jump") if not ui.rolloverPar else op.INSPECTORGADGET.ParSet(val='min', tween='jump')	Call min jump on all values in rollover comp customPage else SetPresetPars on current FX		1	1
ralt.r	op.POSTFX.Current.SetPresetPars(val='random', tween="jump") if not ui.rolloverPar else op.INSPECTORGADGET.ParSet(val='random', tween='tween')	Call random jump on all values in rollover par else SetPresetPars random on current FX		1	1
ralt.x	op.POSTFX.Current.SetPresetPars(val='max', tween="jump") if not ui.rolloverPar else op.INSPECTORGADGET.ParSet(val='max', tween='jump')	Call max jump on all values in rollover comp customPage else SetPresetPars on current FX		1	1
rctrl.-	op.POSTFX.par.Selectedfx = (int(op.POSTFX.par.Selectedfx) - 1)% op.POSTFX.par.Numfx	Prev selected FX		0	1
rctrl.0	op.POSTFX.par.Selectedfx = 0	Selected Fx = 0		1	1
rctrl.1	op.POSTFX.par.Selectedfx = 1	Selected Fx = 1		1	1
rctrl.2	op.POSTFX.par.Selectedfx = 2	Selected Fx = 2		1	1
rctrl.3	op.POSTFX.par.Selectedfx = 3	Selected Fx = 3		1	1
rctrl.4	op.POSTFX.par.Selectedfx = 4	Selected Fx = 4		1	1
rctrl.5	op.POSTFX.par.Selectedfx = 5	Selected Fx = 5		1	1
rctrl.6	op.POSTFX.par.Selectedfx = 6	Selected Fx = 6		1	1
rctrl.7	op.POSTFX.par.Selectedfx = 7	Selected Fx = 7		1	1
rctrl.8	op.POSTFX.par.Selectedfx = 8	Selected Fx = 8		1	1
rctrl.9	op.POSTFX.par.Selectedfx = 9	Selected Fx = 9		1	1
rctrl.=	op.POSTFX.par.Selectedfx = (int(op.POSTFX.par.Selectedfx) + 1)% op.POSTFX.par.Numfx	Next selected FX		0	1
rctrl.alt.shift.-	op.POSTFX.Current.Deleteselectedpreset()	Delete Selectepreset from selected FX		0	1
rctrl.alt.shift.=	op.POSTFX.Current.Addpreset()	Add preset to selected POSTFX		0	1
rctrl.b	op.POSTFX.Current.par.Bypass = not op.POSTFX.Current.par.Bypass 	Selected Fx = 9		1	1
rshift./	op.POSTFX.Current.Randompreset()	Call PresetSting Randompreset Tween on current Fx		1	1
rshift.0	op.POSTFX.Current.Tween(0) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(0)	Call PresetSting Tween to preset index 0 of current /olloverPar owner Comp or current FX		1	1
rshift.1	op.POSTFX.Current.Tween(1) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(1)	Call PresetSting Tween to preset index 1 of current /olloverPar owner Comp or current FX		1	1
rshift.2	op.POSTFX.Current.Tween(2) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(2)	Call PresetSting Tween to preset index 2 of current /olloverPar owner Comp or current POSTFX		1	1
rshift.3	op.POSTFX.Current.Tween(3) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(3)	Call PresetSting Tween to preset index 3 of current /olloverPar owner Comp or current POSTFX		1	1
rshift.4	op.POSTFX.Current.Tween(4) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(4)	Call PresetSting Tween to preset index 4 of current /olloverPar owner Comp or current POSTFX		1	1
rshift.5	op.POSTFX.Current.Tween(5) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(0)	Call PresetSting Tween to preset index 5 of current /olloverPar owner Comp or current POSTFX		1	1
rshift.6	op.POSTFX.Current.Tween(6) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(0)	Call PresetSting Tween to preset index 6 of current /olloverPar owner Comp or current FX		1	1
rshift.7	op.POSTFX.Current.Tween(7) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(0)	Call PresetSting Tween to preset index 7 of current /olloverPar owner Comp or current POSTFX		1	1
rshift.8	op.POSTFX.Current.Tween(8) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(0)	Call PresetSting Tween to preset index 8 of current /olloverPar owner Comp or current POSTFX		1	1
rshift.9	op.POSTFX.Current.Tween(9) if not ui.rolloverPar else op(ui.rolloverPar.owner).Tween(0)	Call PresetSting Tween to preset index 9 of current /olloverPar owner Comp or current POSTFX		1	1
rshift.d	op.POSTFX.Current.SetPresetPars(val='default', tween="tween") if not ui.rolloverPar else op.INSPECTORGADGET.ParSet(val='default', tween='tween')	Morph all customPar values in rolloverPar customPage to their default value else current POSTFX		1	1
rshift.n	op.POSTFX.Current.SetPresetPars(val='min', tween="tween") if not ui.rolloverPar else op.INSPECTORGADGET.ParSet(val='min', tween='tween')	Call min morph on all values in rollover comp customPage else SetPresetPars on current FX		1	1
rshift.r	op.POSTFX.Current.SetPresetPars(val='random', tween="tween") if not ui.rolloverPar else op.INSPECTORGADGET.ParSet(val='random', tween='tween')	Call random morph on all values in rollover par else SetPresetPars random on current FX		1	1
rshift.x	op.POSTFX.Current.SetPresetPars(val='max', tween="tween") if not ui.rolloverPar else op.INSPECTORGADGET.ParSet(val='max', tween='tween')	Call max morph on all values in rollover comp customPage else SetPresetPars on current FX		1	1
shift.alt.i	op.ICONSTINGER.Sting(op(op.INSPECTORGADGET.par.Smartselect), op(op.INSPECTORGADGET.par.Smartselect))	Sting selected COMP with an Icon			0
shift.alt.o	op.OSC.Editoutputtable()	Edit OSC output table			1
shift.b	op.INSPECTORGADGET.BindRolloverPar()	bind rolloverPar to new parent() customPar			1
shift.d	op.INSPECTORGADGET.ParSet(val='default', tween='tween')	Call INSPECTORGADGET to instigate TWEENER methods to interpolateto the default value for ui rolloverPar			0
shift.down	op('/ui/dialogs/timeline/transport/reset/button').click()	restart timelime			1
shift.e	op.INSPECTORGADGET.RefRolloverPar()	Create reference from rolloverPar to new parent() customPar			1
shift.v	op.INSPECTORGADGET.ParSet(val='paste', tween='tween', time=op.TWEENER.par.Time.eval())	Call INSPECTORGADGET to instigate TWEENER methods to interpolateto the clipboard value for ui rolloverPar			1
shift.x	op.INSPECTORGADGET.ParSet(val='max', tween='tween')	Call INSPECTORGADGET to instigate TWEENER methods to interpolateto the normMax value for ui rolloverPar			1
