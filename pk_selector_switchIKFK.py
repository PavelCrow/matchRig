import maya.cmds as cmds
import maya.OpenMaya as om
import maya.mel as mel
import maya.api.OpenMaya as OpenMaya
from functools import partial
import math, sys

armControls = ["arm_control", "shoulder", "arm", "forearm", "wrist", "elbow", "hand", "paw", "paw_palm", "palm", "palmToe"]
legControls = ["leg_control", "foot_fingers", "toeTip", "foot", "knee", "upLeg", "leg", "heel", "toe", "ankle"]
char = ""
sidePrefix = ""
ikFkControl = ""
mirrorAttrLis = ["translateX", "translateY", "translateZ", "rotateX", "rotateY", "rotateZ"]
useMatrixSwitch = False


##################################
# Switch IKFK
##################################

def switchIkFk():
	global char, sidePrefix, ikFkControl, armControls, legControls, useMatrixSwitch

	sels = cmds.ls(sl=True)
	for sel in sels:
		selObject = sel
		if ':' in selObject:
			objectWithoutNS = selObject.split(":")[-1]
			char = selObject.split(objectWithoutNS)[0]
		else:
			objectWithoutNS = selObject
	
		if "_" not in objectWithoutNS and objectWithoutNS != "head":
			print "Select one control of arm leg"
			return
		
		if objectWithoutNS == "head" or objectWithoutNS == "head_control":
			ikFkControl = char + "head"
			limbType = "head"
		else:
			sidePrefix = objectWithoutNS.split("_")[0]
			controlWithoutSidePrefix = objectWithoutNS.split("_")[1]
			limbType = ""
	
			# Choose type of control switch ----------------------------------
			if controlWithoutSidePrefix in armControls:
				ikFkControl = char + sidePrefix + "_" + "arm_control"
				limbType = "arm"
			
			elif controlWithoutSidePrefix in legControls:
				ikFkControl = char  + sidePrefix + "_" + "leg_control"
				limbType = "leg"
			
			else:
				print "Select control of arm or leg"
				return
	
		# Get current ikFk
		if limbType == "head":
			ikFk = cmds.getAttr(ikFkControl + ".ikFk")
		else:
			ikFk = cmds.getAttr(ikFkControl + ".fkIk")
		
		if cmds.attributeQuery("useMatrixIkFkSwitch", n=char+"character", exists=True):
			useMatrixSwitch = cmds.getAttr(char+"character"+".useMatrixIkFkSwitch")
			
		# Swith ikFk
		if ikFk < 0.5 :
			fk_to_ik(limbType)
		else :
			ik_to_fk(limbType)
			
		mel.eval("selectorRefresh;")

def fk_to_ik(limbType):
	print "fk to ik"
	global char, sidePrefix, ikFkControl
	print "QQQQ"
	def snapIkElbow(sourceA, sourceB, sourceC, target):
		# Get pointPositions
		aPos = cmds.xform(sourceA, t=1, q=1, worldSpace=1)
		bPos = cmds.xform(sourceB, t=1, q=1, worldSpace=1)
		cPos = cmds.xform(sourceC, t=1, q=1, worldSpace=1)

		# Get point Vectors
		a = OpenMaya.MVector(aPos)
		b = OpenMaya.MVector(bPos)
		c = OpenMaya.MVector(cPos)

		# Get vectors
		ab = OpenMaya.MVector(b-a)
		ac = OpenMaya.MVector(c-a)

		# Get length of lower vector
		acLen = OpenMaya.MVector(ac).length()

		# Get projection upper vector on lower vector
		pr = ab*ac / acLen

		# Normalize result
		acNorm = OpenMaya.MVector(ac).normal()

		# Get new vector from start to middle point
		ce = acNorm * pr

		# Get position middle point
		e = ce + a

		# Get vector from middle to elbow point and normalize it
		eb = b - e
		ebNorm = OpenMaya.MVector(eb).normal()

		# Make vector as needed length and from b point and final Point elbow control
		elbowV = ebNorm * 0.5 * acLen + b






		# Move control
		cmds.xform(target, t=elbowV, worldSpace=1)

	if limbType == "head":
		selObject = char + "head"
		# Get transform
		tr = cmds.xform( selObject, q=True, t=True, ws=True)
		rt = cmds.xform( selObject, q=True, ro=True, ws=True)
		
		try:
			cmds.setAttr(ikFkControl + ".fkIk", 1)
		except: 
			cmds.setAttr(ikFkControl + ".ikFk", 1)
		
		# Set Transform
		cmds.move( tr[0], tr[1], tr[2], selObject, rotatePivotRelative=True)
		cmds.rotate(rt[0], rt[1], rt[2], selObject, ws=True)
		
	if limbType == "arm":

		# Get sources and tragets
		sourceElbowA = char + sidePrefix + "_" + "arm_limbA_skinJoint"
		sourceElbowB = char + sidePrefix + "_" + "arm_limbB_skinJoint"
		sourceElbowC = char + sidePrefix + "_" + "arm_limbB_end_skinJoint"
		targetElbow = char + sidePrefix + "_" + "elbow"

		sourceHand = char + sidePrefix + "_" + "hand_ikFkSwitchHelper"
		targetHand = char + sidePrefix + "_" + "hand"

		# Transforming
		if cmds.objExists(sourceHand):
			snap(sourceHand, targetHand)

		snapIkElbow(sourceElbowA, sourceElbowB, sourceElbowC, targetElbow)
		
		cmds.setAttr(ikFkControl + ".fkIk", 1)

	if limbType == "leg":
		# Get sources and tragets
		sourceElbowA = char + sidePrefix + "_" + "upLeg_ikFkSwitchHelper"
		sourceElbowB = char + sidePrefix + "_" + "leg_ikFkSwitchHelper"
		sourceElbowC = char + sidePrefix + "_" + "heel_ikFkSwitchHelper"
		targetElbow = char + sidePrefix + "_" + "knee"

		sourceFoot = char + sidePrefix + "_" + "foot_ikFkSwitchHelper"
		targetFoot = char + sidePrefix + "_" + "foot"
		if useMatrixSwitch:
			if cmds.objExists(char + sidePrefix + "_" + "foot_fingers_ikFkSwitchHelper"):
				sourceFingers = char + sidePrefix + "_" + "foot_fingers_ikFkSwitchHelper"
			else:
				sourceFingers = char + sidePrefix + "_" + "toe_ikFkSwitchHelper"
		else:
			sourceFingers = char + sidePrefix + "_" + "foot_fingers_ikFkSwitchHelper"
		targetFingers = char + sidePrefix + "_" + "foot_fingers"

		# Reset ankle
		try:
			cmds.setAttr(char + sidePrefix + "_" + "ankle.rx", 0)
			cmds.setAttr(char + sidePrefix + "_" + "ankle.ry", 0)
			cmds.setAttr(char + sidePrefix + "_" + "ankle.rz", 0)
			cmds.setAttr(char + sidePrefix + "_" + "ankle.auto", 0)
		except:
			pass

		# Transforming
		snap(sourceFoot, targetFoot)
		snap(sourceFingers, targetFingers)
		snapIkElbow(sourceElbowA, sourceElbowB, sourceElbowC, targetElbow)

		

		cmds.setAttr(ikFkControl + ".fkIk", 1)

