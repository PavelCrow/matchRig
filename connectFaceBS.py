import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm
pm.mel.eval('source "pk_makeControls.mel"')

def xform():
	objects = cmds.ls(sl=True)
	for o in objects:
		gr = cmds.group(empty=True, n=o+"_xform")
		cmds.parent(gr,o)
		cmds.setAttr(gr+".tx", 0)
		cmds.setAttr(gr+".ty", 0)
		cmds.setAttr(gr+".tz", 0)
		cmds.setAttr(gr+".rx", 0)
		cmds.setAttr(gr+".ry", 0)
		cmds.setAttr(gr+".rz", 0)
		cmds.setAttr(gr+".sx", 1)
		cmds.setAttr(gr+".sy", 1)
		cmds.setAttr(gr+".sz", 1)
		try:
			parent = cmds.listRelatives(o, parent=True)[0]
			cmds.parent(gr, parent)
		except:
			cmds.parent(gr, world=True)
		cmds.parent(o,gr)
		cmds.select(objects)

def connectCinema():
	# make jaw ctrl
	ctrl = pm.mel.eval("pk_makeCircle(\"jaw_ctrl\", \"y\")" )
	pm.select('skin_CC_Base_JawRoot', ctrl)
	c = pm.parentConstraint(mo=0)
	pm.delete(c)
	pm.select(ctrl)
	xform()
	
	pm.select('jaw_ctrl.cv[0:7]')
	pm.scale(4, 4, 4)
	pm.move(0, -3.5, 5.5, r=1)
	
	pm.setAttr(ctrl+".overrideEnabled", 1)
	pm.setAttr(ctrl+".overrideColor", 17)
	
	pm.parent('jaw_ctrl_xform', 'head')
	pm.select(ctrl, 'skin_CC_Base_JawRoot')
	pm.parentConstraint(mo=0)
	
	cmds.setAttr(ctrl+".sx", lock=1, keyable=0, channelBox=0)
	cmds.setAttr(ctrl+".sy", lock=1, keyable=0, channelBox=0)
	cmds.setAttr(ctrl+".sz", lock=1, keyable=0, channelBox=0)
	cmds.setAttr(ctrl+".v", lock=1, keyable=0, channelBox=0)
	
	
	# make tongue ctrl
	ctrl = pm.mel.eval("pk_makeCircle(\"tongue_ctrl\", \"y\")" )
	pm.select('skin_CC_Base_Tongue01', ctrl)
	c = pm.parentConstraint(mo=0)
	pm.delete(c)
	pm.select(ctrl)
	xform()
	
	pm.select('tongue_ctrl.cv[0:7]')
	pm.rotate(90, 0, 0)
	pm.move(2, 0, 0, r=1, os=1)
	
	pm.setAttr(ctrl+".overrideEnabled", 1)
	pm.setAttr(ctrl+".overrideColor", 15)
	
	pm.parent('tongue_ctrl_xform', 'jaw_ctrl')
	pm.select(ctrl, 'skin_CC_Base_Tongue01')
	pm.parentConstraint(mo=0)
	
	cmds.setAttr(ctrl+".sx", lock=1, keyable=0, channelBox=0)
	cmds.setAttr(ctrl+".sy", lock=1, keyable=0, channelBox=0)
	cmds.setAttr(ctrl+".sz", lock=1, keyable=0, channelBox=0)
	cmds.setAttr(ctrl+".v", lock=1, keyable=0, channelBox=0)
	
	# set blendShapes
	ctrl = pm.PyNode('tongue_ctrl')
	pm.addAttr('tongue_ctrl', ln="Tongue_up", at='double', k=1, min=0, max=1)
	pm.addAttr('tongue_ctrl', ln="Tongue_Raise", at='double', k=1, min=0, max=1)
	pm.addAttr('tongue_ctrl', ln="Tongue_Out", at='double', k=1, min=0, max=1)
	pm.addAttr('tongue_ctrl', ln="Tongue_Narrow", at='double', k=1, min=0, max=1)
	pm.addAttr('tongue_ctrl', ln="Tongue_Lower", at='double', k=1, min=0, max=1)
	pm.addAttr('tongue_ctrl', ln="Tongue_Curl_U", at='double', k=1, min=0, max=1)
	pm.addAttr('tongue_ctrl', ln="Tongue_Curl_D", at='double', k=1, min=0, max=1)
	
	tSh = pm.PyNode('CC_Base_TongueShape')
	sc = tSh.inMesh.inputs()[0]
	gp = sc.input[0].inputGeometry.inputs()[0]
	bs = gp.inputGeometry.inputs()[0]
	
	ctrl.Tongue_up >> bs.Tongue_up__RL_9__
	ctrl.Tongue_Raise >> bs.Tongue_Raise__RL_10__
	ctrl.Tongue_Out >> bs.Tongue_Out__RL_11__
	ctrl.Tongue_Narrow >> bs.Tongue_Narrow__RL_12__
	ctrl.Tongue_Lower >> bs.Tongue_Lower__RL_13__
	ctrl.Tongue_Curl_U >> bs.Tongue_Curl_U__RL_14__
	ctrl.Tongue_Curl_D >> bs.Tongue_Curl_D__RL_15__
	
	tSh = pm.PyNode('CC_Base_Body')
	sc = tSh.inMesh.inputs()[0]
	gp = sc.input[0].inputGeometry.inputs()[0]
	bs = gp.inputGeometry.inputs()[0]
	
	pm.connectAttr('eyes_ctrl.Eyes_Blink', bs.Eyes_Blink__RL_48__)
	pm.connectAttr('eyes_ctrl.Eyes_Squint', bs.Eyes_Squint__RL_47__)
	pm.connectAttr('eyes_ctrl.Eye_Blink_L', bs.Eye_Blink_L__RL_49__)
	pm.connectAttr('eyes_ctrl.Eye_Blink_R', bs.Eye_Blink_R__RL_50__)
	pm.connectAttr('eyes_ctrl.Eyelids_Enlarge', bs.Eyelids_Enlarge__RL_42__)
	
	pm.connectAttr('lips_ctrl.Open', bs.Open__RL_1__)
	pm.connectAttr('lips_ctrl.Explosive', bs.Explosive__RL_2__)
	pm.connectAttr('lips_ctrl.Dental', bs.Dental_Lip__RL_3__)
	pm.connectAttr('lips_ctrl.Tight_O', bs.Tight_O__RL_4__)
	pm.connectAttr('lips_ctrl.Tight', bs.Tight__RL_5__)
	pm.connectAttr('lips_ctrl.Wide', bs.Wide__RL_6__)
	pm.connectAttr('lips_ctrl.Affricate', bs.Affricate__RL_7__)
	pm.connectAttr('lips_ctrl.Lip_Open', bs.Lip_Open__RL_8__)
	pm.connectAttr('lips_ctrl.Lips_Drop', bs.Lips_Drop__RL_26__)
	pm.connectAttr('lips_ctrl.Lips_Smirk', bs.Lips_Smirk__RL_31__)
	pm.connectAttr('lips_ctrl.Lips_Smirk_L', bs.Lips_Smirk_L__RL_32__)
	pm.connectAttr('lips_ctrl.Lips_Smirk_R', bs.Lips_Smirk_R__RL_33__)
	pm.connectAttr('lips_ctrl.Lips_Widen_Sides', bs.Lips_Widen_Sides__RL_34__)
	pm.connectAttr('lips_ctrl.Lips_Drop_Sides', bs.Lips_Drop_Sides__RL_35__)
	pm.connectAttr('lips_ctrl.Lips_Drop_L_Side', bs.Lips_Drop_L_Side__RL_36__)
	pm.connectAttr('lips_ctrl.Lips_Drop_R_Side', bs.Lips_Drop_R_Side__RL_37__)
	pm.connectAttr('lips_ctrl.Lips_Jut_Open', bs.Lips_Jut_Open__RL_39__)
	pm.connectAttr('lips_ctrl.Lips_Widen', bs.Lips_Widen__RL_40__)
	pm.connectAttr('lips_ctrl.Lips_Puckered_Open', bs.Lips_Puckered_Open__RL_41__)
	pm.connectAttr('lips_ctrl.Lips_Zipped_Tight', bs.Lips_Zipped_Tight__RL_43__)
	pm.connectAttr('lips_ctrl.Mouth_Open', bs.Mouth_Open__RL_44__)
	pm.connectAttr('lips_ctrl.Lip_Raise_Top', bs.Lip_Raise_Top__RL_45__)
	pm.connectAttr('lips_ctrl.Lips_Tuck', bs.Lips_Tuck__RL_46__)
	pm.connectAttr('lips_ctrl.Lips_Open', bs.Lips_Open__RL_51__)
	pm.connectAttr('lips_ctrl.Jaw_Rotate', bs.Jaw_Rotate_D__RL_58__)
	pm.connectAttr('lips_ctrl.Jaw_Move', bs.Jaw_Move_D__RL_61__)
	
	pm.connectAttr('brows_ctrl.Brow_Raise_Inner_L', bs.Brow_Raise_Inner_L__RL_16__)
	pm.connectAttr('brows_ctrl.Brow_Raise_Inner_R', bs.Brow_Raise_Inner_R__RL_17__)
	pm.connectAttr('brows_ctrl.Brow_Raise_Outer_L', bs.Brow_Raise_Outer_L__RL_18__)
	pm.connectAttr('brows_ctrl.Brow_Raise_Outer_R', bs.Brow_Raise_Outer_R__RL_19__)
	pm.connectAttr('brows_ctrl.Brow_Drop_L', bs.Brow_Drop_L__RL_20__)
	pm.connectAttr('brows_ctrl.Brow_Drop_R', bs.Brow_Drop_R__RL_21__)
	pm.connectAttr('brows_ctrl.Brow_Raise_L', bs.Brow_Raise_L__RL_22__)
	pm.connectAttr('brows_ctrl.Brow_Raise_R', bs.Brow_Raise_R__RL_23__)
	
	pm.connectAttr('chicks_ctrl.Cheek_Raise_L', bs.Cheek_Raise_L__RL_24__)
	pm.connectAttr('chicks_ctrl.Cheek_Raise_R', bs.Cheek_Raise_R__RL_25__)
	pm.connectAttr('chicks_ctrl.Chin_Raise', bs.Chin_Raise__RL_38__)
	
	pm.connectAttr('nose_ctrl.Nose_Scrunch', bs.Nose_Scrunch__RL_27__)
	pm.connectAttr('nose_ctrl.Nose_Flank_Raise_L', bs.Nose_Flank_Raise_L__RL_28__)
	pm.connectAttr('nose_ctrl.Nose_Flank_Raise_R', bs.Nose_Flank_Raise_R__RL_29__)
	pm.connectAttr('nose_ctrl.Nose_Flank_Raise', bs.Nose_Flank_Raise__RL_30__)

def connectMixamo():
	
	tSh = pm.PyNode('BodyShape')
	sc = tSh.inMesh.inputs()[0]
	gp = sc.input[0].inputGeometry.inputs()[0]
	bs = gp.inputGeometry.inputs()[0]
	tSh2 = pm.PyNode('default1')
	sc2 = tSh2.inMesh.inputs()[0]
	gp2 = sc2.input[0].inputGeometry.inputs()[0]
	bs2 = gp2.inputGeometry.inputs()[0]
	mainCtrl = pm.PyNode('ctrlBox')
	
	attrs = []
	for a in mainCtrl.listAttr():
		if a.isKeyable():
			attrs.append(a)
	
	for a in attrs:
		attrName = a.name().split('.')[-1]
		mainCtrl.attr(attrName) >> bs2.attr(attrName)
		mainCtrl.attr(attrName) >> bs.attr(attrName)




