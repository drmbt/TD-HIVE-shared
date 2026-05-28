"""local get out of jail free card to bypass op.LOGGER dependency and allow for local logging"""

def Notset(string):
	return
def Debug(string):
	if parent().par.Logdebug and int(parent().par.Loglevel) <=0:
		debug(f"Debug | {string}") 

def Info(string):

	if parent().par.Logdebug and int(parent().par.Loglevel) <=1:
		debug(f"Info | {string}")

def Warning(string):
	if parent().par.Logdebug and int(parent().par.Loglevel) <=2:
		debug(f"Warning | {string}")

def Error(string):
	if parent().par.Logdebug and int(parent().par.Loglevel) <=3:
		debug(f"Error | {string}")

def Critical(string):

	if parent().par.Logdebug and int(parent().par.Loglevel) <=4:
		debug(f"Critical | {string}")
