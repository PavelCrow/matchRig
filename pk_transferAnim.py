import maya.cmds as cmds
import maya.mel as mel

animRoot = "CC_Base_Root"

if cmds.window("TransferAnimWindow", ex=True):
	cmds.deleteUI("TransferAnimWindow", window=True)

ns = ""
animRoot = ""
animNs = ""

constr_list = ['CC_Base_R_UpperarmTwist01', 'CC_Base_L_UpperarmTwist01', 
                   'CC_Base_R_Elbow', 'CC_Base_L_Elbow',
                   'CC_Base_R_ForearmTwist01', 'CC_Base_L_ForearmTwist01',
                   'CC_Base_R_ThighTwist01', 'CC_Base_L_ThighTwist01',
                   'CC_Base_R_Knee', 'CC_Base_L_Knee',
                   'CC_Base_R_CalfTwist01', 'CC_Base_L_CalfTwist01',
                   'CC_Base_R_Ribs', 'CC_Base_L_Ribs',
                   'CC_Base_R_RibsNub', 'CC_Base_L_RibsNub',
                   'CC_Base_R_RibsTwist', 'CC_Base_L_RibsTwist',
                   'CC_Base_R_Breast', 'CC_Base_L_Breast']

def ui():
	# -----------------------------------------------------------------------------------------
	window = cmds.window("TransferAnimWindow", title = "Trasfer Amination", widthHeight = (620, 150), sizeable=False)

	mainLayout = cmds.columnLayout(adjustableColumn=True)

	cmds.rowLayout(parent=mainLayout, numberOfColumns=3, columnWidth3=(90, 125, 50), adjustableColumn=2, columnAlign=(1, 'right'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )
	cmds.text(l="Skeleton Root  ")
	rootLine = cmds.textField('rootLine', enable=True, editable=False, text="not set")
	cmds.button(l="set", c=getSceletonRoot)

	cmds.rowLayout(parent=mainLayout, numberOfColumns=3, columnWidth3=(90, 125, 50), adjustableColumn=2, columnAlign=(1, 'right'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )
	cmds.text(l="Rig NameSpace  ")
	nsLine = cmds.textField('nsLine', enable=True, editable=False, text="not set")
	cmds.button(l="grab", c=getNS)

	cmds.separator(parent=mainLayout, h=10, style="in")
	connect_btn = cmds.button("connect_btn", parent=mainLayout, l="Connect Rig", width=150, height=30, enable=True, c=connect)
	bake_btn = cmds.button("bake_btn", parent=mainLayout, l="Bake", width=150, height=30, enable=True, c=transfer)

def getSceletonRoot(self):
	print 'getSceletonRoot'
	global animRoot, animNs
	
	animRoot = cmds.ls(sl=1)[0]
	cmds.textField('rootLine', e=1, text=animRoot)
	
	if ":" in animRoot:
		animNs = animRoot.split(":")[0]
	
def getNS(self):
	print 'getNS'
	global ns
	
	ns = cmds.ls(sl=1)[0].split(":")[0]
	
	cmds.textField('nsLine', e=1, text=ns)

def connect(self):

	if ns == "":
		cmds.warning("Set Namespace from any contol of the rig")
		return

	if animRoot == "":
		cmds.warning("Set animated skeleton root")
		return
	
	joints = cmds.listRelatives(animRoot, allDescendents=1)
	joints.append(animRoot)
	
	for o in joints:
		#print o#, ns+':input_'+o.replace(animNs+":", "")
		try:
			cmds.connectAttr(o+'.t', ns+':input_'+o.replace(animNs+":", "")+'.t')
			cmds.connectAttr(o+'.r', ns+':input_'+o.replace(animNs+":", "")+'.r')
			cmds.connectAttr(o+'.s', ns+':input_'+o.replace(animNs+":", "")+'.s')        
		except: 
			print "MISS", o, ns+':input_'+o.replace(animNs+":", "")
	
	try:
		cmds.connectAttr('CC_Base_Hip.t', ns+':CC_Base_Hip.t')
		cmds.connectAttr('CC_Base_Hip.r', ns+':CC_Base_Hip.r')
		cmds.connectAttr('CC_Base_Hip.s', ns+':CC_Base_Hip.s')	
	except: print "MISS", 'CC_Base_Hip -> ', ns+':CC_Base_Hip'
	try:
		cmds.connectAttr('CC_Base_Hip.t', ns+':input_CC_Base_Root|'+ns+':CC_Base_Hip.t')
		cmds.connectAttr('CC_Base_Hip.r', ns+':input_CC_Base_Root|'+ns+':CC_Base_Hip.r')
		cmds.connectAttr('CC_Base_Hip.s', ns+':input_CC_Base_Root|'+ns+':CC_Base_Hip.s')	
	except: pass
	
	for j in constr_list:
		try:
			cmds.parentConstraint(j, ns+':skin_'+j, mo=0)
		except: pass
	
def transfer(self):
	cmds.select(ns+':controlSet')
	
	for j in constr_list:
		try:
			cmds.select(ns+':skin_'+j, add=1)
		except: pass
	
	mel.eval("string $minTime = `playbackOptions -q -minTime`;")
	mel.eval("string $maxTime = `playbackOptions -q -maxTime`;")
	mel.eval('string $range = $minTime + ":" + $maxTime;')
	mel.eval('bakeResults -simulation true -t $range  -sampleBy 1 -disableImplicitControl true -preserveOutsideKeys false -sparseAnimCurveBake false -removeBakedAttributeFromLayer false -bakeOnOverrideLayer false -minimizeRotation true -at "tx" -at "ty" -at "tz" -at "rx" -at "ry" -at "rz";')			
	
	#cmds.delete(animRoot)

ui()
cmds.showWindow()
