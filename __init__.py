#import maya.cmds as cmds
#import main, utils
#reload(main)
#reload(utils)

#global matchRig_win, matchRig_bakeWin
#try:
	#matchRig_win.close()
	#matchRig_win.deleteLater()
#except: pass
#try:
	#matchRig_bakeWin.close()
	#matchRig_bakeWin.deleteLater()
#except: pass

#matchRig_win = main.MainWindow() 
#matchRig_win.show()

#matchRig_bakeWin = main.ConnectWindow() 
#matchRig_bakeWin.show()


'''

import matchRig
import matchRig.main
reload(matchRig)
reload(matchRig.main)

global matchRig_win
try:
	matchRig_win.close()
	matchRig_win.deleteLater()
except: pass

matchRig_win = matchRig.main.MainWindow() 
matchRig_win.show()


'''

'''

import matchRig
import matchRig.main
reload(matchRig)
reload(matchRig.main)

global matchRig_bakeWin
try:
	matchRig_bakeWin.close()
	matchRig_bakeWin.deleteLater()
except: pass

matchRig_bakeWin = matchRig.main.ConnectWindow() 
matchRig_bakeWin.show()

'''