def ik_to_fk(limbType):
	print "ik to fk"
	global char, sidePrefix, ikFkControl

	# Set Fk
	#if not useMatrixSwitch:
		#try:
			#cmds.setAttr(ikFkControl + ".fkIk", 0)
		#except: 
			#cmds.setAttr(ikFkControl + ".ikFk", 0)

	if limbType == "arm":

		# Get sources and tragets
		sourceArm = char + sidePrefix + "_" + "arm_ikFkSwitchHelper"
		targetArm = char + sidePrefix + "_" + "arm"
		sourceForearm = char + sidePrefix + "_" + "forearm_ikFkSwitchHelper"
		targetForearm = char + sidePrefix + "_" + "forearm"
		sourceWrist = char + sidePrefix + "_" + "wrist_ikFkSwitchHelper"
		targetWrist = char + sidePrefix + "_" + "wrist"

		# Transforming
		snap(sourceArm, targetArm)
		snap(sourceForearm, targetForearm)
		snap(sourceWrist, targetWrist)

		# Set length
		cmds.setAttr(ikFkControl + ".fkIk", 1)

		sourceLengthA = char + sidePrefix + "_" + "arm_limbA_ikJoint"
		sourceLengthB = char + sidePrefix + "_" + "arm_limbB_ikJoint"
		targetLength = char + sidePrefix + "_" + "arm_control"
		if cmds.attributeQuery( 'lengthFactor1', node=targetLength, exists=True ):
			l = cmds.getAttr(sourceLengthA + ".scaleX")
			l2 = cmds.getAttr(sourceLengthB + ".scaleX")
			cmds.setAttr(targetLength + ".lengthFactor1", l)
			cmds.setAttr(targetLength + ".lengthFactor2", l2)
		cmds.setAttr(ikFkControl + ".fkIk", 0)

		# r_forearm fix
		angle = cmds.getAttr(targetForearm + ".rotateY")
		if (angle > 180):
			angle = angle - 360
			cmds.setAttr(targetForearm + ".rotateY", angle)

	if limbType == "leg":
		# Get sources and tragets
		sourceUpLeg = char + sidePrefix + "_" + "upLeg_ikFkSwitchHelper"
		targetUpLeg = char + sidePrefix + "_" + "upLeg"
		sourceLeg = char + sidePrefix + "_" + "leg_ikFkSwitchHelper"
		targetLeg = char + sidePrefix + "_" + "leg"
		sourceHeel = char + sidePrefix + "_" + "heel_ikFkSwitchHelper"
		targetHeel = char + sidePrefix + "_" + "heel"
		sourceToe = char + sidePrefix + "_" + "toe_ikFkSwitchHelper"
		targetToe = char + sidePrefix + "_" + "toe"

		# Transforming
		snap(sourceUpLeg, targetUpLeg)
		snap(sourceLeg, targetLeg)
		snap(sourceHeel, targetHeel)
		snap(sourceToe, targetToe)

		# Set length
		cmds.setAttr(ikFkControl + ".fkIk", 1)
		sourceLengthA = char + sidePrefix + "_" + "leg_limbA_skinJoint"
		sourceLengthB = char + sidePrefix + "_" + "leg_limbB_skinJoint"
		targetLength = char + sidePrefix + "_" + "leg_control"
		if cmds.attributeQuery( 'lengthFactor1', node=targetLength, exists=True ):
			l = cmds.getAttr(sourceLengthA + ".scaleX")
			l2 = cmds.getAttr(sourceLengthB + ".scaleX")
			cmds.setAttr(targetLength + ".lengthFactor1", l)
			cmds.setAttr(targetLength + ".lengthFactor2", l2)
		cmds.setAttr(ikFkControl + ".fkIk", 0)

		# r_leg fix
		angle = cmds.getAttr(targetLeg + ".rotateY")
		if (angle > 180):
			angle = angle - 360
			cmds.setAttr(targetLeg + ".rotateY", angle)

	if limbType == "head":
		selObject = char + "head"
		# Get transform
		tr = cmds.xform( selObject, q=True, t=True, ws=True)
		rt = cmds.xform( selObject, q=True, ro=True, ws=True)

		try:
			cmds.setAttr(ikFkControl + ".fkIk", 0)
		except: 
			cmds.setAttr(ikFkControl + ".ikFk", 0)
		
		# Set Transform
		cmds.move( tr[0], tr[1], tr[2], selObject, rotatePivotRelative=True)
		cmds.rotate(rt[0], rt[1], rt[2], selObject, ws=True)
	
			

