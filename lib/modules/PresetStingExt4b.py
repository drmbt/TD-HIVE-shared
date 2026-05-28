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
log = op.TDResources.op('TDAppLogger')if not hasattr(op, 'LOGGER') else op.LOGGER
class PresetStingExt:
	"""
	presetStingExt description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		
		self.UpdateNumPresets()
		self.tweenList = ['Float', 'Int', 'Toggle', 'RGB', 'RGBA', 'UV', 'UVW', 'WH', 'XY', 'XYZ']
		
		# properties
		TDF.createProperty(self, 'MyProperty', value=0, dependable=True,
						   readOnly=False)
	@property
	def PresetHeader(self):
		items = 'Missing', 'label', 'name', 'path',  'val', 'expr',  'mode', 'time', 'delay', 'type', 'curve',\
			 'page', 'default','min', 'max', 'normMin', 'normMax', 'clampMin', \
			'clampMax', 'enable', 'enableExpr', 'help', 'startSection', 'style', \
			  'menuNames', 'menuLabels', 'menuSource'
		return items
	@property
	def UpdateItems(self):
		items = ['name', 'label', 'val', 'default', 'min', 'max', 
				'normMin', 'norMax', 'clampMin', 'clampMax', 'enable', 
				'enableExpr', 'help', 'style', 'page', 'mode', 'expr', 
				'bindExpr', 'menuNames', 'menuLabels', 'menuSource']
				
		return items

	@property
	def PageBlackList(self):
		'''ignore list for common pages that never get presets'''
		common = [
		'About', 'Info', 'SceneSettings', 'config', 'Config' 'Callbacks', 'callbacks'
		'Presets', 'PresetsHidden', 'Test', 'Sting', 'PRESETS', 'Dependencies', 
		'debug', 'Debug'
		]
		pbl = str(self.ownerComp.par.Pageblacklist.eval()).split(' ')
		if pbl != ['']: 
			common = common + pbl 
		return common

	@property
	def Name(self):
		""" return the name of the ownerComp"""
		return self.ownerComp.name

	@property
	def FxList(self):
		fxList = op(self.ownerComp.par.Operators).findChildren(type=COMP, tags=['Fx'])
		return fxList

	@property	
	def PresetList(self):
		presetList = [op(p) for p in self.ownerComp.op('PresetSting/menu').col('path')[1:]]
		return presetList
	@property
	def PresetNames(self):
		namesList = [p.name for p in self.PresetList]
		return namesList
	@property
	def Operators(self):
		""" return the list of included operators"""
		Ops = self.ownerComp.par.Operators.evalOPs()
		opList = [o for o in Ops]
		fxList = []
		if self.ownerComp.par.Includetaggedfx.eval():
			for OP in opList:
				for x in OP.findChildren(type=COMP, tags=['Fx']):
					fxList.append(x)			
		opsList = opList + fxList	
		return opsList
	@property
	def selectedPreset(self):
		return self.ownerComp.par.Selectedpreset.eval()
	@selectedPreset.setter
	def selectedPreset(self, v):
		self.ownerComp.par.Selectedpreset = v
	@property
	def NumPresets(self):
		return self.ownerComp.par.Numpresets.eval()
	@NumPresets.setter
	def NumPresets(self, v):
		self.ownerComp.par.Numpresets = v

	@property
	def recentPreset(self):
		return self.ownerComp.par.Recentpreset.eval()
		
	@recentPreset.setter
	def recentPreset(self, v):
		self.ownerComp.par.Recentpreset = v
		return

	@property
	def PageScope(self):
		blackList = self.PageBlackList
		pageScope = str(self.ownerComp.par.Pagescope.eval()).split(' ')
		if pageScope == [''] or pageScope == ['*']:
			pageScope = []
			for OP in self.Operators:
				for x in OP.customPages:
					if x not in blackList:
						pageScope.append(x)				
		return pageScope
	
	@property
	def ParBlackList(self):
		return str(self.ownerComp.par.Parblacklist.eval()).split(' ')

	@property
	def ParScope(self):
		blackList = self.ParBlackList
		pars = str(self.ownerComp.par.Parscope.eval()).split(' ')
		parScope = []
		if pars == [''] or pars == ['*']:	
			for OP in self.Operators:
				for x in OP.customPars:
					if x.name not in blackList:
						if x.page in self.PageScope:
							parScope.append(x)
		else:
			parScope = []
			for OP in self.Operators:
				for x in OP.customPars:
					if x.name in pars:
						if x.page in self.PageScope:
							parScope.append(x)

		return parScope
	@property
	def MenuTable(self):
		return self.ownerComp.op('PresetSting/menu')

	def CreatePresetTable(self, name=''):
		ownerComp = self.ownerComp
		if name == '':
			name = ownerComp.par.Name
		if not name:
			name = ownerComp.par.Name.default
		newTable = ownerComp.op('PresetSting').create(tableDAT, tdu.legalName(name))
		op(newTable).nodeY = self.NumPresets * -100
		op(newTable).replaceRow(0, self.PresetHeader, entireRow=True)	
		op(newTable).cloneImmune = True	
		self.WritePreset(op(newTable))
		op(newTable).tags = {'Preset'}
		if self.ownerComp.par.Logdebug:
			log.Info(f"PresetSting	| Create new Preset: '{name}'")
	def CreateDefaultPreset(self):
		ownerComp = self.ownerComp
		name = 'default'
		if ownerComp.op(f"PresetSting/{name}"): ownerComp.op(f"PresetSting/{name}").destroy()
		newTable = ownerComp.op('PresetSting').create(tableDAT, name)
		op(newTable).nodeY = self.NumPresets * -100
		op(newTable).replaceRow(0, self.PresetHeader, entireRow=True)	
		op(newTable).cloneImmune = True	
		self.WritePreset(op(newTable), default=True)
		op(newTable).tags = {'Preset'}
		self.ownerComp.cook(force=True)

	def AddParameters(self, preset='', pars=['']):	
		tweenList = self.tweenList
		if preset != '':
			self.selectedPreset = preset
		if type(pars) != list: pars= [pars]
		selected = self.ownerComp.op(f"PresetSting/{self.selectedPreset}")
		for par in pars:
			if isinstance(par, Par):
				if par.page not in self.PageBlackList:
					v = par.val
					
					op(preset).appendRow([	
						0,
						par.label,
						par.name,
						par.owner.path,							
						par.val,
						str(par.bindExpr).replace('\'', '"') if par.mode == ParMode.BIND else str(par.expr).replace('\'', '"'),
						str(par.mode).strip('ParMode.'),
						"",
						"",
						'absolute' if par.style in tweenList and str(par.mode).strip('ParMode.') == 'CONSTANT' else 'startsnap',
						's' if par.style in tweenList else '',
						par.page,
						par.default,
						par.min,
						par.max if par.style != 'Menu' else len(par.menuNames),
						par.normMin,
						par.normMax if par.style != 'Menu' else len(par.menuNames),	
						par.clampMin,
						par.clampMax,
						par.enable,
						'' if par.enableExpr == None else par.enableExpr,
						par.help,
						par.startSection,
						par.style,
						'' if par.style not in ['Menu', 'StrMenu'] else par.menuNames,
						'' if par.style not in ['Menu', 'StrMenu'] else par.menuLabels,
						'' if par.style not in ['Menu', 'StrMenu'] else par.menuSource,
					])	
		return


	def WritePreset(self, preset='', default=False):
		"""
		Write a new preset tableDAT from supplied criterion. 
		Pattern matching not currently supported, but * or '' return all
		"""
		if preset =='':
			preset = self.selectedPreset
		parsScope = self.ParScope
		tweenList = self.tweenList
		for par in parsScope:
			op(preset).appendRow([	
				0,
				par.label,
				par.name,
				self.Operators[0].relativePath(par.owner),							
				par.val if not default else par.default,
				str(par.bindExpr).replace('\'', '"') if par.mode == ParMode.BIND else str(par.expr).replace('\'', '"'),
				str(par.mode).strip('ParMode.'),
				"",
				"",
				'absolute' if par.style in tweenList and str(par.mode).strip('ParMode.') == 'CONSTANT' else 'startsnap',
				's' if par.style in tweenList else '',
				par.page,
				par.default,
				par.min,
				par.max if par.style != 'Menu' else len(par.menuNames),
				par.normMin,
				par.normMax if par.style != 'Menu' else len(par.menuNames),	
				par.clampMin,
				par.clampMax,
				par.enable,
				'' if par.enableExpr == None else par.enableExpr,
				par.help,
				par.startSection,
				par.style,
				'' if par.style not in ['Menu', 'StrMenu'] else par.menuNames,
				'' if par.style not in ['Menu', 'StrMenu'] else par.menuLabels,
				'' if par.style not in ['Menu', 'StrMenu'] else par.menuSource,
			])	
		self.UpdateNumPresets()
		


	def Overwriteselectedpreset(self, preset=''):

		if preset != '':
			self.selectedPreset = preset
		
		op(self.selectedPreset).clear(keepFirstRow=True)
		self.WritePreset(self.selectedPreset)	
		if self.ownerComp.par.Logdebug:
			log.Info(f"PresetSting	| overwrite: {self.selectedPreset} ")
	def Updatemenu(self):
		self.ownerComp.UpdateMenu()

	def Updateselectedpreset(self, preset=''):
		### To Do: doesn't always update Tagged Fx
		if preset != '':
			self.selectedPreset = preset
		parScope = self.ParScope
		parsList = [x.name for x in self.ParScope]
		presetOp = op(self.selectedPreset)
		tweenList = ['Float', 'Int', 'Toggle', 'RGB', 'RGBA', 'UV', 'UVW', 'WH', 'XY', 'XYZ']
		valList = self.UpdateItems
		labelList = [label.val for label in op(self.selectedPreset).row(0)]

		for par in parScope:
			if par.name in parsList and par.page in self.PageScope:
				if par.name in [c.val for c in op(self.selectedPreset).col('name')]:
					for item in valList:
						if item in labelList:
							row = presetOp.findCell(par.name, cols=['name']).row
							script = f"op('{presetOp}')[{row}, '{item}'] = op('{par.owner}').par['{par.name}'].{item}"
							run(script)

		for c in presetOp.col('mode'):
			if 'ParMode.' in c.val:
				presetOp[c.row, 'mode'] =  c.val.split('.')[1]
		self.Removemissing()
		self.UpdateNumPresets()	
		if self.ownerComp.par.Logdebug:
			log.Info(f"PresetSting	| Update Preset: {self.selectedPreset}")

#	preset execution

	def Removemissing(self, table=None):
		if table == None: table = op(self.ownerComp).op(f'PresetSting/{self.selectedPreset}')
		if 'Missing' in table.row(0):
			rowList = [c.row for c in table.col('Missing') if c== 1]
			if rowList:
				ui.undo.startBlock(f'undo clear missing from {table}')
				table.deleteRows(rowList)
				ui.undo.endBlock()
				if self.ownerComp.par.Logdebug:
					log.Info(f"PresetSting	| Remove Missing Preset: {self.selectedPreset} ")

	def ParSet(self, pars='', val=0,  tween='jump', type='', time='', curve='s', delay='', mode='', expr=''):
		if pars =='':
			try:
				pars = [self.RolloverPar]						
			except:
				pars = ''

				return
		tweenList 	= ['Float', 'Int', 'RGB', 'RGBA', 'Toggle']
		if pars != [None]:
			for par in pars:
				if hasattr(op, "TWEENER"):
					lookup = {
					'min'	 	: par.normMin,
					'max' 		: par.normMax if par.style != 'Menu' else len(par.menuNames),
					'default'	: par.default,
					'half'		: ((par.normMax - par.normMin)/2),
					'random' 	: tdu.remap(tdu.rand(absTime.frame%10000 * par.name), 0, 1, par.normMin, par.normMax) if par.style != 'Menu' else round(tdu.remap(tdu.rand(absTime.frame%10000 * par.name), 0, 1, par.normMin, len(par.menuNames))),
					'paste'		: ui.clipboard}
					
					if val in lookup:				
						v = lookup[val]	
					else:
						v = val
					
					# if curve 	== '':
					# 	curve	= 's' if par.style in tweenList else '',
					type 	= 'absolute' if par.style in tweenList else 'endsnap'
					path 		= par.owner
					name 		= par.name
					if time		== '':
						time	= op.TWEENER.par.Time
					if delay	== '':
						delay	= op.TWEENER.par.Delay
					if mode == '':
						mode 	= str(par.mode).strip('ParMode.')
					if par.mode != ParMode.CONSTANT:
						expr	= par.bindExpr if par.mode == ParMode.BIND else par.expr
					typeLookup = {	
					'absolute'	: f"op.TWEENER.AbsoluteTween(op('{path}').par.{name}, {v}, time={time}, curve='{curve}', delay={delay}, mode='{mode}', expression='{expr}')",
					'relative'	: f"op.TWEENER.RelativeTween(op('{path}').par.{name}, {v}, speed={time}, curve='{curve}', delay={delay}, mode='{mode}', expression='{expr}')",
					'endsnap'	: f"op.TWEENER.CreateEndSnap(op('{path}').par.{name}, '{v}', time={time}, curve='{curve}', mode='{mode}', expression='{expr}')",#, delay='{delay}')",
					'startsnap'	: f"op.TWEENER.CreateStartSnap(op('{path}').par.{name}, '{v}', time={time}, curve='{curve}', mode='{mode}', expression='{expr}')"
					}
					
					if tween == 'tween':
						try:
							run(typeLookup[type])
						except:
							log.Debug('tween failed, execute jump')
							par.val = v
					else:
						par.val = v		
				else:
					par.val = v
		else:
			pass

	def Jump(self, preset = '', pageScope=[''], parScope=['']):
		'''
		Jump methods are mostly deprecated, but are a fallback for missing TWEENER
		parScope and pageScope methods are inactive, as this was causing more problems
		then it fixed and should be done through the Preset Editor, 
		creating new presets as variations when desired
		'''
		if preset != '':
			self.selectedPreset = preset
		# if pageScope == ['']:
		# 	pageScope = self.PageScope
		# if parScope == ['']:
		# 	parScope = self.ParScope
		#parList = [x.name for x in parScope]

		pName		= op(self.selectedPreset).name
		self.recentPreset = pName
		fromOp	= self.Operators[0]
		
		ui.undo.startBlock(f'undo Jump to {op(self.selectedPreset).path} preset "{pName}"')
		for r in range(1, op(self.selectedPreset).numRows):				
			pPath	= str(op(self.selectedPreset)[r, 'path'].val)		
			if op(fromOp).name == pPath:				
				path = op(fromOp).path
			else:
				path= fromOp.op(pPath)			
	#		page	= op(self.selectedPreset)[r, 'page']
			name	= op(self.selectedPreset)[r, 'name']
			v		= op(self.selectedPreset)[r, 'val'].val
			parMode = op(self.selectedPreset)[r, 'mode']
			expr 	= op(self.selectedPreset)[r, 'expr']
			style 	= op(self.selectedPreset)[r, 'style']
			type	= op(self.selectedPreset)[r, 'type'].val
			if v == 'False':
				v = 0
			elif v == 'True':
				v = 1
			if type not in ['startexpr', 'endexpr']:
				if op(path):
					if isinstance(op(path).par[name.val], Par):
						try:
							#if name.val in parList and page.val in pageScope:
							op(path).par[name] = v
		
							op(op(self.selectedPreset))[r, 'Missing'] = '0'
							if style == 'Pulse' and v == True or v == 1:
								op(path).par[name].pulse()
							if parMode == 'CONSTANT':
								op(path).par[name].expr = ''
								op(path).par[name].mode = ParMode.CONSTANT
							elif parMode == 'EXPRESSION':
								op(path).par[name].mode = ParMode.EXPRESSION
								op(path).par[name].expr = expr
							elif parMode == 'BIND':
								op(path).par[name].mode = ParMode.BIND
								op(path).par[name].bindExpr = expr
			
						except:
							if self.ownerComp.par.Logdebug:
								log.Error(f"PresetSting	| FAILED: Jump({self.selectedPreset})")
					else:
						op(op(self.selectedPreset))[r, 'Missing'] = '1'
						if self.ownerComp.par.Logdebug:
							log.Info(f"PresetSting	| Missing: {self.selectedPreset} ")
				else:
					op(op(self.selectedPreset))[r, 'Missing'] = '1'
			else:
				if expr == None:
					expr = f'debug({fromOp})'
				try:
					run(expr, fromOP =op(path))#, fromOP=fromOP, delayFrames = delay)
					op(op(self.selectedPreset))[r, 'Missing'] = '0'
					log.Info(f"PresetSting	| Jump() expr= '{expr}'")
				except:
					log.Warning(f"PresetSting	| FAILED: Jump() expr= '{expr}'")
		ui.undo.endBlock()	

	def Tween(self, index = '', pageScope=[''], parScope=[''], time='', type='', curve='', delay=''):
		"""TWEENER methods for interpolating to preset target values"""	
		fadeTime = time
		ownerComp = self.ownerComp
		pName = op(self.selectedPreset).name
		try:
			if not hasattr(op, 'TWEENER'):
				self.Jump(index, pageScope, parScope)
			else:		
				if index != '':		
					self.selectedPreset = index
				# if pageScope == ['']:
				# 	pageScope = self.PageScope
				# if parScope == ['']:
				# 	parScope = [x.name for x in self.ParScope]
				fromOp	= self.Operators[0]
				ui.undo.startBlock(f'undo Tween to {op(self.selectedPreset).path} preset "{pName}"')
				for r in range(1, op(self.selectedPreset).numRows):
					pPath	= str(op(self.selectedPreset)[r, 'path'].val)		
					if op(fromOp).name == pPath:				
						path = op(fromOp).path
					else:
						path = fromOp.op(pPath)	

					page	= op(self.selectedPreset)[r, 'page']
					name	= op(self.selectedPreset)[r, 'name']
					v		= op(self.selectedPreset)[r, 'val'].val
					if fadeTime == '':
						time= op(self.selectedPreset)[r, 'time']
					else: 
						time= fadeTime
					curve	= op(self.selectedPreset)[r, 'curve'] if op(self.selectedPreset)[r, 'curve'] !='' else 's'
					delay	= op(self.selectedPreset)[r, 'delay']
					mode	= op(self.selectedPreset)[r, 'mode'].val
					expr	= op(self.selectedPreset)[r, 'expr'].val.replace("'", '"')
					type	= op(self.selectedPreset)[r, 'type'].val 
					### bandaid for absolute tweens when assigning expressions
					if mode != 'CONSTANT' and type == 'absolute': 
						type = 'startsnap'

					typeLookup = {	
					'absolute'	: f"op.TWEENER.AbsoluteTween(op('{path}').par.{name}, {v}, time='{time}', curve='{curve}', delay='{delay}', mode='{mode}', expression=\'{expr}\')",
					'relative'	: f"op.TWEENER.RelativeTween(op('{path}').par.{name}, {v}, speed='{time}', curve='{curve}', delay='{delay}', mode='{mode}', expression='{expr}')",
					'endsnap'	: f"op.TWEENER.CreateEndSnap(op('{path}').par.{name}, '{v}', time='{time}', curve='{curve}', mode='{mode}', expression='{expr}')",#, delay='{delay}')",
					'startsnap'	: f"op.TWEENER.CreateStartSnap(op('{path}').par.{name}, '{v}', time='{time}', curve='{curve}', mode='{mode}', expression='{expr}')",
					'startexpr'	: "debug()",
					'endexpr'	: "debug()"
					}
					script	= typeLookup[type]
					if type not in ['startexpr', 'endexpr']:
						if op(path):
							if isinstance(op(path).par[name.val], Par):
								try:
								#	if name.val in parScope and page.val in pageScope:
									run(script)
									op(op(self.selectedPreset))[r, 'Missing'] = '0'	
								except:
									if self.ownerComp.par.Logdebug:
										log.Error(f"PresetSting	| FAILED Preset: '{self.selectedPreset}': TweenPar['{name}']")
							else:
								op(op(self.selectedPreset))[r, 'Missing'] = '1'
								if self.ownerComp.par.Logdebug:
									log.Warning(f"PresetSting	| Missing Preset: '{self.selectedPreset}' TweenPar['{name}']:  ")
						else:
							op(op(self.selectedPreset))[r, 'Missing'] = '1'
							if self.ownerComp.par.Logdebug:
								log.Debug(f'PresetSting | par["{name}" missing')
					
					
					elif type == 'startexpr':
						if delay == '':
							delay = op.TWEENER.par.Delay.eval()	
						if expr == None:
							expr = f'debug({fromOp})'
						
						delay = delay * project.cookRate
						try:
							run(expr, delayFrames= delay, fromOP =op(path))#, fromOP=fromOP, delayFrames = delay)
							op(op(self.selectedPreset))[r, 'Missing'] = '0'
							log.Info(f"PresetSting	| Tween() startexpr: '{expr}', 	delayFrames={delay}")
						except Exception as e:
							debug(e)
					elif type == 'endexpr':
						if delay == '':
							delay = op.TWEENER.par.Delay.eval()	
						if time == '':
							time	=  op.TWEENER.par.Time.eval()				
						delay = (delay + time) *project.cookRate
						# if expr == None:
						# 	expr = f'debug({fromOp})'
						try:
							run(expr, delayFrames= delay, fromOP =op(path))#, fromOP=fromOP, delayFrames = delay)
							op(op(self.selectedPreset))[r, 'Missing'] = '0'
							log.Info(f"PresetSting	| Tween() endexpr: '{expr}', 	delayFrames={delay}")
						except Exception as e:
							debug(e)		
				ui.undo.endBlock()	
			self.recentPreset = pName
			if self.ownerComp.par.Logdebug:
				if fadeTime == '': 
					fadeTime = op.TWEENER.par.Time.eval()
				log.Info(f"PresetSting	| Tween() preset index: {self.PresetNames.index(self.selectedPreset)} '{self.selectedPreset}', 	time={fadeTime}")
		except Exception as e:
			log.Warning(f"PresetSting	| Tween() FAILED preset: {self.PresetNames.index(self.selectedPreset)} '{self.selectedPreset},  time={fadeTime})")

	def SetPresetPars(self, preset=None, val='default',  tween='jump', type='', time=None, curve='s', delay='', mode='', expr=''):
		if not preset: preset = self.recentPreset
		if not time: time = op.TWEENER.par.Time.eval()
	
		if isinstance(preset, int):
			p = self.PresetList[preset]
		else:
			p = self.ownerComp.op(f'PresetSting/{preset}')
		for r in range(1, p.numRows):
			try:
				if p[r, 'path'].val == p.parent(2).name:

					path = p.parent(2).path
				else:
					path = p[r, 'path'].val

				self.ParSet([op(path).par[p[r, 'name'].val]], val=val,  tween=tween, type=type, time=time, curve=curve, delay=delay, mode=mode, expr=expr)
			except Exception as e:
				debug(e)

	def Nextpreset(self):
		newInt = (int(self.ownerComp.par.Selectedpreset)+1)%(self.NumPresets)
		self.ownerComp.par.Preset.val = newInt
		if self.ownerComp.par.Logdebug:
			log.Info(f"PresetSting	| Presetnext(): Tween from index {self.PresetNames.index(self.selectedPreset)} to {newInt}")

	def Prevpreset(self):
		newInt = (int(self.ownerComp.par.Selectedpreset)-1)%(self.NumPresets)
		self.ownerComp.par.Preset.val = newInt
		if self.ownerComp.par.Logdebug:
			log.Info(f"PresetSting	| Presetnext(): Tween from index {self.PresetNames.index(self.selectedPreset)} to {newInt}")

#	Promoted methods as customPars

	def UpdateNumPresets(self):
		
		ownerComp = self.ownerComp
		opfind = ownerComp.op('PresetSting/opfind1')
		opfind.cook(force=True)
		newLen = opfind.numRows-1
		if self.NumPresets > newLen:
			self.Menureconcile()
		self.NumPresets = newLen

	def Menureconcile(self):
		'''onDelete method to update menuTable, called to remove missing presets from menu'''
		dat = self.MenuTable
		for r in reversed(range(1, dat.numRows)):
			if dat[r, 'name'] not in self.ownerComp.op('PresetSting/null_menuNames').col('name'):
				dat.deleteRow(dat.row(r)[0])


	def Addpreset(self, name=''):
		if not name:
			def onSelect(info):
				"""A button has been pressed"""
				if info['button'] != "OK":
					return
				else:
					self.CreatePresetTable(name= info['enteredText'])

			op.TDTox.op('popDialog').Open(
				text = f'Create new preset:',
				title = 'Create Preset',
				buttons = ['OK', 'Cancel'],
				textEntry = True,
				callback = onSelect,)
		else:
			self.CreatePresetTable(name)
		
	def Createdefaultpreset(self):
		self.CreateDefaultPreset()

	def Editselectedpreset(self, preset=''):
		ownerComp = self.ownerComp
		if preset != '':
			self.selectedPreset = preset
		selected = self.ownerComp.op(f"PresetSting/{self.selectedPreset}")
		if hasattr(op, 'PRESETSTINGER'):
			op.PRESETSTINGER.Openpreseteditor(owner=self.ownerComp, preset=self.selectedPreset)
		elif hasattr(op, 'TABLEPOPUP'):
			op.TABLEPOPUP.Open(selected, 
			Label=f'Edit	{ownerComp.parent().path}/{ownerComp.parent().name} 		\
			preset: {selected.name}')
		else:
			op(self.selectedPreset).openViewer()

	def Duplicateselectedpreset(self, preset=''):
		
		if preset != '':
			self.selectedPreset = preset
		ownerComp = self.ownerComp
		name = op(self.selectedPreset).name
		newTable = ownerComp.op('PresetSting').create(tableDAT, tdu.legalName(name))
		op(newTable).copy(op(self.selectedPreset))
		op(newTable).nodeY = self.NumPresets * -100
		op(newTable).tags = {'Preset'}
		op(newTable).cloneImmune = True
		if self.ownerComp.par.Logdebug:
			log.Info(f'PresetSting | Duplicateselectedpreset() {preset}')
	def Deleteselectedpreset(self, preset=''):
		if preset != '':
			self.selectedPreset = preset
		if self.ownerComp.par.Deletewarning:
			self.deleteDialog([op(self.selectedPreset)])
		else:
			self.DeletePresets([op(self.selectedPreset)])
	def Deleteallpresets(self):
		def onSelect(info):
			"""A button has been pressed"""
			if info['button'] != "OK":
				return
			else:
				self.DeletePresets([p.name for p in self.PresetList])

		op.TDTox.op('popDialog').Open(
			text = f'Delete All Presets?:\n{[p.name for p in self.PresetList]}',
			title = 'Delete ALL',
			buttons = ['OK', 'Cancel'],
			textEntry = False,
			callback = onSelect,)	

		if self.ownerComp.par.Logdebug:
			log.Info(f'PresetSting | Deleteallpresets() \n	{[p.name for p in self.PresetList]}')
		
		
	def	deletePresets(self, v : list=''):
		if self.ownerComp.par.Deletewarning:
			if v['button'] != 'Cancel':
				v = v['details']
			else:
				v = ['']
		if v != ['']:
			ui.undo.startBlock(f'undo Delete Selected Preset: {self.selectedPreset}')
			for item in v:
				self.ownerComp.op(f"PresetSting/{item}").destroy()
				if self.ownerComp.par.Logdebug:
					log.Info(f"PresetSting | deletePresets('{self.selectedPreset}'")
			ui.undo.endBlock()
		
	def	DeletePresets(self, v : list=''):
		if v != ['']:
			ui.undo.startBlock(f'undo Delete Selected Preset: {self.selectedPreset}')
			for item in v:
				if not isinstance(item, str):
					item = item.name
				self.ownerComp.op(f"PresetSting/{item}").destroy()
			ui.undo.endBlock()
			if self.ownerComp.par.Logdebug:
				log.Info(f'PresetSting | DeletePresets()  Preset: {v}')
	def deleteDialog(self, info):

		op.TDResources.op('popDialog').Open(
		text=f'Are you sure you want to delete preset(s)?:\n\n{op(info[0]).parent()}\n\n{[i.name for i in info]}',
		title='Delete Presets',
		buttons=['OK', 'Cancel'],
		callback=self.deletePresets,
		details=info,
		textEntry=False,
		escButton=2,
		enterButton=1,
		escOnClickAway=True)


	def Renameselectedpreset(self):
		ui.undo.startBlock(f'undo Rename Selected Preset: {self.selectedPreset}')
		op(self.selectedPreset).name = tdu.legalName(self.ownerComp.par.Name)
		ui.undo.endBlock()
		self.UpdateNumPresets()
		if self.ownerComp.par.Logdebug:
			log.Debug(f'PresetSting | Renameselectedpreset()  Rename Selected Preset: "{self.selectedPreset}"')
	def Exportpreset(self, preset=''):
		debug(preset)
		if preset == '':
			fileName = ui.chooseFile(load=False, start=f'local/mappings/{preset}', 
									fileTypes=['tsv'], title='Save table as:')
		
		if fileName:
			op(self.selectedPreset).save(fileName)
			if self.ownerComp.par.Logdebug:
				log.Info(f"PresetSting | Exportpreset() '{self.selectedPreset}' successfully saved as '{fileName}'")
			

	def Exportallpresets(self, folder=''):
		ownerComp = self.ownerComp
		start = start='local/mappings'
		if folder == '':
			folder = ui.chooseFolder(title='Select Folder', start=start)
		for p in self.PresetList:
			p.save(f"{folder}/{p.name}.tsv", createFolders=True)
		if self.ownerComp.par.Logdebug:
			log.Info(
				f"PresetSting | Exportallpresets()\n	scene: '{ownerComp.name}' \n	presets: {[p.name for p in self.PresetList]}\n	path: {folder}")
	#	debug(f"export all presets from {ownerComp.path} to {path}")


	def Importpreset(self, fileName=''):
		ownerComp = self.ownerComp
		if fileName == '':		
			fileName = ui.chooseFile(load=True, start='local/mappings', 
								fileTypes=['py'], title='Load table:')
		if fileName:
			print('valid')
			name = tdu.legalName(str(os.path.splitext(fileName)[0]).rsplit('/')[-1:][0])
			ui.undo.startBlock(f'undo {fileName} import preset from {name}')
			newTable = ownerComp.op('PresetSting').create(tableDAT, name)
			op(newTable).nodeY = self.NumPresets * -100
			newTable.par.file = fileName
			newTable.par.loadonstartpulse.pulse()
			newTable.par.file = ''
			ui.undo.endBlock()
			if self.ownerComp.par.Logdebug:
				log.Info(f"PresetSting | Importpreset() '{fileName}' successfully imported as '{name}'")

	
	

	def Importpresetfolder(self, folder=''):
		ownerComp = self.ownerComp
		start='local/mappings'		
		if folder == '':
			folder = ui.chooseFolder(title='Select Folder', start=start)
		ownerComp.par.Presetfolder = folder
		if ownerComp.par.Presetfolder != '':
			self.Importdialog(folder)
			
			
				#self.Importpreset(n)
				
		return
	def ImportCallbacks(self, info):
		if info['button'] == 'Cancel':
			return
		if info['button'] == 'Replace':
			self.Deleteallpresets()
		if info['button'] == 'Import':
			pass
		for p in self.ownerComp.op('PresetSting/folder_presets').col('path')[1:]:
			self.Importpreset(p.val)
	def Importdialog(self, info):

		op.TDResources.op('popDialog').Open(
		text=f'Would you like to \nReplace current presets or \nImport to collection?',
		title='Replace Presets?',
		buttons=['Cancel', 'Replace', 'Import'],
		callback=self.ImportCallbacks,
		details=info,
		textEntry=False,
		escButton=2,
		enterButton=1,
		escOnClickAway=True)

	def Appendparameter(self, par, preset=None):
		if not preset: self.ownerComp.par.Selectedpreset = preset
		tweenList = self.tweenList
		preset = self.ownerComp.par.Selectedpreset
		if isinstance(par, Par):
			if par.name in op(preset).col('name'):
				for c in op(preset).col('name'):
					if c.val == par.name and op(preset)[c.row, 'path'] == self.Operators[0].relativePath(par.owner):
						ui.undo.startBlock(f'replace row {par} in {preset}')
						op(preset).replaceRow(c.row, 
							[	
								0,
								self.Operators[0].relativePath(par.owner),						
								par.name,
								par.label,							
								par.val,
								"",
								'absolute' if par.style in tweenList else 'startsnap',
								's' if par.style in tweenList else '',
								"",
								par.default,
								par.min,
								par.max if par.style != 'Menu' else len(par.menuNames),
								par.normMin,
								par.normMax if par.style != 'Menu' else len(par.menuNames),	
								par.clampMin,
								par.clampMax,
								par.enable,
								'' if par.enableExpr == None else par.enableExpr,
								par.help,
								par.startSection,
								par.style,
								par.page,
								str(par.mode).strip('ParMode.'),
								str(par.bindExpr).replace('\'', '"') if par.mode == ParMode.BIND else str(par.expr).replace('\'', '"'),
								'' if par.style not in ['Menu', 'StrMenu'] else par.menuNames,
								'' if par.style not in ['Menu', 'StrMenu'] else par.menuLabels,
								'' if par.style not in ['Menu', 'StrMenu'] else par.menuSource,
									])	
						ui.undo.endBlock()
						if self.ownerComp.par.Logdebug:
							log.Info(f"PresetSting | Appendparameter() '{par.name}' successfully replaced in preset: '{preset}'")
			else:
				ui.undo.startBlock(f'Append {par} to {preset}')
				op(preset).appendRow([	
						0,
						self.Operators[0].relativePath(par.owner),						
						par.name,
						par.label,							
						par.val,
						"",
						'absolute' if par.style in tweenList else 'startsnap',
						's' if par.style in tweenList else '',
						"",
						par.default,
						par.min,
						par.max if par.style != 'Menu' else len(par.menuNames),
						par.normMin,
						par.normMax if par.style != 'Menu' else len(par.menuNames),	
						par.clampMin,
						par.clampMax,
						par.enable,
						'' if par.enableExpr == None else par.enableExpr,
						par.help,
						par.startSection,
						par.style,
						par.page,
						str(par.mode).strip('ParMode.'),
						str(par.bindExpr).replace('\'', '"') if par.mode == ParMode.BIND else str(par.expr).replace('\'', '"'),
						'' if par.style not in ['Menu', 'StrMenu'] else par.menuNames,
						'' if par.style not in ['Menu', 'StrMenu'] else par.menuLabels,
						'' if par.style not in ['Menu', 'StrMenu'] else par.menuSource,
						])	
				ui.undo.endBlock()
				if self.ownerComp.par.Logdebug:
					log.Info(f"PresetSting | Appendparameter() '{par.name}' successfully appended to preset:'{preset}'")

	def Appendpreset(self, preset=''):
		if preset != '':
			self.selectedPreset = preset
		ownerComp = self.ownerComp
		fileName = ui.chooseFile(load=True, start='local/mappings ', 
								fileTypes=['py'], title='Load table:')
		
		name = tdu.legalName(str(os.path.splitext(fileName)[0]).rsplit('/')[-1:][0])

		if fileName:
			
			ui.undo.startBlock(f'undo append {fileName} to preset {name}')
			newTable = ownerComp.create(tableDAT, 'importProxy')
			op(newTable).nodeY = self.NumPresets * -100
			newTable.par.file = fileName
			newTable.par.loadonstartpulse.pulse()
			newTable.par.file = ''
			op(self.selectedPreset).appendRows(op('importProxy').rows()[1:])
			newTable.destroy()
			ui.undo.endBlock()
			if self.ownerComp.par.Logdebug:
				log.Info(f"PresetSting | Appendpreset() '{fileName}' successfully appended to preset: '{preset}'")


	def Test(self):
		debug('Test')


# parexec_passThru callbacks
	def onParValueChange(self, par=None, val=None, prev=None):
		"""panelexec_passThru value change callbacks to condense logic to ext"""
		if par.name == 'Preset':
			if par.val in self.PresetNames:
				self.Tween(par.val)
		if hasattr(self, par.name):
			try:
				getattr(self.ownerComp, par.name)()
			except Exception as e:
				debug(e, par.name)
	def onParPulse(self, par=None, val=None):
		"""panelexec_passThru pulse callbacks to condense logic to ext"""
		ownerComp = self.ownerComp
		if par.name == 'Help':
			print(help(self))
		if hasattr(self, par.name):
			try:
				getattr(ownerComp, par.name)()
			except Exception as e:
				debug(e)

# end region 