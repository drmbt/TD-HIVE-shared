"""

Help: search "Extensions" in wiki
"""
log = op.TDResources.op('TDAppLogger') if not hasattr(op, 'LOGGER') else op.LOGGER
from TDStoreTools import StorageManager
import TDFunctions as TDF

class MenuSourceExt:
	"""
	MenuSourceExt description
	"""
	def __init__(self, path):
		self.ownerComp = path

#	methods for mod access
	@property		
	def menuNames(self):
		return [x.val for x in op(self.ownerComp).col('name')][1:]
	@property
	def menuLabels(self):
		return [x.val for x in op(self.ownerComp).col('name')][1:]

#	extension methods
	@property
	def MenuTable(self):
		return op('menu')

	@property
	def NameList(self):
		return [n.val for n in op('null_menuNames').col('name')[1:]]

	@property
	def MenuNames(self):
		return [n.val for n in op('menu').col('name')[1:]]

	def UpdateMenu(self):
		self.Addnew()
		self.RemoveBlank()
		self.RemoveOld()
		self.FixPaths()
		#run(f"op('{self.ownerComp}').FixPaths()", delayFrames=10)
		self.ownerComp.UpdateNumPresets()

	def UpdatePaths(self):

		menu = self.MenuTable
		if menu.numRows > 1:
			oldName = menu[1, 'path'].val.split('/')[-3]
			changeOp= parent()
			assembly = changeOp.path.split('/')[:-2]
			assembly.append(f"{parent(2).Operators[0].name}/PresetSting/")
			path = '/'.join(assembly)
			for r in range(1, self.MenuTable.numRows):
				self.MenuTable[r, 'path'] = path + self.MenuTable[r, 'name']
			for preset in parent().findChildren(depth=1, type=tableDAT, name='^menu'):
				for r in range(1, preset.numRows):
					if preset[r, 'path'].val == oldName:
						preset[r, 'path'] = parent(2).Operators[0].name
				log.Debug(f'PresetSting	| UpdatePaths() in preset: "{preset}" from "{oldName}" to {parent(2).Operators[0].name}')
			run(f"op('{self.ownerComp}').ClearErrors()", delayFrames=1)
				

	def ClearErrors(self):
		self.ownerComp.clearScriptErrors(recurse=True, error='*')
	def Addnew(self):
		#debug(len(self.NameList))
		for name in self.NameList:
			#debug(name)
			if name not in self.MenuNames:
				self.MenuTable.appendRow(op('null_menuNames').row(name))
		return
	def RemoveOld(self):
		#debug()
		for name in self.MenuNames:
			if name not in self.NameList:
				self.MenuTable.deleteRow(name)
	
	def FixPaths(self):
		for r in range(1, self.MenuTable.numRows):
			l = str(self.MenuTable[r, 'path']).split('/') #)
			newPath = "/".join(l[:-1]) 
			self.MenuTable[r, 'path'] = newPath + f"/{self.MenuTable[r, 'name'].val}"
		return 
	
	def RemoveBlank(self):
		for r in reversed(range(1, self.MenuTable.numRows)):
			if self.MenuTable[r,0].val =='':
				self.MenuTable.deleteRow(r)