def snap(source, target):
	
	if useMatrixSwitch:
		#print source, target
		# Get transform by local martix ----------------------------------------------
		
		targetParent = cmds.listRelatives( target, parent=True )
	
		# get rotate order of the target
		rotOrderTarget = cmds.getAttr('%s.rotateOrder'%target)
	
		# get matrix of the source
		matrixList = cmds.getAttr('%s.worldMatrix'%source)
		mMatrix = om.MMatrix()
		om.MScriptUtil.createMatrixFromList(matrixList, mMatrix)
	
	
		# get target parent inverse matrix
		parent_floatList = cmds.xform(targetParent,q=True,matrix=1, worldSpace=1)
		parent_matrix = om.MMatrix()
		om.MScriptUtil.createMatrixFromList(parent_floatList,parent_matrix )
		invMatrixParent = parent_matrix.inverse()
	
		# solve final matrix
		final_matrix = mMatrix * invMatrixParent
	
		# get rotation
		mTransformMtx = om.MTransformationMatrix(final_matrix)
		rotOrderTarget = cmds.getAttr('%s.rotateOrder'%target)
		eulerRot = mTransformMtx.eulerRotation()
		eulerRot.reorderIt(rotOrderTarget)
		angles = [math.degrees(angle) for angle in (eulerRot.x, eulerRot.y, eulerRot.z)]
		#print angles
		# rotate
		cmds.rotate(angles[0], angles[1], angles[2], target, os=True)
	
		# Move
		tr = cmds.xform( source, q=True, t=True, ws=True)
		cmds.move( tr[0], tr[1], tr[2], target, rotatePivotRelative=True)			
		
		
	else:

		# Get transform
		tr = cmds.xform( source, q=True, t=True, ws=True)
		rt = cmds.xform( source, q=True, ro=True, ws=True)

		# Set Transform
		cmds.move( tr[0], tr[1], tr[2], target, rotatePivotRelative=True)
		cmds.rotate(rt[0], rt[1], rt[2], target, ws=True)




##################################
# Snap elbow/knee
##################################

def snapElbowKnee():
	global char, sidePrefix, armControls, legControls

	sels = cmds.ls(sl=True)
	for sel in sels:
		try:
			selObject = sel
			if ':' in selObject:
				ctrlName = selObject.split(":")[-1]
				char = selObject.split(ctrlName)[0]
				objectWithoutNS = ctrlName
			else:
				objectWithoutNS = selObject
		
			if "_" not in objectWithoutNS:
				print "Select one control of arm or leg"
				return
		
			sidePrefix = objectWithoutNS.split("_")[0]
			controlWithoutSidePrefix = objectWithoutNS.split("_")[1]
		
			# Get sources and tragets
			if controlWithoutSidePrefix in armControls:
				sourceA = char + sidePrefix + "_" + "arm_limbA_skinJoint"
				sourceB = char + sidePrefix + "_" + "arm_limbB_skinJoint"
				sourceC = char + sidePrefix + "_" + "hand"
				target = char + sidePrefix + "_" + "elbow"
		
			elif controlWithoutSidePrefix in legControls:
				sourceA = char + sidePrefix + "_" + "upLeg_ikFkSwitchHelper"
				sourceB = char + sidePrefix + "_" + "leg_ikFkSwitchHelperAim"
				sourceC = char + sidePrefix + "_" + "kneeEnd_ikFkSwitchHelper"
				target = char + sidePrefix + "_" + "knee"
		
			else:
				print "Select control of arm or leg"
				return
		
		
			# Get pointPositions
			aPos = cmds.xform(sourceA, t=1, q=1, worldSpace=1)
			bPos = cmds.xform(sourceB, t=1, q=1, worldSpace=1)
			cPos = cmds.xform(sourceC, t=1, q=1, worldSpace=1)
		
			# Get point Vectors
			a = OpenMaya.MVector(aPos)
			b = OpenMaya.MVector(bPos)
			c = OpenMaya.MVector(cPos)
		
			# Get vectors
			ab = OpenMaya.MVector(b-a)
			ac = OpenMaya.MVector(c-a)
		
			# Get length of lower vector
			acLen = OpenMaya.MVector(ac).length()
		
			# Get projection upper vector on lower vector
			pr = ab*ac / acLen
		
			# Normalize result
			acNorm = OpenMaya.MVector(ac).normal()
		
			# Get new vector from start to middle point
			ce = acNorm * pr
		
			# Get position middle point
			e = ce + a
		
			# Get vector from middle to elbow point and normalize it
			eb = b - e
			ebNorm = OpenMaya.MVector(eb).normal()
		
			# Make vector as needed length and from b point and final Point elbow control
			elbowV = ebNorm * acLen * 0.5 + b
		
			# Move control
			cmds.xform(target, t=elbowV, worldSpace=1)
		except: pass


