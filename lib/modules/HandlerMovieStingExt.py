import TDJSON

class ExtHandlerExt:
	
	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		self.ownerCompParent = ownerComp.parent()
		self.par_page_names = ['MovieFile', 'MovieAudio', 'MovieInfo']
		self.ownerComp.tags=['MovieSting']
	
	def Add_ext(self):
		# fetch target pars as whole page and convert to JSON Dict
		for page in self.ownerComp.customPages:
			if page in self.par_page_names:
				page_as_json = TDJSON.pageToJSONDict(page)
		
		# add pars to parent
				TDJSON.addParametersFromJSONDict(self.ownerCompParent, page_as_json)
		
		# set references for all pars to tie ops  together
		for each_par in self.ownerCompParent.pars():
			if each_par.page in self.par_page_names:
				self.ownerComp.par[each_par.name].bindExpr = f"parent().par.{each_par.name}"
		extsLen = self.ownerCompParent.par.extension1.sequence.numBlocks
		if self.ownerCompParent.par.extension1.eval() =='' and extsLen == 1:
			extNum = 1
			self.ownerCompParent.par.extension1.sequence.numBlocks = extsLen + 1
		else:
			extNum = extsLen + 1
			self.ownerCompParent.par.extension1.sequence.numBlocks = extsLen + 2
		ext1Script = f"op('{self.ownerCompParent}').par.extension{extNum} = \"op('./MovieSting/MovieStingExt').module.MovieStingExt(me)\""
		name1Script = f"op('{self.ownerCompParent}').par.extname{extNum} = 'MovieStingExt'"
		promote1Script = f"op('{self.ownerCompParent}').par.promoteextension{extNum} = True"
		menu0Script = f"op('{self.ownerComp}').par.Driver.menuSource =		 \"op('{self.ownerComp}').op('audiodevout').par.driver\""
		menu1Script = f"op('{self.ownerComp}').parent().par.Driver.menuSource = \"op('{self.ownerComp}').op('audiodevout').par.driver\""
		menu2Script = f"op('{self.ownerComp}').par.Device.menuSource =		 \"op('{self.ownerComp}').op('audiodevout').par.device\""
		menu3Script = f"op('{self.ownerComp}').parent().par.Device.menuSource = \"op('{self.ownerComp}').op('audiodevout').par.device\""
		cookScript = f"op('{self.ownerComp}').parent().cook(force=True, recurse=True)"
		run(ext1Script)
		run(name1Script)
		run(promote1Script)

		run(menu0Script, delayFrames=20)
		run(menu1Script,delayFrames=30)
		run(menu2Script, delayFrames=30)
		run(menu3Script,delayFrames=30)
		run(cookScript,delayFrames=35)
	#	self.ownerCompParent.tags = ['']
	def Remove_ext(self):
		debug('removeExt')
		# for each_par in self.ownerComp.pars():
		# 	each_par.mode = ParMode.CONSTANT
		# for custom_par in self.ownerCompParent.customPars():
		# 	if custom_par.page in self.par_page_namess:
		# 		par.destroy()
		

		# for r in range(1, len(self.ownerCompParent.extensions)+1):
		# 	if 'MenuSourceExt' in self.ownerCompParent.par[f'extension{r}'].val:
		# 		self.ownerCompParent.par[f'extname{r}'] = ''
		# 		self.ownerCompParent.par[f'promoteextension{r}'] = False
		# 		self.ownerCompParent.par[f'extension{r}'] = ''

		try:
			me.parent().op('math_offset').inputConnectors[0].connect(me.parent().op('switch1'))
			me.parent().op('extensionParExec').par.active = False
			op('Lagger').destroy()
		except:
			pass
		for r in range(1, len(self.ownerCompParent.extensions)):
			if 'MovieStingExt' in self.ownerCompParent.par[f'extension{r}'].val:
				self.ownerCompParent.par[f'extname{r}'] = ''
				self.ownerCompParent.par[f'promoteextension{r}'] = False
				self.ownerCompParent.par[f'extension{r}'] = ''
	
		pageList = self.par_page_names
		destroy_pars = [each_par for each_par in self.ownerCompParent.pars() if each_par.page in pageList]
	
		for each_par in self.ownerComp.pars():
			try:
				each_par.mode = ParMode.CONSTANT
			except:
				pass		
			# debug(each_par)
		
		for each_par in destroy_pars:
			try:
				each_par.enableExpr = ''
			except:
				pass
		for each_par in destroy_pars:
			try:
				each_par.destroy()
			except:
				pass
	

		
		
		


		custom_pages = self.ownerCompParent.customPages
		for page in reversed(custom_pages):
			if page.name in self.par_page_names:
				try:
					custom_page_index = custom_pages.index(page.name)
					self.ownerCompParent.customPages[custom_page_index].destroy()
				except:
					pass
		

		self.ownerComp.destroy()
 