"""
Extension classes enhance TouchDesigner components with python. An
extension is accessed via ext.ExtensionClassName from any operator
within the extended component. If the extension is promoted via its
Promote Extension parameter, all its attributes with capitalized names
can be accessed externally, e.g. op('yourComp').PromotedFunction().
 
Help: search "Extensions" in wiki
"""

from TDStoreTools import StorageManager
import TDFunctions as TDF
import os
from os import path

class PresetStinger:
	"""
	PresetStingExt description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		#self.Refreshpresetstable()
		self.ownerComp.par.Selectedpresetowner =  ''
		#self.ownerComp.par.Selectedpreset =  ''
		# properties
		TDF.createProperty(self, 'MyProperty', value=0, dependable=True,
						   readOnly=False)

	@property
	def PresetSting(self):
		return op('PresetStingMaster')
	@property
	def PresetsTable(self):
		return self.ownerComp.op('table_PresetStings')
	
	@property
	def PresetsTemp(self):
		return self.ownerComp.op('base_presetsTemp')
	


	def Openpreseteditor(self, owner='', preset=''):
		if owner != '':
			self.ownerComp.par.Selectedparentpath = owner.path
		if isinstance(preset, int):
			preset = owner.PresetList[preset]
		if preset != '':
			self.ownerComp.par.Selectedpreset.val = preset
		self.ownerComp.par.Selectedpresetowner = op(self.ownerComp.par.Selectedparentpath).name
		window = self.ownerComp.op('PresetStingerUI/window1')
		if window.isOpen:
			window.par.winclose.pulse()
		window.par.winopen.pulse()

		
	def Refreshpresetstable(self):
		table = self.PresetsTable
		opfind = self.ownerComp.op('opfind_PresetStings')
		opfind.par.cookpulse.pulse()
		table.clear(keepFirstRow=True)
		for r in range(1, self.ownerComp.op('sort_PresetStings').numRows):
			table.appendRow(self.ownerComp.op('sort_PresetStings').row(r))


		# if table.numRows > 1:
		# 	self.Selectedparentpath(1)
		#debug('PresetStinger PresetsTable updated')

	def Sting(self, path=''):
		#debug('test', path)
		if path == '':
			path = self.ownerComp.par.Stingpath.eval()
			
		if path != None:
			target = op(path)
			if target.findChildren(depth=1, name='PresetSting'):
			#	debug('hasSting')
				target.op('PresetSting').Addpreset()
			else:
			#	debug('else')
				pSting = target.copy(self.PresetSting, name='PresetSting')
				pSting.nodeX = TDF.findNetworkEdges(target)['positions']['right'] -150
				pSting.nodeY = - 350
				pSting.allowCooking = True
				log.Debug(f'PRESETSTINGER.Sting() | {path}')
				

		else:
			debug('no PresetStinger path specified')

	def Exportresolumefx(self, fromOp=''):
		if fromOp == '':
			fromOp = self.ownerComp.par.Stingpath.eval()

		legalStyles = ['Float', 'Int', 'Toggle', 'RGB', 'RGBA', 'File', 'Folder', 'String', 'Strmenu']
		tags = fromOp.tags
		psh = fromOp.par.parentshortcut.val
		temp = self.ownerComp.op('temp')

		# rebuild component fresh
		if temp.op(fromOp.name):
			temp.op(fromOp.name).destroy()
		newOp = temp.create(baseCOMP, fromOp.name)
		newOp.par.parentshortcut = psh

		page = fromOp.customPages[0].name
		mod.HF.CopyPars(fromOp, newOp, [page, 'config', 'Config'])

		# copy preset stings and tag info
		ops = [o for o in fromOp.findChildren(depth=1, name='^PresetSting')]
		newOp.tags = tags
		newOp.copyOPs(ops)
		try:
			newOp.op('wetDryMix').par.Drywet.mode = ParMode.CONSTANT
			newOp.op('wetDryMix').par.Drywet.val = 1
			newOp.op('switch_bypass').par.index.mode = ParMode.CONSTANT
			newOp.op('switch_bypass').par.index.val = 0
			newOp.par.Bypass.destroy()
		except Exception as e:
			debug(f"Error removing Bypass and Drywet methods: {e}")
		newChildren = newOp.findChildren(depth=1)

		exportFolder = f"{tdu.expandPath(self.ownerComp.par.Ffglresolumefx)}/{newOp.name}"

		# dictionary for normalized parameters
		normParDict = {}

		for o in newChildren:
			for p in o.pars('*'):
				if p.style == 'Float' and p.mode != ParMode.CONSTANT:
					oldExpr = None

					# --- Check bindExpr ---
					if "parent()" in str(p.bindExpr) or (psh and psh in str(p.bindExpr)):
						try:
							refPar = eval(f"op('{p.owner}').{str(p.bindExpr)}")
							if refPar.normMax > 1:
								oldExpr = str(p.bindExpr)
						except Exception as e:
							debug(f"Skipping {p} (bindExpr error: {e})")
							continue

					# --- Check expr if bindExpr didn’t qualify ---
					if not oldExpr and ("parent()" in str(p.expr) or (psh and psh in str(p.expr))):
						try:
							refPar = eval(f"op('{p.owner}').{str(p.expr)}")
							if refPar.normMax > 1:
								oldExpr = str(p.expr)
						except Exception as e:
							debug(f"Skipping {p} (expr error: {e})")
							continue

					if not oldExpr:
						continue

					# --- Safe to proceed ---
					ppar = eval(f"op('{p.owner}').{oldExpr}")
					oldDef = ppar.default
					oldMin = ppar.normMin
					oldMax = ppar.normMax
					oldVal = ppar.val

					newExpr = f"({oldExpr}) * ({oldMax} - {oldMin}) + {oldMin}"
					p.expr = newExpr
					p.mode = ParMode.EXPRESSION

					# normalize values
					normVal = (oldVal - oldMin) / float(oldMax - oldMin)
					normDef = (oldDef - oldMin) / float(oldMax - oldMin)

					ppar.normMin = 0
					ppar.normMax = 1
					ppar.default = normDef
					ppar.val = normVal

					# store info for preset normalization
					normParDict[ppar.name] = {
						'oldMin': oldMin,
						'oldMax': oldMax,
						'oldDef': oldDef,
						'oldVal': oldVal,
						'normDef': normDef,
						'normVal': normVal,
					}


		self.NormalizePresets(fromOp, newOp, normParDict, exportFolder)

		self.Stingffgl(newOp, exportFolder, normParDict)
		
		# normalize all preset tables
		

		#try:

		# clean other Pars
		# clean and normalize presets
		# export presets
		# make sure all pars are set to par.mode = ParMode.CONSTANT

	def Stingffgl(self, target='', exportFolder='', normParDict={}):
		if target == '':
			target = self.ownerComp.par.Stingpath.eval()
		if exportFolder == '':
			exportFolder = f"{tdu.expandPath(self.ownerComp.par.Ffglresolumefx)}/{target.name}"
		op.PRESETSTINGER.op('PresetPlayer').par.Folderpresets.val = exportFolder
		pSting = target.copy(op.PRESETSTINGER.op('PresetPlayer'))
		pSting.allowCooking = True
		pSting.nodeX = TDF.findNetworkEdges(target)['positions']['right'] -150
		pSting.nodeY = - 350
		run(f"op('{target}').par.Folderpresets = '{exportFolder}'", delayFrames=13)
		run(f"op('{target}').par.Time = .05", delayFrames=14)
		try:
			run(f"op('{target}').par.Input = ''", delayFrames=15)
		except:
			pass
		run(f"op('{target}').allowCooking = False", delayFrames=20)
		run(f"op('{target}').allowCooking = True", delayFrames=25)
		run(f"op('{target}').save(f'{exportFolder}/{target.name}.tox')", delayFrames=30)
		debug(f"save {target} to {exportFolder}/{target.name}.tox")

		
			
	def NormalizePresets(self, fromOp, newOp, normParDict, exportFolder):
		"""
		Update each preset DAT in newOp.PresetList to match the new normalized parameter ranges.
		"""
		oldPresetList = getattr(fromOp, 'PresetList', None)
		temp = self.ownerComp.op('base_presetsTemp')
		for pt in temp.findChildren():
			pt.destroy()
		if not oldPresetList:
			debug(f"No PresetList found in {fromOp.path}")
			return
		for p in oldPresetList:
			temp.copy(p)
		presetList = temp.findChildren(tags=['Preset'])
		if not presetList:
			debug(f"No PresetList found in {newOp.path}")
			return

		for presetTable in presetList:
			for r in range(presetTable.numRows-1, 0, -1):  # skip header
				parName = presetTable[r, 'name'].val
				if parName in ['Bypass', 'Drywet']:
					presetTable.deleteRow(r)
					continue
				if parName not in normParDict:
					continue

				info = normParDict[parName]
				oldMin = info['oldMin']
				oldMax = info['oldMax']

				# safely get numeric fields
				def _f(c):
					try:
						return float(presetTable[r, c].val)
					except:
						return None

				val     = _f('val')
				minv    = _f('min')
				maxv    = _f('max')
				default = _f('default')

				def _norm(v):
					if v is None:
						return None
					return (v - oldMin) / float(oldMax - oldMin)

				# normalized equivalents
				nVal     = _norm(val)
				nMin     = _norm(minv)
				nMax     = _norm(maxv)
				nDefault = _norm(default)

				# write normalized values back into table
				if nVal is not None:
					presetTable[r, 'val'].val = nVal
				if nDefault is not None:
					presetTable[r, 'default'].val = nDefault
				if nMin is not None:
					presetTable[r, 'min'].val = nMin
				if nMax is not None:
					presetTable[r, 'max'].val = nMax

				# normalize metadata
				presetTable[r, 'normMin'].val = 0.0
				presetTable[r, 'normMax'].val = 1.0
				debug(f"Normalized {parName} in {presetTable.name} to {nVal} {nMin} {nMax} {nDefault}")
		for pt in presetList:
			if pt.name not in ['ON', 'OFF', 'CLEAR', 'BYPASS']:
				pt.save(f'{exportFolder}/{pt.name}.tsv')

		debug(f"Preset normalization complete. Presets exported to {exportFolder}")


	def Unsting(self, target=None):
		debug(target)
		if not target:
			target = self.ownerComp
		debug(target)
		if target.par.Warningdialog:
			confirm = ui.messageBox('Delete Confirmation',
				f'Are you sure you want to remove PresetSting from \n{target}?',
				buttons=['OK', 'Cancel'])
		else:
			confirm = 0
		if confirm == 0:	
			debug()
			try:

				ui.undo.startBlock(f'Remove PresetSting from {target.path}')
				self.removeDependencies(target)

				self.removePresetsPage(target)

			#	self.removeTags(target)

			#	self.Refreshpresetstable()
				self.removePresetSting(target)
				self.removeExtensions(target.path)

				ui.undo.endBlock()	
			except Exception as e:
				debug(f'{e} \nno valid PresetSting target to destroy at {target.path}')

	def UpdatePresetSting(self, targetOp):
		targetOp.Exportallpresets(folder='local/mappings/presets/temp')
		targetOp.par.Unsting.pulse()
		run(f"op('{op.PRESETSTINGER.path}').Sting(op('{targetOp}'))", delayFrames=100)
		run(f"op('{targetOp}').Importpresetfolder(folder='local/mappings/presets/temp', dialog=False, replace=True)", delayFrames=199)


	def ReplacePresets(self, targetOp):
		debug('ReplacePresets')
		for pt in self.PresetsTemp.findChildren():
			targetOp.op('PresetSting').copy(pt)
			debug(f"put back {pn}")
		for pd in self.PresetsTemp.findChildren():
			pd.destroy()
			debug(f'destroy {pd}')
		debug(f"update PresetSting for {targetOp}")




	def removeDependencies(self, target):
		for par in TDF.getCustomPage(target, 'Dependencies').pars:
			if par.name in [p.name for p in TDF.getCustomPage(target.op('PresetSting'), 'Dependencies').pars if p.name!='Dependencies']:
				par.destroy()
	def removePresetsPage(self, target):
		TDF.getCustomPage(target, 'PRESETS').destroy()

	def removeExtensions(self, target):
		l = len(target.par.extension1.sequence)
		for r in reversed(range(1, l)):
			if target.par[f"extname{r}"].val in ['MenuSource', 'PresetSting']:
				target.par[f"extension{r}"] = ''
				target.par[f"extname{r}"] = ''
				target.par[f"promoteextension{r}"] = False

	def removeTags(self, target):
		target.tags.remove('PresetStung')

	def removePresetSting(self, target):
		debug()
		target.op('PresetSting').destroy()


#	local preset methods
	def Addpreset(self):
		op(self.ownerComp.par.Selectedpath).Addpreset()

	def Jump(self):
		op(self.ownerComp.par.Selectedpath).Jump(
			self.ownerComp.par.Selectedpreset.eval())
	def Tween(self):
		op(self.ownerComp.par.Selectedpath).Tween(
			self.ownerComp.par.Selectedpreset.eval())
	# def Duplicateselectedpresets(self):
		
	
#	export functions

	def Exportallpresetops(self, folder=''):
		ownerComp = self.ownerComp
		ppath = project.folder
		start = f"{ppath}/local/mappings/{project.name}"
		table = self.PresetsTable

	
		if folder == '':
			folder = ownerComp.par.Exportfolder
		if folder == '':
			folder = ui.chooseFolder(title='Select Folder', start=start)
		if folder != None:
			ownerComp.par.Exportfolder = folder
			if ownerComp.par.Exportfolder != '':
				if not path.exists(tdu.expandPath(ownerComp.par.Exportfolder)):
					try:
						os.makedirs(tdu.expandPath(ownerComp.par.Exportfolder))
					except Exception as e:
						debug(e)
				for r in range(1, table.numRows):
					absFolder 	= tdu.expandPath(f"{ownerComp.par.Exportfolder}/{table[r, 'name']}")
					op(table[r, 'path']).Exportallpresets(absFolder)	
			ownerComp.par.Exportfolder = ''
			debug(f"export all presets from {project.name} to {absFolder}")

	def Exportselectedpresetops(self, folder=''):
		ownerComp = self.ownerComp
		ppath = project.folder
		start = f"{ppath}/local/mappings/{project.name}"
		table = ownerComp.op('null_selected')

		if folder == '':
			folder = ownerComp.par.Exportfolder
		if folder == '':
			folder = ui.chooseFolder(title='Select Folder', start=start)
		if folder != None:
			ownerComp.par.Exportfolder = folder
			if ownerComp.par.Exportfolder != '':
				if not path.exists(tdu.expandPath(ownerComp.par.Exportfolder)):
					try:
						os.makedirs(tdu.expandPath(ownerComp.par.Exportfolder))
					except Exception as e:
						debug(e)
				for r in range(1, table.numRows):
					absFolder 	= tdu.expandPath(f"{ownerComp.par.Exportfolder}/{table[r, 'name']}")
					op(table[r, 'path']).Exportallpresets(absFolder)	
			ownerComp.par.Exportfolder = ''
			debug(f"export all presets from {project.name} to {absFolder}")

# parexec_passThru callbacks

	def onParValueChange(self, par, prev):
		"""panelexec_passThru value change callbacks to condense logic to ext"""
		if par.name == 'Test':
			debug('Test')
		else: 
			try:
				getattr(self.ownerComp, par.name)(par)
			except Exception as e:
				pass	
	def onParPulse(self, par):
		"""panelexec_passThru pulse callbacks to condense logic to ext"""
		ownerComp = self.ownerComp
		if par.name == 'Help':
			print(help(self))
		else: 
			try:
				getattr(ownerComp, par.name)()
			except Exception as e:
				pass
# end region 