##################################
# Symmetry
##################################

def getMatrix(node):
	'''
	Gets the world matrix of an object based on name.
	'''
	#Selection list object and MObject for our matrix
	selection = OpenMaya.MSelectionList()
	matrixObject = OpenMaya.MObject()

	#Adding object
	selection.add(node)

	#New api is nice since it will just return an MObject instead of taking two arguments.
	MObjectA = selection.getDependNode(0)

	#Dependency node so we can get the worldMatrix attribute
	fnThisNode = OpenMaya.MFnDependencyNode(MObjectA)

	#Get it's world matrix plug
	worldMatrixAttr = fnThisNode.attribute( "worldMatrix" )

	#Getting mPlug by plugging in our MObject and attribute
	matrixPlug = OpenMaya.MPlug( MObjectA, worldMatrixAttr )
	matrixPlug = matrixPlug.elementByLogicalIndex( 0 )

	#Get matrix plug as MObject so we can get it's data.
	matrixObject = matrixPlug.asMObject(  )

	#Finally get the data
	worldMatrixData = OpenMaya.MFnMatrixData( matrixObject )
	worldMatrix = worldMatrixData.matrix( )

	return worldMatrix

def decompMatrix(node,matrix):
	'''
	Decomposes a MMatrix in new api. Returns an list of translation,rotation,scale in world space.
	'''
	#Rotate order of object
	rotOrder = cmds.getAttr('%s.rotateOrder'%node)
	#print rotOrder

	#Puts matrix into transformation matrix
	mTransformMtx = OpenMaya.MTransformationMatrix(matrix)

	#Translation Values
	trans = mTransformMtx.translation(OpenMaya.MSpace.kWorld)

	#Euler rotation value in radians
	eulerRot = mTransformMtx.rotation()

	#Reorder rotation order based on ctrl.
	eulerRot.reorderIt(rotOrder)

	#Find degrees
	angles = [math.degrees(angle) for angle in (eulerRot.x, eulerRot.y, eulerRot.z)]

	#Find world scale of our object.
	scale = mTransformMtx.scale(OpenMaya.MSpace.kWorld)

	#Return Values
	return [trans.x,trans.y,trans.z],angles,scale

