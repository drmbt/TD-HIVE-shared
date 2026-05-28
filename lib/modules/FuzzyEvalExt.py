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
log = op.LOGGER
V = op.MOD
class FuzzyEvalExt:
	"""
	DEPENDANCIES: op.MOD Vscript
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp


	@property
	def Window(self):
		return self.ownerComp.op('window1')

	@property
	def Field(self):
		return self.ownerComp.op('field1')

	@property
	def Field_result(self):
		return self.ownerComp.op('field_result')
	
	@property
	def Vscript(self):
		return self.ownerComp.par.Vscript.eval()

	@Vscript.setter
	def Vscript(self, val):
		self.ownerComp.par.Vscript = val

	def Open(self):

		self.Close()
		
		self.ownerComp.setFocus()
		self.Window.par.winopen.pulse()
		
			# hack should be automatically set by kbfocus
			# self.ownerComp.op('entry').setFocus()
			# hack shouldn't have to wait a frame
		run('op("' + self.ownerComp.path + '").op("field1").'
						'setKeyboardFocus(selectAll=True)',
						delayFrames=1, delayRef=op.TDResources)
		
		return

	def Close(self):
		self.Clear()
		self.Window.par.winclose.pulse()

	def Clear(self):
		self.Field.op('string')[0,0] = ""
		self.Field_result.op('string')[0,0] = ""
		self.Field_result.par.borderar = .5
		self.Field_result.par.borderag = .5
		self.Field_result.par.borderab = .5

	def Eval(self):
		self.ownerComp.op('script_live').run()
		# path = self.ownerComp.path
		# script =self.ownerComp.op('null_eval')[0,0].val

		# fromOP=ui.panes.current.owner
		
		# if self.Vscript:
		# 	try:
		# 		V.ParseString(script)
		# 	except:
		# 		pass
		# try:	
		# 	run(script, fromOP=fromOP)
		# 	self.Field_result.par.borderar = 0
		# 	self.Field_result.par.borderag = 1
		# 	self.Field_result.par.borderab = 0
		# 	log.Debug(f"{fromOP}: {self.ownerComp.op('null_eval')[0,0].val} = {self.Field_result.op('string')[0,0].val}")
		# except Exception as e:
		# 	debug(e)
		# 	if self.ownerComp.op('null_eval')[0,0].val == '':
		# 		self.Clear()
		# 	else:
		# 		self.Field_result.par.borderar = 1
		# 		self.Field_result.par.borderag = 0
		# 		self.Field_result.par.borderab = 0
		# 	pass


	# def LiveEval(self):
	# 	path = self.ownerComp
	# 	script = f"{path}.op('Field_result/string')[0,0] = eval({path}.op('null_eval')[0,0].val)"
	# 	fromOP=ui.panes.current.owner

	# 	if self.Vscript:
	# 		try:
	# 			run(f"op.MOD.ParseString('{op('null_eval')[0,0].val}')")
	# 		except:
	# 			pass
	# 	try:	
	# 		debug('try')
	# 		run(script, fromOP=fromOP)
	# 		self.Field_result.par.borderar = 0
	# 		self.Field_result.par.borderag = 1
	# 		self.Field_result.par.borderab = 0
	# 		#log.Debug(f"{fromOP}: {op('null_eval')[0,0].val} = {op('Field_result/string')[0,0].val}")
	# 	except Exception as e:
	# 		debug(e)
	# 		#log.Debug(f"FAILED    {fromOP}: {op('null_eval')[0,0].val} = {op('Field_result/string')[0,0].val}, {e}")
	# 		if self.ownerComp.op('null_eval')[0,0].val == '':
	# 			self.Clear()
	# 		else:
	# 			self.Field_result.par.borderar = 1
	# 			self.Field_result.par.borderag = 0
	# 			self.Field_result.par.borderab = 0
	# 		pass
	# 	return