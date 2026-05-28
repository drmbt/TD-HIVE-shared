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
from fractions import Fraction
log = op.LOGGER
class MovieStingExt:
	"""
	MovieStingExt description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

		# properties
		TDF.createProperty(self, 'MyProperty', value=0, dependable=True,
						   readOnly=False)
		self.RangeFrames()
		# attributes:
		self.a = 0 # attribute
		self.B = 1 # promoted attribute

		# stored items (persistent across saves and re-initialization):
		storedItems = [
			# Only 'name' is required...
			{'name': 'StoredProperty', 'default': None, 'readOnly': False,
			 						'property': True, 'dependable': True},
		]
		# Uncomment the line below to store StoredProperty. To clear stored
		# 	items, use the Storage section of the Component Editor
		
		# self.stored = StorageManager(self, ownerComp, storedItems)

	# def __del__(self):
	# 	me.parent().Remove_ext()

	def Winopen(self):
		if hasattr(op, 'PARPOPUP'):
			op.PARPOPUP.Open(Op = me.parent().path, Label = f"MovieSting | {me.parent(2).name}")
		else:
			me.parent().openViewer()

	def RangeFrames(self, val=None):
		if not val: val = me.parent().op('info_movie')['length']
		me.parent().op('math_frameRange').par.torange2 = val

	def Trimunit(self, val):

		me.parent().op('moviefilein').par.tstartunit = val
		me.parent().op('moviefilein').par.tendunit = val
		me.parent().op('moviefilein').par.indexunit = val
		me.parent().op('movieinfo').par.tstartunit = val
		me.parent().op('movieinfo').par.tendunit = val
		me.parent().op('movieinfo').par.indexunit = val

	def GetInfo(self):
		infoCHOP = me.parent().op('info_movie')
		info = {}
		for r in range(infoCHOP.numChans):
			info[infoCHOP[r].name] = infoCHOP[r].eval()
		return info
	

	def GetFraction(self, x, y):
		return Fraction(x, y).limit_denominator()


	def Initinfo(self):
		ownerComp = self.ownerComp
		info = self.GetInfo()
		lookup = {
			'true_length'		: 'Truenumimages',
			'num_images'	:	"Numimages",
			'sample_rate'	: 'Rate',
			'aspectx'		: 'Aspectw',
			'aspecty'		: 'Aspecth',
			'file_resx'		: 'Resw',
			'file_resy'		: 'Resh'
		}
		for key, val in lookup.items():
			self.ownerComp.par[val] = me.parent().op('info_movie')[key]
			me.parent().par[val] = me.parent().op('info_movie')[key]
		self.ownerComp.par.Ratio = round(ownerComp.par.Aspectw / ownerComp.par.Aspecth, 3)
		me.parent().par.Ratio = round(ownerComp.par.Aspectw / ownerComp.par.Aspecth, 3)
		fraction = self.GetFraction(int(ownerComp.par.Aspectw.val), int(ownerComp.par.Aspecth.val))
		ownerComp.par.Ratiofraction = f"{fraction.numerator} : {fraction.denominator}"
		me.parent().par.Ratiofraction = f"{fraction.numerator} : {fraction.denominator}"
		log.Info(f"MovieStingExt Initinfo() | {self.ownerComp.par.File}")
		#self.ownerComp.par.Ratiofraction = str(Fraction(ownerComp.par.Aspectw, ownerComp.par.Aspecth))

	def Testme(self):
		debug(me.parent().op('info_movie'))
		debug(me.op('info_movie'))