def symmetryByMatrix(source, target, ns):
	# set float lists
	source_floatList = cmds.xform(source, q=True, matrix=1, worldSpace=1)
	# print source_floatList

	mirror_floatList = cmds.xform(ns + "mirror_loc",q=True,matrix=1, worldSpace=1)
	vector_floatList = [-1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
	# vector2_floatList = [-1.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, -1.0]

	# Make matrixes
	source_matrix = om.MMatrix()
	om.MScriptUtil.createMatrixFromList(source_floatList,source_matrix)

	mirror_matrix = om.MMatrix()
	om.MScriptUtil.createMatrixFromList(mirror_floatList,mirror_matrix)
	mirror_transformMatrix = om.MTransformationMatrix(mirror_matrix)
	mirror_inverse_matrix = mirror_transformMatrix.asMatrixInverse()

	vector_matrix = om.MMatrix()
	om.MScriptUtil.createMatrixFromList(vector_floatList,vector_matrix )

	# vector2_matrix = om.MMatrix()
	# om.MScriptUtil.createMatrixFromList(vector2_floatList,vector2_matrix )

	# Solve
	final_matrix = source_matrix * mirror_inverse_matrix * vector_matrix * mirror_matrix #* vector2_matrix
	final_transformMatrix = om.MTransformationMatrix(final_matrix)

	# Apply
	t = final_transformMatrix.translation(om.MSpace.kWorld)
	cmds.move( t.x, t.y, t.z, target, absolute=True, worldSpace=True )


	cmds.rotate( 0, cmds.getAttr(ns + "posCtrl.ry")*-2, 0, target, relative=True, worldSpace=True )
	cmds.rotate( 0, cmds.getAttr(ns + "mirror_loc.ry")*2, 0, target, relative=True, worldSpace=True )

	#Get Matrix
	# mat = getMatrix(source)
	# print mat

	# #Decompose matrix
	# matDecomp = decompMatrix(source,mat)

	#Print our values
	# sys.stdout.write('\n---------------------------%s---------------------------\n'%source)
	# sys.stdout.write('\nTranslation : %s' %matDecomp[0])
	# sys.stdout.write('\nRotation    : %s' %matDecomp[1])
	# sys.stdout.write('\nScale       : %s\n' %matDecomp[2])
	pass

def symmetryByConstraint(source, target, ns):
	#print "cc", source, target, ns
	
	sel = cmds.ls(sl=True)
	
	loc = cmds.spaceLocator()
	cmds.parent(loc, ns+"mirror_loc")
	con = cmds.parentConstraint(source, loc)
	cmds.delete(con)
	gr = cmds.group()
	cmds.xform(os=1, piv=(0,0,0) )
	cmds.setAttr(gr+".scaleX", -1)
	cmds.parent(loc, ns+"mirror_loc")
	cmds.delete(gr)
	
	
	
	cmds.setAttr(loc[0]+".scaleZ", 1)
	
	cmds.duplicate(target, n="loc2")
	loc2 = "loc2"
	#targetParent = cmds.listRelatives(target, p=True)
	#cmds.parent(loc2[0], targetParent[0])
	con2 = cmds.parentConstraint(loc, "loc2")
	
	#cmds.setAttr(loc2[0]+".rotateOrder", cmds.getAttr(target+".rotateOrder"))
	#return
	cmds.setAttr(target+".tx", cmds.getAttr(loc2+".tx"))
	cmds.setAttr(target+".ty", cmds.getAttr(loc2+".ty"))
	cmds.setAttr(target+".tz", cmds.getAttr(loc2+".tz"))
	cmds.setAttr(target+".rx", cmds.getAttr(loc2+".rx"))
	if cmds.getAttr(loc2+".ry") > 0:
		cmds.setAttr(target+".ry", cmds.getAttr(loc2+".ry")-180)
	else:
		cmds.setAttr(target+".ry", cmds.getAttr(loc2+".ry")+180)
	cmds.setAttr(target+".rz", cmds.getAttr(loc2+".rz"))
	cmds.delete(loc)
	cmds.delete(loc2)
	
	cmds.select(sel)
	
def symmetry():
	controls = cmds.ls(selection=True)
	#if len(controls) > 0:
		#cmds.select (clear=True)

	for control in controls:
		#print control
		#Get control name without ns
		ctrlName = control.split(":")[-1]

		#Get namespases
		ns = control.split(ctrlName)[:-1]
		if len(ns) == 0:
			ns = ""
		else:
			ns = ns[0]

		#Get side
		side = ctrlName.split("_")[0]
		if side != "l" and side != "r":
			side = "c"

		#Get name without side prefix
		nameUnside = ctrlName[2:]
		if side == "c":
			nameUnside = ctrlName

		#Get target control
		if side == "c":
			target = ctrlName
		elif side == "l":
			target = "r_" + nameUnside
		elif side == "r":
			target = "l_" + nameUnside


		attrList = []
		attrListKeyable = cmds.listAttr(control, keyable=True )
		if type(attrListKeyable) != list :
			attrListKeyable = []
		attrListNonkeyable = cmds.listAttr( channelBox = True )
		if type(attrListNonkeyable) != list :
			attrListNonkeyable = []
		attrList = attrListKeyable + attrListNonkeyable


		if cmds.attributeQuery( 'mirrored', node=control, exists=True ):
			mirrored = cmds.getAttr(control + ".mirrored")
		else:
			mirrored = False

		if cmds.attributeQuery( 'matrixMirror', node=control, exists=True ):
			matrixMirror = cmds.getAttr(control + ".matrixMirror")
		else:
			matrixMirror = False
			
		if cmds.attributeQuery( 'constraintMirror', node=control, exists=True ):
			constraintMirror = cmds.getAttr(control + ".constraintMirror")
		else:
			constraintMirror = False

		if side != "c":
			for attr in attrList:
				try:
					attrVar = cmds.getAttr(control + "." + attr)
				except:
					#print target, "cannot getAttr"
					pass

				# if attr is translate or rotate
				if attr in mirrorAttrLis:
					# if ctrl is full mirrored
					if mirrored:
						cmds.setAttr((ns + target + "." + attr), attrVar)
					# else if ctrl have mirrors attr's
					elif cmds.attributeQuery( 'translateXMirror', node=control, exists=True ):
						# mirror atribute and set
						if cmds.getAttr(control + "." + attr + "Mirror"):
							cmds.setAttr((ns + target + "." + attr), attrVar * -1)
						# else, copy attr and set
						else:
							cmds.setAttr((ns + target + "." + attr), attrVar )
					else:
						print "Control is not SET !!!!!!!!!!!!!"
				# another attr is coping
				else:
					try:
						cmds.setAttr((ns + target + "." + attr), attrVar)
					except:
						#print target, "cannot modify"
						pass

		else:
			for attr in attrList:
				try:
					attrVar = cmds.getAttr(control + "." + attr)
				except:
					#print target, "cannot getAttr"
					pass

				# if attr is translate or rotate
				if attr in mirrorAttrLis:
					# else if ctrl have mirrors attr's
					if cmds.attributeQuery( 'translateXMirror', node=control, exists=True ):
						# mirror atribute and set
						if cmds.getAttr(control + "." + attr + "Mirror"):
							cmds.setAttr((ns + target + "." + attr), 0)
					else:
						print "Control is not SET !!!!!!!!!!!!!"


		if matrixMirror:
			symmetryByMatrix(control, ns + target, ns)
		if constraintMirror:
			symmetryByConstraint(control, ns + target, ns)

		# fix for head
		if matrixMirror and ctrlName == "head" and cmds.getAttr(control + ".ikFk") == 1 :
			cmds.setAttr(control + ".ry", cmds.getAttr(ns + "head_symmetryHelper_loc.ry") )
			cmds.rotate( 0, cmds.getAttr(ns + "posCtrl.ry")*-1, 0, control, relative=True, worldSpace=True )
		if matrixMirror and ctrlName == "head" and cmds.getAttr(control + ".ikFk") == 0 :
			cmds.setAttr(control + ".ry", 0 )



##################################
# Mirror
##################################

def mirrorByMatrix(source, target, ns):
	# set float lists
	source_floatList = cmds.xform(source,q=True,matrix=1, worldSpace=1)
	target_floatList = cmds.xform(target,q=True,matrix=1, worldSpace=1)
	# print source_floatList

	sourceT = cmds.getAttr(source + ".t")
	targetT = cmds.getAttr(target + ".t")

	mirror_floatList = cmds.xform(ns + "mirror_loc",q=True,matrix=1, worldSpace=1)
	vector_floatList = [-1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]

	# Make matrixes
	source_matrix = om.MMatrix()
	om.MScriptUtil.createMatrixFromList(source_floatList,source_matrix)

	mirror_matrix = om.MMatrix()
	om.MScriptUtil.createMatrixFromList(mirror_floatList,mirror_matrix)
	mirror_transformMatrix = om.MTransformationMatrix(mirror_matrix)
	mirror_inverse_matrix = mirror_transformMatrix.asMatrixInverse()

	vector_matrix = om.MMatrix()
	om.MScriptUtil.createMatrixFromList(vector_floatList,vector_matrix )

	# Solve
	final_matrix = source_matrix * mirror_inverse_matrix * vector_matrix * mirror_matrix
	final_transformMatrix = om.MTransformationMatrix(final_matrix)

	# Apply
	t = final_transformMatrix.translation(om.MSpace.kWorld)
	cmds.move( t.x, t.y, t.z, target, absolute=True, worldSpace=True )

	cmds.rotate( 0, cmds.getAttr(ns + "posCtrl.ry")*-2, 0, target, relative=True, worldSpace=True )
	cmds.rotate( 0, cmds.getAttr(ns + "mirror_loc.ry")*2, 0, target, relative=True, worldSpace=True )





	# Make matrixes
	target_matrix = om.MMatrix()
	om.MScriptUtil.createMatrixFromList(target_floatList,target_matrix)

	# Solve
	final_matrix = target_matrix * mirror_inverse_matrix * vector_matrix * mirror_matrix
	final_transformMatrix = om.MTransformationMatrix(final_matrix)

	# Apply
	t = final_transformMatrix.translation(om.MSpace.kWorld)
	cmds.move( t.x, t.y, t.z, source, absolute=True, worldSpace=True )

	cmds.rotate( 0, cmds.getAttr(ns + "posCtrl.ry")*-2, 0, source, relative=True, worldSpace=True )
	cmds.rotate( 0, cmds.getAttr(ns + "mirror_loc.ry")*2, 0, source, relative=True, worldSpace=True )

def mirror():
	controls = cmds.ls(selection=True)

	#if len(controls) > 0:
		#cmds.select (clear=True)

	# Remove opposite control, if selected both
	for selCntrol in controls:
		#Get sourceControl name without ns
		ctrlName = selCntrol.split(":")[-1]

		#Get side
		nameUnside = ctrlName[2:]
		side = ctrlName.split("_")[0]



		if side == "r" :
			print "l_" + nameUnside
			if ("l_" + nameUnside) in controls:
				print "l_" + nameUnside + " exist"
				controls.remove("l_" + nameUnside)


	for sourceControl in controls:
		#Get sourceControl name without ns
		ctrlName = sourceControl.split(":")[-1]

		#Get namespases
		ns = sourceControl.split(ctrlName)[:-1]
		if len(ns) == 0:
			ns = ""
		else:
			ns = ns[0]

		#Get side
		side = ctrlName.split("_")[0]
		if side != "l" and side != "r":
			side = "c"

		#Get name without side prefix
		nameUnside = ctrlName[2:]
		if side == "c":
			nameUnside = ctrlName

		#Get target control
		if side == "c":
			target = ctrlName
		elif side == "l":
			target = "r_" + nameUnside
		elif side == "r":
			target = "l_" + nameUnside

		if cmds.attributeQuery( 'mirrored', node=sourceControl, exists=True ):
			mirrored = cmds.getAttr(sourceControl + ".mirrored")
		else:
			mirrored = False

		if cmds.attributeQuery( 'matrixMirror', node=sourceControl, exists=True ):
			matrixMirror = cmds.getAttr(sourceControl + ".matrixMirror")
		else:
			matrixMirror = False

		targetControl = ns + target
		# print sourceControl, targetControl

		# copy data

		attrList = []

		attrListKeyable = cmds.listAttr(sourceControl, keyable=True )
		if type(attrListKeyable) != list :
			attrListKeyable = []
		attrListNonkeyable = cmds.listAttr( channelBox = True )
		if type(attrListNonkeyable) != list :
			attrListNonkeyable = []
		attrList = attrListKeyable + attrListNonkeyable

		if side != "c":
			for attr in attrList:
				try:
					attrVarSource = cmds.getAttr(sourceControl + "." + attr)
					attrVarTarget = cmds.getAttr(targetControl + "." + attr)
				except:
					#print target, "cannot getAttr"
					pass

				# if attr is translate or rotate
				if attr in mirrorAttrLis:
					# if ctrl is full mirrored
					if mirrored:
						cmds.setAttr((targetControl + "." + attr), attrVarSource)
						cmds.setAttr((sourceControl + "." + attr), attrVarTarget)
					# else if ctrl have mirrors attr's
					elif cmds.attributeQuery( 'translateXMirror', node=sourceControl, exists=True ):
						if(attr != "translateX" and attr != "translateY" and attr != "translateZ"): # disable translate mirror for matrix mirror
							# mirror atribute and set
							if cmds.getAttr(sourceControl + "." + attr + "Mirror"):
								cmds.setAttr((targetControl + "." + attr), attrVarSource * -1)
								cmds.setAttr((sourceControl + "." + attr), attrVarTarget * -1)
							# else, copy attr and set
							else:
								cmds.setAttr((targetControl + "." + attr), attrVarSource )
								cmds.setAttr((sourceControl + "." + attr), attrVarTarget )
						if(matrixMirror == False): # enable translate mirror for not matrix mirror
							if (attr == "translateX" or attr == "translateY" or attr == "translateZ"):
								# mirror atribute and set
								if cmds.getAttr(sourceControl + "." + attr + "Mirror"):
									cmds.setAttr((targetControl + "." + attr), attrVarSource * -1)
									cmds.setAttr((sourceControl + "." + attr), attrVarTarget * -1)
								# else, copy attr and set
								else:
									cmds.setAttr((targetControl + "." + attr), attrVarSource )
									cmds.setAttr((sourceControl + "." + attr), attrVarTarget )
					else:
						print "Control is not SET !!!!!!!!!!!!!"
				# another attr is coping
				else:
					try:
						cmds.setAttr((targetControl + "." + attr), attrVarSource)
						cmds.setAttr((sourceControl + "." + attr), attrVarTarget)
					except:
						#print target, "cannot modify"
						pass

		if side == "c":
			for attr in attrList:
				try:
					attrVarSource = cmds.getAttr(sourceControl + "." + attr)
				except:
					print target, "cannot getAttr"
					pass

				# if attr is translate or rotate
				if attr in mirrorAttrLis:
					# else if ctrl have mirrors attr's
					if cmds.attributeQuery( 'translateXMirror', node=sourceControl, exists=True ):
						# mirror atribute and set
						if cmds.getAttr(sourceControl + "." + attr + "Mirror"):
							cmds.setAttr((targetControl + "." + attr), attrVarSource * -1)
					else:
						print "Control is not SET !!!!!!!!!!!!!"


		if matrixMirror:
			mirrorByMatrix(sourceControl, targetControl, ns)



def newSymmetry(flip=False): 
	
	def matrixMirror_flipped(flip=False):
		
		# set float lists
		source_floatList = cmds.xform(control, q=True, matrix=1, worldSpace=1)
		target_floatList = cmds.xform(target, q=True, matrix=1, worldSpace=1)
		rotOrderSource = cmds.getAttr(control+'.rotateOrder')
		rotOrderTarget = cmds.getAttr(target+'.rotateOrder')
		# print source_floatList
	
		mirrorLoc_floatList = cmds.xform(ns + "mirror_loc",q=True,matrix=1, worldSpace=1)
		vector_floatList = [-1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
		flip_floatList = [-1.0, 0.0, 0, 0.0, 0.0, 1.0, 0.0, 0.0, 0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
	
		# Make matrixes
		source_matrix = om.MMatrix()
		om.MScriptUtil.createMatrixFromList(source_floatList,source_matrix)
		
		target_matrix = om.MMatrix()
		om.MScriptUtil.createMatrixFromList(target_floatList,target_matrix)		
	
		mirrorLoc_matrix = om.MMatrix()
		om.MScriptUtil.createMatrixFromList(mirrorLoc_floatList,mirrorLoc_matrix)
		mirror_transformMatrix = om.MTransformationMatrix(mirrorLoc_matrix)
		mirrorLoc_inverse_matrix = mirror_transformMatrix.asMatrixInverse()
	
		vector_matrix = om.MMatrix()
		om.MScriptUtil.createMatrixFromList(vector_floatList,vector_matrix )
	
		flip_matrix = om.MMatrix() # for flip on 180 angle
		om.MScriptUtil.createMatrixFromList(flip_floatList,flip_matrix )	
	
		# Solve
		final_matrix = flip_matrix * source_matrix * mirrorLoc_inverse_matrix * vector_matrix * mirrorLoc_matrix
		final_transformMatrix = om.MTransformationMatrix(final_matrix)
	
		# Move
		t = final_transformMatrix.translation(om.MSpace.kWorld)
		cmds.move( t.x, t.y, t.z, target, absolute=True, worldSpace=True )
	
		# get rotation from matrix
		eulerRot = final_transformMatrix.eulerRotation()
		# modify rotation by rotateOrder
		eulerRot.reorderIt(rotOrderTarget)
		# convert from radians and rotate target
		angles = [math.degrees(angle) for angle in (eulerRot.x, eulerRot.y, eulerRot.z)]
		cmds.rotate(angles[0], angles[1], angles[2], target, ws=True)	
		
		
		# --------------- flip -----------------
		if flip:
			print control, target
			
			# Solve
			final_matrix = flip_matrix * target_matrix * mirrorLoc_inverse_matrix * vector_matrix * mirrorLoc_matrix
			final_transformMatrix = om.MTransformationMatrix(final_matrix)
		
			# Move
			t = final_transformMatrix.translation(om.MSpace.kWorld)
			cmds.move( t.x, t.y, t.z, control, absolute=True, worldSpace=True )
		
			# get rotation from matrix
			eulerRot = final_transformMatrix.eulerRotation()
			# modify rotation by rotateOrder
			eulerRot.reorderIt(rotOrderSource)
			# convert from radians and rotate source
			angles = [math.degrees(angle) for angle in (eulerRot.x, eulerRot.y, eulerRot.z)]
			cmds.rotate(angles[0], angles[1], angles[2], control, ws=True)			
	
	
	controls = cmds.ls(selection=True)

	for control in controls:
		#Get control name without ns
		ctrlName = control.split(":")[-1]

		#Get namespases
		ns = control.split(ctrlName)[:-1]
		if len(ns) == 0:
			ns = ""
		else:
			ns = ns[0]

		#Get side
		side = ctrlName.split("_")[0]
		if side != "l" and side != "r":
			side = "c"
			
		#Get name without side prefix
		nameUnside = ctrlName[2:]
		if side == "c":
			nameUnside = ctrlName

		#Get target control
		if side == "c":
			target = ctrlName
		elif side == "l":
			target = "r_" + nameUnside
		elif side == "r":
			target = "l_" + nameUnside
		
		target = ns + target

		# get type of the mirror
		mirrored = False
		if cmds.attributeQuery( 'mirrored', node=control, exists=True ):
			mirrored = cmds.getAttr(control + ".mirrored")

		# get attr list
		attrList = []
		attrListNonkeyable = []
		
		attrListKeyable = cmds.listAttr(control, keyable=True )
		if type(attrListKeyable) != list :
			attrListKeyable = []
		attrListNonkeyable = cmds.listAttr(control, channelBox = True )
		if type(attrListNonkeyable) != list :
			attrListNonkeyable = []
		attrList = attrListKeyable + attrListNonkeyable
		print control, attrList
		
		if side != "c":
			# copy all attr values
			if mirrored:
				for attr in attrList:
					try:
						# get attrs values
						attrVarSource = cmds.getAttr(control + "." + attr)
						attrVarTarget = cmds.getAttr(target + "." + attr)
						# set to target and source for flip
						cmds.setAttr((target + "." + attr), attrVarSource)
						if flip:
							cmds.setAttr((control + "." + attr), attrVarTarget)
					except:
						print target, "cannot getAttr"
			# matrix mirror on some controls
			if not mirrored:
				matrixMirror_flipped(flip)
				for attr in attrList:
					if attr not in mirrorAttrLis:
						try:
							# get attrs values
							attrVarSource = cmds.getAttr(control + "." + attr)
							attrVarTarget = cmds.getAttr(target + "." + attr)
							# set to target and source for flip
							cmds.setAttr((target + "." + attr), attrVarSource)
							if flip:
								cmds.setAttr((control + "." + attr), attrVarTarget)
						except:
							print target, "cannot getAttr"					

		else:
			# copy all attr values
			for attr in attrList:
				attrVarSource = cmds.getAttr(control + "." + attr)
				# for pelvis mirror only rotation
				if ctrlName == "pelvis":
					if attr == "rotateZ":
						if flip:						
							cmds.setAttr((target + "." + attr), attrVarSource*-1)
						else:
							cmds.setAttr((target + "." + attr), 0)					
				# for other controls:
				else:
					try:
						if attr == "translateX" or attr == "rotateY" or attr == "rotateZ":
							if flip:						
								cmds.setAttr((target + "." + attr), attrVarSource*-1)
							else:							
								cmds.setAttr((target + "." + attr), 0)
					except:
						print target, "cannot getAttr"			
		

def setupMirrorControls(m=False, tx=False, ty=False, tz=False, rx=False, ry=False, rz=False):
	# Add mirror attribute to selected controls
	objs = cmds.ls(sl=True)
	if len(objs) == 0:
		print "Select controls"
	else:
		for obj in objs:
			#Add attr's
			if cmds.attributeQuery( 'mirrored', node=obj, exists=True ) == False:
				cmds.addAttr(obj, longName="mirrored", attributeType='bool')
			if cmds.attributeQuery( 'translateXMirror', node=obj, exists=True ) == False:
				cmds.addAttr(obj, longName="translateXMirror", attributeType='bool')
				cmds.addAttr(obj, longName="translateYMirror", attributeType='bool')
				cmds.addAttr(obj, longName="translateZMirror", attributeType='bool')
				cmds.addAttr(obj, longName="rotateXMirror", attributeType='bool')
				cmds.addAttr(obj, longName="rotateYMirror", attributeType='bool')
				cmds.addAttr(obj, longName="rotateZMirror", attributeType='bool')
			if cmds.attributeQuery( 'matrixMirror', node=obj, exists=True ) == False:
				cmds.addAttr(obj, longName="matrixMirror", attributeType='bool')
			if cmds.attributeQuery( 'constraintMirror', node=obj, exists=True ) == False:
				cmds.addAttr(obj, longName="constraintMirror", attributeType='bool')			
			#if cmds.attributeQuery( 'switchAxeXY', node=obj, exists=True ) == False:
				#cmds.addAttr(obj, longName="switchAxeXY", attributeType='bool')
				#cmds.addAttr(obj, longName="switchAxeYZ", attributeType='bool')
				#cmds.addAttr(obj, longName="switchAxeXZ", attributeType='bool')
			#Set attr's
			#cmds.setAttr((obj + ".mirrored"), m)
			#cmds.setAttr((obj + ".translateXMirror"), tx)
			#cmds.setAttr((obj + ".translateYMirror"), ty)
			#cmds.setAttr((obj + ".translateZMirror"), tz)
			#cmds.setAttr((obj + ".rotateXMirror"), rx)
			#cmds.setAttr((obj + ".rotateYMirror"), ry)
			#cmds.setAttr((obj + ".rotateZMirror"), rz)
			pass