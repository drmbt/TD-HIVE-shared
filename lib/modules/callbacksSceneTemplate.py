log = mod.local_log if not hasattr(op, 'LOGGER') else op.LOGGER
 
def onInit(info):
	if parent.Scene.par.Oninit.eval():
		#op('MovieFile').par.Initinfo.pulse()
		if parent().par.Logdebug:
			log.Debug(f'onInit | Scene: {parent().name}')	
		return
		
def onStart(info):
	if parent.Scene.par.Onstart.eval():
		op('switch1').par.index = 1
		#parent().par.Reloadsrc.pulse()
		#debug(op('switch1').par.index)
		#if op('MovieFile'):
		#	op('MovieFile').par.Active = True
		#parent.Scene.par.Active = True
		#if hasattr(parent.Scene.par.Reset): parent.Scene.par.Reset.pulse()
		
		if parent().par.Logdebug:
			log.Debug(f'onStart | Scene: {parent().name}')	
		return
def onDone(info):
	if parent.Scene.par.Ondone.eval():
		if parent().par.Logdebug:
			log.Debug(f'onDone | Scene: {parent().name}')	
		return
def onExit(info):
	
	if parent.Scene.par.Onexit.eval():
		if parent.Scene.name != op.SCENECHANGER.par.Currentscenename:
			delay = (parent.Scene.par.Fadeouttime * project.cookRate)
			scriptDataGate = f"op('{parent.Scene}').op('switch1').par.index = 0"
			scriptInitData = f"op('{parent.Scene}').Initdatatable()"
			scriptPlay = f"op('{parent.Scene}').par.Play = False"
			run(scriptInitData, delayFrames = delay-1)
			run(scriptDataGate, delayFrames = delay+1)
			run(scriptPlay, delayFrames = delay+2)
			
			#r.par.camera = ""
			#r.par.geometry = ""
			#r.par.lights = ""
			#op('renderpass1').par.geometry = ''
			#op('SpaceCameraRig').par.Refrender = ''
			if parent().par.Logdebug:
				log.Debug(f'onExit | Scene: {parent().name}')	
			return 