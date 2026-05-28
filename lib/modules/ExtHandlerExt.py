import TDJSON
 
class ExtHandlerExt:
	
	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		self.ownerCompParent = ownerComp.parent()
		self.par_page_names = ['PRESETS']
		self.ownerComp.tags=['PresetSting']
	
	def Add_ext(self):
		# fetch target pars as whole page and convert to JSON Dict
		if "PRESETS" not in parent(2).customPages:
			for page in self.ownerComp.customPages:
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
			ext1Script = f"op('{self.ownerCompParent}').par.extension{extNum} = \"op('./PresetSting/PresetStingExt').module.PresetStingExt(me)\""
			name1Script = f"op('{self.ownerCompParent}').par.extname{extNum} = 'PresetStingExt'"
			promote1Script = f"op('{self.ownerCompParent}').par.promoteextension{extNum} = True"
			ext2Script = f"op('{self.ownerCompParent}').par.extension{extNum+1} = \"op('./PresetSting/MenuSourceExt').module.MenuSourceExt(me)\""
			name2Script = f"op('{self.ownerCompParent}').par.extname{extNum+1} = 'MenuSourceExt'"
			promote2Script = f"op('{self.ownerCompParent}').par.promoteextension{extNum+1} = True"
			menu0Script = f"op('{self.ownerComp}').par.Preset.menuSource =		 \"op('./MenuSourceExt').module.MenuSourceExt('menu')\""
			menu1Script = f"op('{self.ownerComp}').par.Selectedpreset.menuSource = \"op('./MenuSourceExt').module.MenuSourceExt('menu')\""
			menu2Script = f"op('{self.ownerCompParent}').par.Preset.menuSource =		 \"op('./PresetSting/MenuSourceExt').module.MenuSourceExt('menu')\""
			menu3Script = f"op('{self.ownerCompParent}').par.Selectedpreset.menuSource = \"op('./PresetSting/MenuSourceExt').module.MenuSourceExt('menu')\""
			run(ext1Script)
			run(name1Script)
			run(promote1Script)
			run(ext2Script)
			run(name2Script)
			run(promote2Script)
			run(menu0Script, delayFrames=20)
			run(menu1Script,delayFrames=20)
			run(menu2Script, delayFrames=30)
			run(menu3Script,delayFrames=30)
	#	self.ownerCompParent.tags = ['']
	def Remove_ext(self):
		# for each_par in self.ownerComp.pars():
		# 	each_par.mode = ParMode.CONSTANT
		# for custom_par in self.ownerCompParent.customPars():
		# 	if custom_par.page in self.par_page_namess:
		# 		par.destroy()
		

		for r in range(1, len(self.ownerCompParent.extensions)+1):
			if 'MenuSourceExt' in self.ownerCompParent.par[f'extension{r}'].val:
				self.ownerCompParent.par[f'extname{r}'] = ''
				self.ownerCompParent.par[f'promoteextension{r}'] = False
				self.ownerCompParent.par[f'extension{r}'] = ''
		for r in range(1, len(self.ownerCompParent.extensions)):
			if 'PresetSting' in self.ownerCompParent.par[f'extension{r}'].val:
				self.ownerCompParent.par[f'extname{r}'] = ''
				self.ownerCompParent.par[f'promoteextension{r}'] = False
				self.ownerCompParent.par[f'extension{r}'] = ''
		
		
		# custom_pages = self.ownerCompParent.customPages
		# for page in custom_pages:
		# 	if page.name in reversed(self.par_page_namess):
		# 		custom_page_index = custom_pages.index(page)
		# 		debug(custom_page_index)
		# 		self.ownerCompParent.customPages[custom_page_index].destroy()

		# # self.ownerComp.destroy()

		pageList = self.par_page_names
		destroy_pars = [each_par for each_par in self.ownerCompParent.pars() if each_par.page in pageList]

		for each_par in destroy_pars:
			each_par.destroy()
		
		for each_par in self.ownerComp.pars():
			each_par.mode = ParMode.CONSTANT


		custom_pages = self.ownerCompParent.customPages
		for page in reversed(custom_pages):
			if page.name in self.par_page_names:
				custom_page_index = custom_pages.index(page.name)
				self.ownerCompParent.customPages[custom_page_index].destroy()

		self.ownerComp.destroy()
 