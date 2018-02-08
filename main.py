#!/usr/bin/env python
# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel
import pymel.core as pm
import maya.OpenMayaUI as omui
import maya.api.OpenMaya as om
from functools import partial

# import PySide.QtGui as QWidgets
#from PySide import QtCore, QtGui
from Qt import QtWidgets, QtCore, QtGui
try:
	from shiboken import wrapInstance
except:
	from shiboken2 import wrapInstance

import os, imp, types, webbrowser, logging, inspect, traceback, io, json
import utils
import matchRig_mainWindow as mainWindow
import matchRig_bakeWindow as bakeWindow
reload(utils)

import pk_selector_switchIKFK
reload(pk_selector_switchIKFK)

logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)



# Compile Py from Ui u
#utils.compileUI()
#reload(mainWindow)
#reload(bakeWindow)

fileName = __name__.split('.')[-1]
rootFolder = __file__.split(fileName)[0]
data_file = rootFolder + 'data.json'

def mayaMainWindow():
	mainWindowPtr = omui.MQtUtil.mainWindow()
	return wrapInstance(long(mainWindowPtr), QtWidgets.QWidget)


class MainWindow(QtWidgets.QMainWindow, mainWindow.Ui_Dialog):
	def __init__(self, parent=mayaMainWindow()):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		logger.debug("Start " + inspect.stack()[0][3])

		moduleName = __name__.split('.')[0]
		self.modulePath = os.path.abspath(imp.find_module(moduleName)[1])
		self.back_btn.setIcon(QtGui.QIcon(self.modulePath+"/back.png"))

		mel.eval('source "%s/pk_makeControls.mel"' %self.modulePath.replace('\\', '/'))

		self.setFixedSize(self.size())

		self.sidePos = ""
		self.l_name = 'l'
		self.r_name = 'r'

		self.buttons = {}
		self.buttons["head"] = ["", self.head_btn]
		self.buttons["neck"] = ["", self.neck_btn]
		self.buttons["chest"] = ["", self.chest_btn]
		self.buttons["shoulder"] = ["", self.shoulder_btn]
		self.buttons["pelvis"] = ["", self.pelvis_btn]
		self.buttons["forearm"] = ["", self.forearm_btn]
		self.buttons["arm"] = ["", self.arm_btn]
		self.buttons["hand"] = ["", self.hand_btn]
		self.buttons["hip"] = ["", self.hip_btn]
		self.buttons["leg"] = ["", self.leg_btn]
		self.buttons["foot"] = ["", self.foot_btn]
		self.buttons["toe"] = ["", self.toe_btn]
		self.buttons["spine_1"] = ["", self.spine_1_btn]
		self.buttons["spine_2"] = ["", self.spine_2_btn]
		self.buttons["spine_3"] = ["", self.spine_3_btn]
		self.buttons["spine_4"] = ["", self.spine_4_btn]
		self.buttons["spine_5"] = ["", self.spine_5_btn]
		self.buttons["forearm_1"] = ["", self.forearm_1_btn]
		self.buttons["forearm_2"] = ["", self.forearm_2_btn]
		self.buttons["forearm_3"] = ["", self.forearm_3_btn]
		self.buttons["arm_1"] = ["", self.arm_1_btn]
		self.buttons["arm_2"] = ["", self.arm_2_btn]
		self.buttons["arm_3"] = ["", self.arm_3_btn]
		self.buttons["hip_1"] = ["", self.hip_1_btn]
		self.buttons["hip_2"] = ["", self.hip_2_btn]
		self.buttons["hip_3"] = ["", self.hip_3_btn]
		self.buttons["leg_1"] = ["", self.leg_1_btn]
		self.buttons["leg_2"] = ["", self.leg_2_btn]
		self.buttons["leg_3"] = ["", self.leg_3_btn]
		self.buttons["finger_1_1"] = ["", self.finger_1_1_btn]
		self.buttons["finger_1_2"] = ["", self.finger_1_2_btn]
		self.buttons["finger_1_3"] = ["", self.finger_1_3_btn]
		self.buttons["finger_2_1"] = ["", self.finger_2_1_btn]
		self.buttons["finger_2_2"] = ["", self.finger_2_2_btn]
		self.buttons["finger_2_3"] = ["", self.finger_2_3_btn]
		self.buttons["finger_3_1"] = ["", self.finger_3_1_btn]
		self.buttons["finger_3_2"] = ["", self.finger_3_2_btn]
		self.buttons["finger_3_3"] = ["", self.finger_3_3_btn]
		self.buttons["finger_4_1"] = ["", self.finger_4_1_btn]
		self.buttons["finger_4_2"] = ["", self.finger_4_2_btn]
		self.buttons["finger_4_3"] = ["", self.finger_4_3_btn]
		self.buttons["finger_5_1"] = ["", self.finger_5_1_btn]
		self.buttons["finger_5_2"] = ["", self.finger_5_2_btn]
		self.buttons["finger_5_3"] = ["", self.finger_5_3_btn]
		self.buttons["weapon_1"] = ["", self.weapon_1_btn]
		self.buttons["acc_1"] = ["", self.acc_1_btn]
		self.buttons["symWeapon_1"] = ["", self.symWeapon_1_btn]
		self.buttons["addObject_1"] = ["", self.addObject_1_btn]
		self.buttons["addObject_2"] = ["", self.addObject_2_btn]
		self.buttons["addObject_3"] = ["", self.addObject_3_btn]
		self.buttons["addObject_4"] = ["", self.addObject_4_btn]
		self.buttons["addObject_5"] = ["", self.addObject_5_btn]
		self.buttons["addObject_6"] = ["", self.addObject_6_btn]
		self.buttons["addObject_7"] = ["", self.addObject_7_btn]
		self.buttons["addObject_8"] = ["", self.addObject_8_btn]
		self.buttons["addObject_9"] = ["", self.addObject_9_btn]

		self.mainButtonsList = []
		self.mainButtonsList.append(self.head_btn)
		self.mainButtonsList.append(self.neck_btn)
		self.mainButtonsList.append(self.chest_btn)
		self.mainButtonsList.append(self.shoulder_btn)
		self.mainButtonsList.append(self.pelvis_btn)
		self.mainButtonsList.append(self.forearm_btn)
		self.mainButtonsList.append(self.arm_btn)
		self.mainButtonsList.append(self.hand_btn)
		self.mainButtonsList.append(self.hip_btn)
		self.mainButtonsList.append(self.leg_btn)
		self.mainButtonsList.append(self.foot_btn)
		self.mainButtonsList.append(self.toe_btn)

		self.addButtonsList = []
		self.addButtonsList.append(self.spine_1_btn)		
		self.addButtonsList.append(self.spine_2_btn)		
		self.addButtonsList.append(self.spine_3_btn)		
		self.addButtonsList.append(self.spine_4_btn)		
		self.addButtonsList.append(self.spine_5_btn)
		self.addButtonsList.append(self.forearm_1_btn)
		self.addButtonsList.append(self.forearm_2_btn)
		self.addButtonsList.append(self.forearm_3_btn)
		self.addButtonsList.append(self.arm_1_btn)
		self.addButtonsList.append(self.arm_2_btn)
		self.addButtonsList.append(self.arm_3_btn)
		self.addButtonsList.append(self.hip_1_btn)
		self.addButtonsList.append(self.hip_2_btn)
		self.addButtonsList.append(self.hip_3_btn)
		self.addButtonsList.append(self.leg_1_btn)
		self.addButtonsList.append(self.leg_2_btn)
		self.addButtonsList.append(self.leg_3_btn)
		self.addButtonsList.append(self.finger_1_1_btn)
		self.addButtonsList.append(self.finger_1_2_btn)
		self.addButtonsList.append(self.finger_1_3_btn)
		self.addButtonsList.append(self.finger_2_1_btn)
		self.addButtonsList.append(self.finger_2_2_btn)
		self.addButtonsList.append(self.finger_2_3_btn)
		self.addButtonsList.append(self.finger_3_1_btn)
		self.addButtonsList.append(self.finger_3_2_btn)
		self.addButtonsList.append(self.finger_3_3_btn)
		self.addButtonsList.append(self.finger_4_1_btn)
		self.addButtonsList.append(self.finger_4_2_btn)
		self.addButtonsList.append(self.finger_4_3_btn)
		self.addButtonsList.append(self.finger_5_1_btn)
		self.addButtonsList.append(self.finger_5_2_btn)
		self.addButtonsList.append(self.finger_5_3_btn)
		self.addButtonsList.append(self.weapon_1_btn)
		self.addButtonsList.append(self.acc_1_btn)
		self.addButtonsList.append(self.symWeapon_1_btn)
		self.addButtonsList.append(self.addObject_1_btn)
		self.addButtonsList.append(self.addObject_2_btn)
		self.addButtonsList.append(self.addObject_3_btn)
		self.addButtonsList.append(self.addObject_4_btn)
		self.addButtonsList.append(self.addObject_5_btn)
		self.addButtonsList.append(self.addObject_6_btn)
		self.addButtonsList.append(self.addObject_7_btn)
		self.addButtonsList.append(self.addObject_8_btn)
		self.addButtonsList.append(self.addObject_9_btn)

		self.connectSignals()

		self.initUI()

	def connectSignals(self):
		logger.debug("Start " + inspect.stack()[0][3])

		for b in self.mainButtonsList:
			b.clicked.connect(self.setJoint)

		for b in self.addButtonsList:
			b.clicked.connect(self.setJoint)
		
		self.symWeapon_cb.clicked.connect(self.updateUI)

		self.reset_btn.clicked.connect(self.reset)
		self.match_btn.clicked.connect(self.match)
		self.connect_btn.clicked.connect(self.connectRig)
		self.importRig_btn.clicked.connect(self.importRig)

		self.sidesSet_btn.clicked.connect(self.setSidesNaming)
		self.posersVis_cb.clicked.connect(partial(self.visToggle, self.posersVis_cb, 'posers'))
		self.controlsVis_cb.clicked.connect(partial(self.visToggle, self.controlsVis_cb, 'controls'))
		self.jointsVis_cb.clicked.connect(partial(self.visToggle, self.jointsVis_cb, 'skinJoints'))
		self.jointsTempl_cb.clicked.connect(partial(self.visToggle, self.jointsTempl_cb, 'joints_template'))

		self.save_btn.clicked.connect(self.saveMap)
		self.load_btn.clicked.connect(self.loadMap)

	def importRig(self):

		# duplicate sceleton and rename it
		joints = cmds.ls(type="joint")
		
		try:
			root = cmds.listRelatives(joints[0], parent=1, fullPath=1)[0].split("|")[1]
			root = cmds.rename(root, "skin_"+root)
		except: 
			try:
				root = joints[0]
			except:
				cmds.warning("Can not find sceleton root")
				return
		#print "ROOT", root
		skin_root = cmds.group(root, n="skin_root")
		for j in joints:
			#print j
			j = cmds.rename(j, "skin_"+j)

		input_root = cmds.duplicate(skin_root, n="input_root")
		childs = cmds.listRelatives("input_root", children=1, allDescendents=1, f=1)
		for c in childs:
			#if cmds.objectType(c) == "joint":
			cmds.rename(c, c.split("|")[-1].replace("skin_", "input_"))


		cmds.hide("skin_root")


		# import rig
		#filePath = self.modulePath + "/match_rig.ma"
		filePath = self.modulePath + "/match_rig_nekki.ma"
		cmds.file(filePath, pr=1, i=1, type="mayaAscii", rpr="match_rig_nekki", mergeNamespacesOnClash=False, options="v=0;")

		for o in ['head', 'neck', 'spine', 'l_arm', 'r_arm', 'l_leg', 'r_leg', 'l_shoulder', 'r_shoulder', 'l_foot', 'r_foot']:
			cmds.showHidden(o+'_skinJoints')		

		
		# save default values
		utils.pyToAttr('character.uiMatchButtons', {})
		utils.pyToAttr('character.sidePos', self.sidePos)
		utils.pyToAttr('character.l_side', self.l_name)
		utils.pyToAttr('character.r_side', self.r_name)
		
		utils.pyToAttr('character.posersVis', 0)
		utils.pyToAttr('character.controlsVis', 1)
		utils.pyToAttr('character.jointsVis', 1)
		utils.pyToAttr('character.jointsTempl', 0)
		
		self.initUI()

	def setSidesNaming(self):
		self.l_name = self.leftSide_lineEdit.text()
		self.r_name = self.rigthSide_lineEdit.text()

		utils.pyToAttr('character.l_side', self.l_name)
		utils.pyToAttr('character.r_side', self.r_name)
		
		if self.buttons['hand'][0] != "":
			
			# save prefix type
			array = self.buttons['hand'][0].split("_")
			if array[0] == 'input':
				del array[0]
			if array[0] == self.l_name:
				self.sidePos = "prefix"
			elif array[-1] == self.l_name:
				self.sidePos = "suffix"
			elif self.l_name in array[-1]:
				self.sidePos = "suffix_merged"
			elif self.l_name in array:
				self.sidePos = "middle"
			utils.pyToAttr('character.sidePos', self.sidePos)		

	def setJoint(self):

		# get current button and its name
		btn = self.sender()
		jointName = btn.objectName().split('_btn')[0]		

		# select saved joint on ctrl pressed
		modifiers = QtWidgets.QApplication.keyboardModifiers()
		if modifiers == QtCore.Qt.ControlModifier:
			savedJoint = self.buttons[jointName][0]
			if savedJoint == "":
				cmds.select(clear=1)
			else:
				cmds.select(savedJoint)
			return

		# get selected joint
		sel = cmds.ls(sl=1)
		if len(sel) != 1:
			cmds.warning("Select one joint")
			return
		j = sel[0]

		# clear current joint from another button assign
		for i in self.buttons:
			if self.buttons[i][0] == j:
				self.buttons[i][0] = ""
				break

		# assign current joint to button
		self.buttons[jointName][0] = j

		# save prefix type
		if jointName == "hand":
			array = j.split("_")
			if array[0] == self.l_name:
				self.sidePos = "prefix"
			elif array[-1] == self.l_name:
				self.sidePos = "suffix"
			elif self.l_name in array[-1]:
				self.sidePos = "suffix_merged"
			elif self.l_name in array:
				self.sidePos = "middle"
			utils.pyToAttr('character.sidePos', self.sidePos)		
			
		# save root joint
		elif jointName == "pelvis":
			utils.pyToAttr('character.rootJoint', j)

		# update and save
		self.reset_btn.setEnabled(True)
		self.updateUI()
		self.save()

	def initUI(self):
		
		if cmds.objExists('rig'):
			self.modules = cmds.listRelatives('rig')

		if not cmds.objExists("character"):
			for b in self.mainButtonsList:
				b.setStyleSheet("")
				b.setEnabled(False)
			for b in self.addButtonsList:
				b.setStyleSheet("")
				b.setEnabled(False)

			self.match_btn.setEnabled(False)
			self.connect_btn.setEnabled(False)
			self.reset_btn.setEnabled(False)
			
			self.sides_gb.setEnabled(False)
			self.display_gb.setEnabled(False)
			self.map_gb.setEnabled(False)
			self.symWeapon_cb.setEnabled(False)
			
		else:
			for b in self.mainButtonsList:
				b.setStyleSheet("background-color: rgb(40, 70, 140)")
				b.setEnabled(True)
			for b in self.addButtonsList:
				b.setStyleSheet("")
				b.setEnabled(True)

				self.importRig_btn.setEnabled(False)
				
				self.sides_gb.setEnabled(True)
				self.display_gb.setEnabled(True)
				self.map_gb.setEnabled(True)				
				self.symWeapon_cb.setEnabled(True)				

			self.load()
			self.updateUI()

	def updateUI(self):
		filledMainButtons = []

		# fill buttons assigns
		for b in self.buttons:
			if self.buttons[b][0] == "":
				if b[-1].isdigit():
					self.buttons[b][1].setStyleSheet("")
				else:
					self.buttons[b][1].setStyleSheet("background-color: rgb(40, 70, 140)")
			else:
				self.buttons[b][1].setStyleSheet("background-color: rgb(140, 70, 0)")

				if not b[-1].isdigit():
					filledMainButtons.append(b)

		# enable match/connect buttons
		if len(filledMainButtons) == 12:
			self.match_btn.setEnabled(True)
			self.connect_btn.setEnabled(True)
		else:
			self.match_btn.setEnabled(False)
			self.connect_btn.setEnabled(False)
			
		# update symmetry buttons
		if not self.symWeapon_cb.isChecked():
			self.symWeapon_1_btn.setEnabled(True)
		else:
			self.symWeapon_1_btn.setEnabled(False)
			self.symWeapon_1_btn.setStyleSheet("")

		# fill sides naming waidgets
		self.leftSide_lineEdit.setText(self.l_name)
		self.rigthSide_lineEdit.setText(self.r_name)

		# update display checkboxes
		try:
			self.posersVis_cb.setChecked(utils.attrToPy('character.posersVis'))
			self.controlsVis_cb.setChecked(utils.attrToPy('character.controlsVis'))
			self.jointsVis_cb.setChecked(utils.attrToPy('character.jointsVis'))
			self.jointsTempl_cb.setChecked(utils.attrToPy('character.jointsTempl'))
		except: pass

	def save(self):
		print "save"

		filledButtons = {}

		for b in self.buttons:
			if self.buttons[b][0] != "":
				filledButtons[b] = self.buttons[b][0]

		utils.pyToAttr('character.uiMatchButtons', filledButtons)

	def load(self):
		
		try:
			self.sidePos = utils.attrToPy('character.sidePos')
			self.l_name = utils.attrToPy('character.l_side')
			self.r_name = utils.attrToPy('character.r_side')
		except:
			utils.pyToAttr('character.sidePos', self.sidePos)
			utils.pyToAttr('character.l_side', self.l_name)
			utils.pyToAttr('character.r_side', self.r_name)			

		filledButtons = utils.attrToPy('character.uiMatchButtons')

		for b in filledButtons:
			self.buttons[b][0] = filledButtons[b]

	def visToggle(self, cb, obj_type):
		logger.debug(traceback.extract_stack()[-1][2])

		state = cb.isChecked()

		def updateVis():
			for m in self.modules:
				m_name = m.split('_rig')[0]
				try:
					if state == 0:
						cmds.hide(m_name+'_'+obj_type)
					else:
						cmds.showHidden(m_name+'_'+obj_type)
				except: pass

		def updateTemplate():
			for m in self.modules:
				try:
					if state == 0:
						cmds.setAttr(m[:-4]+"_skinJoints.template", 0)
					else:
						cmds.setAttr(m[:-4]+"_skinJoints.template", 1)
				except: pass

		if obj_type == 'posers': 
			utils.pyToAttr('character.posersVis', state!=0)	
			updateVis()
		elif obj_type == 'controls': 
			utils.pyToAttr('character.controlsVis', state!=0)
			cmds.setAttr("character.bodyControls", state!=0)
			updateVis()
		elif obj_type == 'skinJoints': 
			utils.pyToAttr('character.jointsVis', state!=0)		
			updateVis()
		elif obj_type == 'joints_template': 
			utils.pyToAttr('character.jointsTempl', state!=0)		
			updateTemplate()

	def reset(self):
		self.buttons = {}
		self.buttons["head"] = ["", self.head_btn]
		self.buttons["neck"] = ["", self.neck_btn]
		self.buttons["chest"] = ["", self.chest_btn]
		self.buttons["shoulder"] = ["", self.shoulder_btn]
		self.buttons["pelvis"] = ["", self.pelvis_btn]
		self.buttons["forearm"] = ["", self.forearm_btn]
		self.buttons["arm"] = ["", self.arm_btn]
		self.buttons["hand"] = ["", self.hand_btn]
		self.buttons["hip"] = ["", self.hip_btn]
		self.buttons["leg"] = ["", self.leg_btn]
		self.buttons["foot"] = ["", self.foot_btn]
		self.buttons["toe"] = ["", self.toe_btn]
		self.buttons["spine_1"] = ["", self.spine_1_btn]
		self.buttons["spine_2"] = ["", self.spine_2_btn]
		self.buttons["spine_3"] = ["", self.spine_3_btn]
		self.buttons["spine_4"] = ["", self.spine_4_btn]
		self.buttons["spine_5"] = ["", self.spine_5_btn]
		self.buttons["forearm_1"] = ["", self.forearm_1_btn]
		self.buttons["forearm_2"] = ["", self.forearm_2_btn]
		self.buttons["forearm_3"] = ["", self.forearm_3_btn]
		self.buttons["arm_1"] = ["", self.arm_1_btn]
		self.buttons["arm_2"] = ["", self.arm_2_btn]
		self.buttons["arm_3"] = ["", self.arm_3_btn]
		self.buttons["hip_1"] = ["", self.hip_1_btn]
		self.buttons["hip_2"] = ["", self.hip_2_btn]
		self.buttons["hip_3"] = ["", self.hip_3_btn]
		self.buttons["leg_1"] = ["", self.leg_1_btn]
		self.buttons["leg_2"] = ["", self.leg_2_btn]
		self.buttons["leg_3"] = ["", self.leg_3_btn]		
		self.buttons["finger_1_1"] = ["", self.finger_1_1_btn]
		self.buttons["finger_1_2"] = ["", self.finger_1_2_btn]
		self.buttons["finger_1_3"] = ["", self.finger_1_3_btn]
		self.buttons["finger_2_1"] = ["", self.finger_2_1_btn]
		self.buttons["finger_2_2"] = ["", self.finger_2_2_btn]
		self.buttons["finger_2_3"] = ["", self.finger_2_3_btn]
		self.buttons["finger_3_1"] = ["", self.finger_3_1_btn]
		self.buttons["finger_3_2"] = ["", self.finger_3_2_btn]
		self.buttons["finger_3_3"] = ["", self.finger_3_3_btn]
		self.buttons["finger_4_1"] = ["", self.finger_4_1_btn]
		self.buttons["finger_4_2"] = ["", self.finger_4_2_btn]
		self.buttons["finger_4_3"] = ["", self.finger_4_3_btn]
		self.buttons["finger_5_1"] = ["", self.finger_5_1_btn]
		self.buttons["finger_5_2"] = ["", self.finger_5_2_btn]
		self.buttons["finger_5_3"] = ["", self.finger_5_3_btn]
		self.buttons["weapon_1"] = ["", self.weapon_1_btn]
		self.buttons["acc_1"] = ["", self.acc_1_btn]		

		self.save()
		self.updateUI()

		cmds.select(clear=1)

	def match(self):

		def matchPos(src, tgt):
			if src == "" or self.buttons[src][0] == "":
				return
			#print "matched ", src, tgt
			c = cmds.pointConstraint(self.buttons[src][0], tgt, mo=0)
			cmds.delete(c)

		def matchTransform(src, tgt):
			if src == "" or self.buttons[src][0] == "":
				return
			#print "matched ", src, tgt
			c = cmds.parentConstraint(self.buttons[src][0], tgt, mo=0)
			cmds.delete(c)

		matchPos("pelvis", "spine_mainPoser")
		matchPos("chest", "chest_mainPoser")
		matchPos("neck", "neck_mainPoser")
		matchPos("head", "head_poser")
		matchPos("shoulder", "shoulder_poser")
		matchPos("forearm", "arm_poser")
		matchPos("arm", "elbow_poser")
		matchPos("hip", "hip_poser")
		matchPos("leg", "knee_poser")
		matchPos("hand", "hand_mainPoser")
		matchPos("toe", "l_foot_mainPoser")

		# move and orient foot mainPoser
		c = cmds.aimConstraint(self.buttons["foot"][0], "l_foot_mainPoser", aimVector=(0,0,-1))
		cmds.delete(c)
		cmds.setAttr("l_foot_mainPoser.rotateX", 0)
		cmds.setAttr("l_foot_mainPoser.rotateZ", 0)

		matchPos("foot", "l_heel_poser")

	def connectRig(self):
			
		def connect(src, tgt, con="par", sym=False, offset=False):
			#print "connect ", src, tgt
			srcJnt = self.buttons[src][0]

			if src == "" or srcJnt == "":
				return
			#print "matched ", src, tgt
			if sym:
				if self.sidePos == "prefix":
					srcJnt = "input_" + self.r_name + srcJnt[7:]
				elif self.sidePos == "suffix":
					srcJnt = srcJnt[:-1] + self.r_name
				elif self.sidePos == "suffix_merged" or self.sidePos == "middle":
					srcJnt = srcJnt.replace(self.l_name, self.r_name)
			
			loc = cmds.spaceLocator(n=tgt+"_connectRig_loc")[0]
			cmds.parent(loc, srcJnt)
			constr = cmds.parentConstraint(tgt , loc, mo=0)
			cmds.delete(constr)
			
			if con == "t":
				cmds.pointConstraint(loc , tgt, mo=0)
			elif con == "r":
				cmds.orientConstraint(loc , tgt, mo=0)
			else:
				cmds.parentConstraint(loc , tgt, mo=0)

		def connectVectorSystem(in0, in1, in2, ctrl, sym=False):

			j0 = self.buttons[in0][0]
			j1 = self.buttons[in1][0]
			j2 = self.buttons[in2][0]

			if sym:
				if self.sidePos == "prefix":
					j0 = "input_" + self.r_name + j0[7:]
					j1 = "input_" + self.r_name + j1[7:]
					j2 = "input_" + self.r_name + j2[7:]
				elif self.sidePos == "suffix":
					j0 = j0[:-1] + self.r_name			
					j1 = j1[:-1] + self.r_name		
					j2 = j2[:-1] + self.r_name
				elif self.sidePos == "suffix_merged" or self.sidePos == "middle":
					j0 = j0.replace(self.l_name, self.r_name)	
					j1 = j1.replace(self.l_name, self.r_name)	
					j2 = j2.replace(self.l_name, self.r_name)

			# make offset vector system
			loc1 = cmds.spaceLocator()[0]
			cmds.pointConstraint(j0, j2, loc1, mo=0)
			loc2 = cmds.spaceLocator()[0]
			cmds.parent(loc1, j1)
			cmds.parent(loc2, loc1)
			utils.resetAttrs(loc2)
			cmds.aimConstraint(j1, loc1, mo=0)
			cmds.pointConstraint(j1, loc2, mo=0)
			loc3 = cmds.spaceLocator()[0]
			cmds.parent(loc3, loc2)
			utils.resetAttrs(loc3)
			cmds.setAttr(loc3+".tx", 20)

			# connect vector control to system		
			cmds.pointConstraint(loc3, ctrl, mo=0)[0]

		# connect rig controls to input sceleton
		connect("pelvis", "pelvis", "par", False)
		connect("chest", "chest", "par", False)
		connect("neck", "neck", "par", False)
		connect("shoulder", "l_shoulder", "par", False)
		connect("shoulder", "r_shoulder", "par", True)
		connect("head", "head", "par", False)
		connect("hand", "l_hand", "par", False)
		connect("hand", "r_hand", "par", True)
		connect("foot", "l_foot", "par", False)
		connect("foot", "r_foot", "par", True)
		connect("toe", "l_toeIk", "r", False)
		connect("toe", "r_toeIk", "r", True)
		connect("toe", "l_toeFk", "r", False)
		connect("toe", "r_toeFk", "r", True)
		connect("foot", "l_heelFk", "r", False)
		connect("foot", "r_heelFk", "r", True)
		connect("leg", "l_leg", "r", False)
		connect("leg", "r_leg", "r", True)
		connect("hip", "l_upLeg", "r", False)
		connect("hip", "r_upLeg", "r", True)
		connect("forearm", "l_arm", "r", False)
		connect("forearm", "r_arm", "r", True)
		connect("arm", "l_forearm", "r", False)
		connect("arm", "r_forearm", "r", True)
		connect("hand", "l_wrist", "r", False)
		connect("hand", "r_wrist", "r", True)
		
		connectVectorSystem("hip", "leg", "foot", "l_knee")
		connectVectorSystem("hip", "leg", "foot", "r_knee", True)
		connectVectorSystem("forearm", "arm", "hand", "l_elbow")
		connectVectorSystem("forearm", "arm", "hand", "r_elbow", True)
		

		# connect main rig joints to skin sceleton
		def connectSkinJoint(src, tgtName, sym=False):
			
			tgt = self.buttons[tgtName][0].replace("input", "skin")
			if tgt == "":
				return		
			if sym:
				if self.sidePos == "prefix":
					tgt = "skin_" + self.r_name + tgt[6:]
				elif self.sidePos == "suffix":
					tgt = tgt[:-1] + self.r_name
				elif self.sidePos == "suffix_merged" or self.sidePos == "middle":
					tgt = tgt.replace(self.l_name, self.r_name)
			cmds.parentConstraint(src, tgt, mo=1)	
			try:
				cmds.scaleConstraint(src, tgt, mo=1)
			except: pass
			
	
		connectSkinJoint("pelvis_joint", "pelvis")
		connectSkinJoint("chest_joint", "chest")
		connectSkinJoint("neck_1_joint", "neck")
		connectSkinJoint("head_joint", "head")
		connectSkinJoint("l_shoulder_joint_1", "shoulder")
		connectSkinJoint("r_shoulder_joint_1", "shoulder", True)
		connectSkinJoint("l_arm_limb_b_1_joint", "arm")
		connectSkinJoint("r_arm_limb_b_1_joint", "arm", True)
		connectSkinJoint("l_arm_limbB_end_skinJoint", "hand")
		connectSkinJoint("r_arm_limbB_end_skinJoint", "hand", True)
		connectSkinJoint("l_leg_limb_b_1_joint", "leg")
		connectSkinJoint("r_leg_limb_b_1_joint", "leg", True)
		connectSkinJoint("l_heel_joint", "foot")
		connectSkinJoint("r_heel_joint", "foot", True)
		connectSkinJoint("l_toe_joint", "toe")
		connectSkinJoint("r_toe_joint", "toe", True)		
		
		# connect forearms and hips
		#if noTwisting:
		connectSkinJoint("l_arm_limb_a_4_joint", "forearm")
		connectSkinJoint("r_arm_limb_a_4_joint", "forearm", True)	
		connectSkinJoint("l_leg_limb_a_4_joint", "hip")
		connectSkinJoint("r_leg_limb_a_4_joint", "hip", True)		

		

		# connect optional rig joints ------------------------------------------
		for n in self.buttons:
			if cmds.objExists(n+"_ctrl_OFFSET"):
				cmds.delete(n+"_ctrl_OFFSET")		
			if cmds.objExists("l_"+n+"_ctrl_OFFSET"):
				cmds.delete("l_"+n+"_ctrl_OFFSET")		
			if cmds.objExists("r_"+n+"_ctrl_OFFSET"):
				cmds.delete("r_"+n+"_ctrl_OFFSET")		

		def makeControlAndConnect(rigJoint, inputJointName, scale=1, color=18, shape="circle"):
			inputJoint = self.buttons[inputJointName][0]

			if inputJoint == "":
				return			

			if rigJoint.split('_')[0] == "l":
				side = "l_"
			elif rigJoint.split('_')[0] == "r":
				side = "r_"
				if self.sidePos == "prefix":
					inputJoint = "input_" + self.r_name + inputJoint[7:]
				elif self.sidePos == "suffix":
					inputJoint = inputJoint[:-1] + self.r_name
				elif self.sidePos == "suffix_merged" or self.sidePos == "middle":
					inputJoint = inputJoint.replace(self.l_name, self.r_name)		
			else:
				side = ""

			skinJoint = inputJoint.replace("input", "skin")				

			if shape == "circle":
				ctrl = mel.eval("pk_makeCircle(\"%s_ctrl\", \"y\")" %(side+inputJointName))
			elif shape == "cube":
				ctrl = mel.eval("pk_makeCube(\"%s_ctrl\")" %(side+inputJointName))

			cmds.setAttr(ctrl+".overrideEnabled", 1)
			cmds.setAttr(ctrl+".overrideColor", color)
			cmds.setAttr(ctrl+".sx", scale)
			cmds.setAttr(ctrl+".sy", scale)
			cmds.setAttr(ctrl+".sz", scale)
			cmds.setAttr(ctrl+".sz", scale)
			ctrl_grp = cmds.group(ctrl, n=ctrl+"_OFFSET")			
			cmds.parent(ctrl_grp, rigJoint)
			utils.resetAttrs(ctrl_grp)
			cmds.parentConstraint(inputJoint, ctrl, mo=0)
			cmds.parentConstraint(ctrl, skinJoint, mo=0)

			cmds.sets(ctrl, forceElement='controlSet', edit=1)

			cmds.setAttr(ctrl+".sx", lock=1, keyable=0, channelBox=0)
			cmds.setAttr(ctrl+".sy", lock=1, keyable=0, channelBox=0)
			cmds.setAttr(ctrl+".sz", lock=1, keyable=0, channelBox=0)
			cmds.setAttr(ctrl+".v", lock=1, keyable=0, channelBox=0)

			if inputJointName.split("_")[0] == "finger":
				digit = inputJointName.split("_")[-1]
				digitPrev = str(int(digit)-1)
				objPrev = side + inputJointName[:-1*len(digit)] + str(int(digit)-1) + '_ctrl'
				if cmds.objExists(objPrev):
					cmds.parent(ctrl_grp, objPrev)
					cmds.showHidden(ctrl_grp)
			
			# mirror simmetry control
			if side == "r_":
				par = cmds.listRelatives(ctrl, parent=1)[0]
				sc = cmds.getAttr(par+".sx")
				cmds.setAttr(par+".sx", -1.0*sc)

		makeControlAndConnect("l_arm_limb_b_2_joint", "arm_1", 6)
		makeControlAndConnect("l_arm_limb_b_3_joint", "arm_2", 6)
		makeControlAndConnect("l_arm_limb_b_4_joint", "arm_3", 6)
		makeControlAndConnect("r_arm_limb_b_2_joint", "arm_1", 6)
		makeControlAndConnect("r_arm_limb_b_3_joint", "arm_2", 6)
		makeControlAndConnect("r_arm_limb_b_4_joint", "arm_3", 6)
		
		makeControlAndConnect("l_arm_limb_a_2_joint", "forearm_1", 6)
		makeControlAndConnect("l_arm_limb_a_3_joint", "forearm_2", 6)
		makeControlAndConnect("l_arm_limb_a_4_joint", "forearm_3", 6)
		makeControlAndConnect("r_arm_limb_a_2_joint", "forearm_1", 6)
		makeControlAndConnect("r_arm_limb_a_3_joint", "forearm_2", 6)
		makeControlAndConnect("r_arm_limb_a_4_joint", "forearm_3", 6)
		
		makeControlAndConnect("l_leg_limb_a_2_joint", "hip_1", 6)
		makeControlAndConnect("l_leg_limb_a_3_joint", "hip_2", 6)
		makeControlAndConnect("l_leg_limb_a_4_joint", "hip_3", 6)
		makeControlAndConnect("r_leg_limb_a_2_joint", "hip_1", 6)
		makeControlAndConnect("r_leg_limb_a_3_joint", "hip_2", 6)
		makeControlAndConnect("r_leg_limb_a_4_joint", "hip_3", 6)		

		makeControlAndConnect("l_leg_limb_b_2_joint", "leg_1", 6)
		makeControlAndConnect("l_leg_limb_b_3_joint", "leg_2", 6)
		makeControlAndConnect("l_leg_limb_b_4_joint", "leg_3", 6)
		makeControlAndConnect("r_leg_limb_b_2_joint", "leg_1", 6)
		makeControlAndConnect("r_leg_limb_b_3_joint", "leg_2", 6)
		makeControlAndConnect("r_leg_limb_b_4_joint", "leg_3", 6)
		
		makeControlAndConnect("spine_2_joint", "spine_1", 20)
		makeControlAndConnect("spine_3_joint", "spine_2", 20)
		makeControlAndConnect("spine_4_joint", "spine_3", 20)
		makeControlAndConnect("spine_5_joint", "spine_4", 20)
		makeControlAndConnect("spine_6_joint", "spine_5", 20)
		
		makeControlAndConnect("l_arm_limbB_end_skinJoint", "finger_1_1", 2)
		makeControlAndConnect("r_arm_limbB_end_skinJoint", "finger_1_1", 2)
		makeControlAndConnect("l_arm_limbB_end_skinJoint", "finger_1_2", 2)
		makeControlAndConnect("r_arm_limbB_end_skinJoint", "finger_1_2", 2)
		makeControlAndConnect("l_arm_limbB_end_skinJoint", "finger_1_3", 2)
		makeControlAndConnect("r_arm_limbB_end_skinJoint", "finger_1_3", 2)
		makeControlAndConnect("l_arm_limbB_end_skinJoint", "finger_2_1", 2)
		makeControlAndConnect("r_arm_limbB_end_skinJoint", "finger_2_1", 2)
		makeControlAndConnect("l_arm_limbB_end_skinJoint", "finger_2_2", 2)
		makeControlAndConnect("r_arm_limbB_end_skinJoint", "finger_2_2", 2)
		makeControlAndConnect("l_arm_limbB_end_skinJoint", "finger_2_3", 2)
		makeControlAndConnect("r_arm_limbB_end_skinJoint", "finger_2_3", 2)
		makeControlAndConnect("l_arm_limbB_end_skinJoint", "finger_3_1", 2)
		makeControlAndConnect("r_arm_limbB_end_skinJoint", "finger_3_1", 2)
		makeControlAndConnect("l_arm_limbB_end_skinJoint", "finger_3_2", 2)
		makeControlAndConnect("r_arm_limbB_end_skinJoint", "finger_3_2", 2)
		makeControlAndConnect("l_arm_limbB_end_skinJoint", "finger_3_3", 2)
		makeControlAndConnect("r_arm_limbB_end_skinJoint", "finger_3_3", 2)
		makeControlAndConnect("l_arm_limbB_end_skinJoint", "finger_4_1", 2)
		makeControlAndConnect("r_arm_limbB_end_skinJoint", "finger_4_1", 2)
		makeControlAndConnect("l_arm_limbB_end_skinJoint", "finger_4_2", 2)
		makeControlAndConnect("r_arm_limbB_end_skinJoint", "finger_4_2", 2)
		makeControlAndConnect("l_arm_limbB_end_skinJoint", "finger_4_3", 2)
		makeControlAndConnect("r_arm_limbB_end_skinJoint", "finger_4_3", 2)
		makeControlAndConnect("l_arm_limbB_end_skinJoint", "finger_5_1", 2)
		makeControlAndConnect("r_arm_limbB_end_skinJoint", "finger_5_1", 2)
		makeControlAndConnect("l_arm_limbB_end_skinJoint", "finger_5_2", 2)
		makeControlAndConnect("r_arm_limbB_end_skinJoint", "finger_5_2", 2)
		makeControlAndConnect("l_arm_limbB_end_skinJoint", "finger_5_3", 2)
		makeControlAndConnect("r_arm_limbB_end_skinJoint", "finger_5_3", 2)
		
		makeControlAndConnect("l_shoulder_joint_1", "acc_1", 10, 15, "cube")
		makeControlAndConnect("r_shoulder_joint_1", "acc_1", 10, 15, "cube")
		
		makeControlAndConnect("posCtrl", "addObject_1", 15, 15, "cube")
		makeControlAndConnect("posCtrl", "addObject_2", 15, 15, "cube")
		makeControlAndConnect("posCtrl", "addObject_3", 15, 15, "cube")
		makeControlAndConnect("posCtrl", "addObject_4", 15, 15, "cube")
		makeControlAndConnect("posCtrl", "addObject_5", 15, 15, "cube")
		makeControlAndConnect("posCtrl", "addObject_6", 15, 15, "cube")
		makeControlAndConnect("posCtrl", "addObject_7", 15, 15, "cube")
		makeControlAndConnect("posCtrl", "addObject_8", 15, 15, "cube")
		makeControlAndConnect("posCtrl", "addObject_9", 15, 15, "cube")
		
		# add symmetry weapons controls
		makeControlAndConnect("l_arm_limbB_end_skinJoint", "weapon_1", 10, 15, "cube")
		if self.symWeapon_cb.isChecked():
			makeControlAndConnect("r_arm_limbB_end_skinJoint", "weapon_1", 10, 15, "cube")
		else:
			makeControlAndConnect("r_arm_limbB_end_skinJoint", "symWeapon_1", 10, 15, "cube")

		# add parent attribute
		def addParentAttr(control, parents, niceNames):
			if not cmds.objExists(control):
				return
			
			obj = cmds.listRelatives(control, parent=1)[0]
			targets = []
			for i, n in enumerate(parents):
				t = cmds.spaceLocator(n='target_'+n+'__'+control)[0]
				t_gr = cmds.group(n='target_'+n+'__'+control+"_grp", empty=1)
				cmds.parent(t, t_gr)
				targets.append(t)
				cmds.parent(t_gr, parents[i])
				cmds.hide(t_gr)
	
			# create constraint
			const = cmds.parentConstraint(targets, obj, mo=0)[0]
	
			# add attr
			cmds.addAttr(control, longName="parent", attributeType='enum', keyable=1, enumName=':'.join(niceNames) )
			# set draven keys
			for k in range (len(parents)):
				# first set attr on control
				cmds.setAttr("%s.%s" %(control, "parent"), k)
				# then foreach constraint attr
				for i in range (len(parents)):
					# set 1 or 0
					if i == k:
						cmds.setAttr("%s.%sW%i" %(const, targets[i], i), 1)
					else:
						cmds.setAttr("%s.%sW%i" %(const, targets[i], i), 0)
					# and set key
					cmds.setDrivenKeyframe("%s.%sW%i" %(const, targets[i], i), currentDriver="%s.%s" %(control, "parent"))			
					
			cmds.setAttr("%s.%s" %(control, "parent"), 0)
	
		addParentAttr('l_weapon_1_ctrl', ['l_arm_limbB_end_skinJoint', 'r_arm_limbB_end_skinJoint', 'head_joint', 'chest_joint', 'pelvis_joint', 'twoHanded'], 
			          ['hand', 'r_hand', 'head', 'chest', 'pelvis', 'two handed'] )
		addParentAttr('r_weapon_1_ctrl', ['r_arm_limbB_end_skinJoint', 'l_arm_limbB_end_skinJoint', 'head_joint', 'chest_joint', 'pelvis_joint', 'twoHanded'], 
			          ['hand', 'l_hand', 'head', 'chest', 'pelvis', 'two handed'] )

		cmds.parent('skin_root', 'input_root', 'character')
		
		
		# connect shapes
		def connectShape(src, tgt):
			try:
				cmds.connectAttr(src+'.worldSpace[0]', tgt+'.create')
			except: pass
		
		connectShape('l_arm_1_ctrlShape', 'r_arm_1_ctrlShape')
		connectShape('l_arm_2_ctrlShape', 'r_arm_2_ctrlShape')
		connectShape('l_arm_3_ctrlShape', 'r_arm_3_ctrlShape')
		connectShape('l_forearm_1_ctrlShape', 'r_forearm_1_ctrlShape')
		connectShape('l_forearm_2_ctrlShape', 'r_forearm_2_ctrlShape')
		connectShape('l_forearm_3_ctrlShape', 'r_forearm_3_ctrlShape')
		connectShape('l_acc_1_ctrlShape', 'r_acc_1_ctrlShape')
		connectShape('l_weapon_1_ctrlShape', 'r_weapon_1_ctrlShape')
		connectShape('l_hip_1_ctrlShape', 'r_hip_1_ctrlShape')
		connectShape('l_hip_2_ctrlShape', 'r_hip_2_ctrlShape')
		connectShape('l_hip_3_ctrlShape', 'r_hip_3_ctrlShape')
		connectShape('l_leg_1_ctrlShape', 'r_leg_1_ctrlShape')
		connectShape('l_leg_2_ctrlShape', 'r_leg_2_ctrlShape')
		connectShape('l_leg_3_ctrlShape', 'r_leg_3_ctrlShape')
		
		connectShape('l_finger_1_1_ctrlShape', 'r_finger_1_1_ctrlShape')
		connectShape('l_finger_1_2_ctrlShape', 'r_finger_1_2_ctrlShape')
		connectShape('l_finger_1_3_ctrlShape', 'r_finger_1_3_ctrlShape')
		connectShape('l_finger_2_1_ctrlShape', 'r_finger_2_1_ctrlShape')
		connectShape('l_finger_2_2_ctrlShape', 'r_finger_2_2_ctrlShape')
		connectShape('l_finger_2_3_ctrlShape', 'r_finger_2_3_ctrlShape')
		connectShape('l_finger_3_1_ctrlShape', 'r_finger_3_1_ctrlShape')
		connectShape('l_finger_3_2_ctrlShape', 'r_finger_3_2_ctrlShape')
		connectShape('l_finger_3_3_ctrlShape', 'r_finger_3_3_ctrlShape')
		connectShape('l_finger_4_1_ctrlShape', 'r_finger_4_1_ctrlShape')
		connectShape('l_finger_4_2_ctrlShape', 'r_finger_4_2_ctrlShape')
		connectShape('l_finger_4_3_ctrlShape', 'r_finger_4_3_ctrlShape')
		connectShape('l_finger_5_1_ctrlShape', 'r_finger_5_1_ctrlShape')
		connectShape('l_finger_5_2_ctrlShape', 'r_finger_5_2_ctrlShape')
		connectShape('l_finger_5_3_ctrlShape', 'r_finger_5_3_ctrlShape')
		
		if cmds.objExists("twoHanded"):
			connect("hand", "twoHanded", "par", True, False)
		
	def saveMap(self):
		
		# get current scene path
		fullName = cmds.file(q=1,  expandName=1)
		fileName = cmds.file(q=1, expandName=1).split('/')[-1]
		filePath = fullName.split(fileName)[0]		

		filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", filePath, "*.map")[0]
		print filename
		
		if filename == "":
			return

		# convert buttons data
		buttonsData = {}
		for b in self.buttons:
			buttonsData[b] = self.buttons[b][0]
			
		
		data = [buttonsData, self.l_name, self.r_name, self.sidePos]

		with open(filename, 'w') as outfile:
			json.dump(data, outfile, indent = 4)		

	def loadMap(self):
		
		# get current scene path
		fullName = cmds.file(q=1,  expandName=1)
		fileName = cmds.file(q=1, expandName=1).split('/')[-1]
		filePath = fullName.split(fileName)[0]		

		filename = QtWidgets.QFileDialog.getOpenFileName(self, "Save file", filePath, "*.map")[0]
		if filename == "":
			return
		
		with open(filename) as data_file:
			data = json.load(data_file)		
			
		buttonsData = data[0]
		self.l_name = data[1]
		self.r_name = data[2]
		self.sidePos = data[3]
		
		for b in self.buttons:
			try:
				self.buttons[b][0] = buttonsData[b]
			except:
				self.buttons[b][0] = ""
		
		self.updateUI()
		self.save()
		
		utils.pyToAttr('character.l_side', self.l_name)
		utils.pyToAttr('character.r_side', self.r_name)
		utils.pyToAttr('character.sidePos', self.sidePos)
		utils.pyToAttr('character.rootJoint', self.buttons['pelvis'][0])		

class ConnectWindow(QtWidgets.QMainWindow, bakeWindow.Ui_MainWindow):
	def __init__(self, parent=mayaMainWindow()):
		super(ConnectWindow, self).__init__(parent)
		self.setupUi(self)
		logger.debug("Start " + inspect.stack()[0][3])

		self.connectSignals()		
		self.l_name = 'l'
		self.r_name = 'r'
		self.data = {}
		self.rigs = {}
		self.root = ""
		
		self.bakeControls_btn.setVisible(False)
		self.clearKeys_btn.setVisible(False)
		self.exclude_groupBox.setVisible(False)
		self.exclude_frame.setVisible(False)
		self.exclude_groupBox.setChecked(False)
		
		
		if not cmds.objExists('character'):
			self.main_frame.setEnabled(0)
			self.connectRig_btn.setEnabled(0)
			self.bakeControls_btn.setEnabled(0)
			self.import_frame.setEnabled(1)
		else:
			#try:
			self.connectRig_btn.setEnabled(not cmds.getAttr('character.connected'))
			self.bakeControls_btn.setEnabled(cmds.getAttr('character.connected') and not cmds.getAttr('character.backed'))
			self.main_frame.setEnabled(cmds.getAttr('character.backed'))
			self.import_frame.setEnabled(0)
			#except: pass
		
		self.addMenu()	
		self.load()
		self.updateRigsList()
		#self.resize(self.minimumSizeHint())
		
		if cmds.objExists('input_root'):
			self.root = cmds.listRelatives('input_root')[0].split('input_')[-1]
		

	def addMenu(self):
		
		def setText(text):
			self.skeletonRoot_lineEdit.setText(text)
		
		menu = QtWidgets.QMenu(self)
		
		for m in ['Armature', 'skeleton']:
			m_action = QtWidgets.QAction(self)
			m_action.setText(m)
			m_action.triggered.connect(partial(setText, m))
			menu.addAction(m_action)	
			
		self.setSceletonRoot_btn.setMenu(menu)

	def connectSignals(self):
		logger.debug("Start " + inspect.stack()[0][3])

		self.connectRig_btn.clicked.connect(self.connectRig)
		self.bakeControls_btn.clicked.connect(self.bakeControls)
		self.bakeSceleton_btn.clicked.connect(self.bakeSceleton)

		self.add_btn.clicked.connect(self.addToExclude)
		self.remove_btn.clicked.connect(self.removeFromExclude)
		self.clear_btn.clicked.connect(self.clearList)		

		self.clearKeys_btn.clicked.connect(self.clear)
		self.export_btn.clicked.connect(self.hotExport)
		self.import_btn.clicked.connect(self.hotImport)
		self.addRig_btn.clicked.connect(self.addRig)
		self.removeRig_btn.clicked.connect(self.removeRig)

		self.bakeIkFk_btn.clicked.connect(self.bakeIkFk)
		self.switchIkFk_btn.clicked.connect(self.switchIkFk)
		self.switchParent_btn.clicked.connect(self.switchParent)
		self.switchParentRange_btn.clicked.connect(self.switchParentRange)
		
		self.importRig_btn.clicked.connect(self.imporRig)
		self.importDefaultFbx_btn.clicked.connect(self.importDefaultFbx)
		self.exclude_groupBox.clicked.connect(self.switchExcludeList)
		self.alignTwoHanded_btn.clicked.connect(self.alignTwoHanded)
		self.alignTwoHandedRange_btn.clicked.connect(self.alignTwoHandedBake)

	def load(self):
		
		self.data = json.load( open(data_file, 'r') )
		self.rigs = self.data['rigs']

	def addRig(self):
		# get current scene path
		fullName = cmds.file(q=1,  expandName=1)
		fileName = cmds.file(q=1, expandName=1).split('/')[-1]
		filePath = fullName.split(fileName)[0]		
		
		# open select window 
		rigPath = QtGui.QFileDialog.getOpenFileName(self, "import rig", filePath, "*.ma")[0]
		if rigPath == "":
			return		
		
		# update data
		rigName = rigPath.split('/')[-1][:-3]
		self.rigs[rigName] = rigPath
		self.data['rigs'] = self.rigs	
		
		self.save()
		self.updateRigsList(rigName)

	def save(self):
		# save data
		with open(data_file, 'w') as file:
			json.dump(self.data, file, indent = 4)			
	
	def removeRig(self):
		curRig = self.rigs_comboBox.currentText()
		
		del self.rigs[curRig]
		
		self.save()
		self.updateRigsList()
		
	def updateRigsList(self, curRig=""):
		logger.debug("Start " + inspect.stack()[0][3])
		
		self.rigs_comboBox.clear()
		
		# fill list
		for r in sorted(self.rigs):
			self.rigs_comboBox.addItem(r)
	                                                                                                                                                                                                                                                                                                                                                                                                                    
		# set current item
		if curRig != "":
			for x, name in enumerate(sorted(self.rigs)):
				if name == curRig:
					self.rigs_comboBox.setCurrentIndex(x)		

	def imporRig(self):
		## get current scene path
		#fullName = cmds.file(q=1,  expandName=1)
		#fileName = cmds.file(q=1, expandName=1).split('/')[-1]
		#filePath = fullName.split(fileName)[0]		

		## open select window 
		#filePath = QtGui.QFileDialog.getOpenFileName(self, "import rig", filePath, "*.ma")[0]
		
		filePath = self.rigs[self.rigs_comboBox.currentText()]
		
		if filePath == "":
			return		
		
		# geometry grouping
		if not cmds.objExists('Geometry'):
			geo_gr = pm.group(empty=1, n='Geometry')
			all = pm.ls(dag=1)
			for o in all:
				if o.getParent() == None:
					children = o.getChildren()
					if len(children) > 0:
						if o.getChildren()[0].type() == 'mesh':
							pm.parent(o, geo_gr)		

		# import rig
		cmds.file(filePath, pr=1, i=1, type="mayaAscii", mergeNamespacesOnClash=False, options="v=0;")
		
		cmds.hide('input_root')
		cmds.hide('skin_root')
		
		self.root = cmds.listRelatives('input_root')[0].split('input_')[-1]
		
		utils.setUserAttr('character', 'connected', 0, 'bool')
		utils.setUserAttr('character', 'backed', 0, 'bool')
		
		self.connectRig_btn.setEnabled(1)
		self.import_frame.setEnabled(0)

	def connectRig(self):
		childs = cmds.listRelatives("input_root", children=1, type="joint", allDescendents=1)
		
		def connect(src, tgt):
			try:
				cmds.connectAttr(src+".t", tgt+".t")
				cmds.connectAttr(src+".r", tgt+".r")
				orX = cmds.getAttr(src+".jointOrientX")
				orY = cmds.getAttr(src+".jointOrientY")
				orZ = cmds.getAttr(src+".jointOrientZ")
				cmds.setAttr(tgt+".jointOrientX", orX)
				cmds.setAttr(tgt+".jointOrientY", orY)
				cmds.setAttr(tgt+".jointOrientZ", orZ)
			except: 
				print "missed ", src, " to ", tgt

		for c in childs:
			connect(c[6:], c)
			
		self.connectRig_btn.setEnabled(0)
		self.bakeControls_btn.setEnabled(1)
		
		utils.setUserAttr('character', 'connected', 1, 'bool')
		
		# disconnect twist controls from input skeleton
		try:
			cmds.delete('l_arm_2_ctrl_parentConstraint1')
			cmds.delete('r_arm_2_ctrl_parentConstraint1')
		except: pass
		
		self.bakeControls()

	def bakeControls(self):
		# bake controls
		cmds.select('controlSet')
		mel.eval("string $minTime = `playbackOptions -q -minTime`;")
		mel.eval("string $maxTime = `playbackOptions -q -maxTime`;")
		mel.eval('string $range = $minTime + ":" + $maxTime;')
		mel.eval('bakeResults -simulation true -t $range  -sampleBy 1 -disableImplicitControl true -preserveOutsideKeys false -sparseAnimCurveBake false -removeBakedAttributeFromLayer false -bakeOnOverrideLayer false -minimizeRotation true -at "tx" -at "ty" -at "tz" -at "rx" -at "ry" -at "rz";')			

		orig_joints = []
						
		joints = pm.listRelatives(self.root, children=1, type="joint", allDescendents=1)
		for j in joints:
			orig_joints.append(j)				

		for j in orig_joints:
			try:
				name = j.name().split('|')[-1]
				self.disconnect(j, pm.PyNode('input_'+name))
				#pm.delete(j, channels=1, unitlessAnimationCurves=False, hierarchy="none")
				#self.connect(pm.PyNode('skin_'+name), j)
			except: print "miss in connect joints after bakeControls ", j	
		
		cmds.hide(self.root, 'Geometry')
		cmds.select(clear=1)
		
		self.bakeControls_btn.setEnabled(0)
		self.main_frame.setEnabled(1)
		
		utils.setUserAttr('character', 'backed', 1, 'bool')		

	def bakeSceleton(self):
		orig_joints = []
		skeletonRoot = self.skeletonRoot_lineEdit.text()
		#joints = pm.listRelatives("Armature", children=1, type="joint", allDescendents=1)
		joints = pm.listRelatives(skeletonRoot, children=1, type="joint", allDescendents=1)
		
		if cmds.objectType(skeletonRoot) == 'joint':
			pm.delete(pm.PyNode(skeletonRoot), channels=1, unitlessAnimationCurves=False, hierarchy="none")
			self.connect(pm.PyNode('skin_'+skeletonRoot), pm.PyNode(skeletonRoot))
			
		for j in joints:
			orig_joints.append(j)	
				
		for j in orig_joints:
			try:
				name = j.name().split('|')[-1]
				pm.delete(j, channels=1, unitlessAnimationCurves=False, hierarchy="none")
				self.connect(pm.PyNode('skin_'+name), j)
			except: print "miss in connectOrigSkeletonToRig ", j
			
		# bake orig sceleton
		#return
		#cmds.select('Armature')
		cmds.select(skeletonRoot)
		mel.eval("string $minTime = `playbackOptions -q -minTime`;")
		mel.eval("string $maxTime = `playbackOptions -q -maxTime`;")
		mel.eval('string $range = $minTime + ":" + $maxTime;')
		mel.eval('bakeResults -simulation true -t $range -hierarchy below -sampleBy 1 -disableImplicitControl true -preserveOutsideKeys false -sparseAnimCurveBake false -removeBakedAttributeFromLayer false -bakeOnOverrideLayer false -minimizeRotation true -at "tx" -at "ty" -at "tz" -at "rx" -at "ry" -at "rz";')					
		
		cmds.select(clear=1)

	def addToExclude(self):
		logger.debug("Add")

		sel = cmds.ls(sl=1)
		if len(sel) != 0:

			names = []
			for index in xrange(self.listWidget.count()):
				names.append(self.listWidget.item(index).text())			

			for o in sel:
				if o not in names:
					self.listWidget.addItem(o)

	def removeFromExclude(self):
		logger.debug("Remove")

		sel = cmds.ls(sl=1)

		for item in self.listWidget.selectedItems():
			self.listWidget.takeItem(self.listWidget.row(item))		

	def clearList(self):
		logger.debug("Clear")

		while self.listWidget.count() > 0:
			self.listWidget.takeItem(0)

		names = []
		for index in xrange(self.listWidget.count()):
			names.append(self.listWidget.item(index).text())		

	def clear(self):
		names = []
		for index in xrange(self.listWidget.count()):
			names.append(self.listWidget.item(index).text())

		joints = cmds.ls(type='joint')
		for j in joints:
			try:
				cmds.cutKey(j, cl=1, at=["sx", "sy", "sz"], o='keys')
				cmds.rotationInterpolation(j+'_rotateX', c='quaternionSlerp')
				cmds.rotationInterpolation(j+'_rotateX', c='none')
				if j not in names:
					cmds.cutKey(j, cl=1, at=["tx", "ty", "tz"])
			except: pass		

	def bakeIkFk(self):
		logger.debug("bakeIkFk")

		o = cmds.ls(sl=1)[0]

		frames = cmds.keyframe(o+'.tx', q=1, timeChange=1)
		if type(frames) == types.NoneType:
			frames = cmds.keyframe(o+'.ry', q=1, timeChange=1)
		#if type(frames) == types.NoneType:
			#frames = cmds.keyframe(o+'.fkIk', q=1, timeChange=1)

		initFrame = cmds.currentTime(q=1)

		if o.split("_")[0] == 'l':
			side = 'l'
		elif o.split("_")[0] == 'r':
			side = 'r'

		if side == 'r' or side == 'l':
			if o in ['l_hand', 'l_elbow', 'r_hand', 'r_elbow']:
				cmds.cutKey(side+'_wrist')
				cmds.cutKey(side+'_forearm')
				cmds.cutKey(side+'_arm')
				cmds.setKeyframe(side+'_wrist')
				cmds.setKeyframe(side+'_forearm')
				cmds.setKeyframe(side+'_arm')

				for f in frames:
					cmds.currentTime(f)
					pk_selector_switchIKFK.switchIkFk()
					mel.eval('human_switchFkIk -sl')

			elif o in ['l_wrist', 'l_forearm', 'l_arm', 'r_wrist', 'r_forearm', 'r_arm']:
				cmds.cutKey(side+'_hand')
				cmds.cutKey(side+'_elbow')
				cmds.setKeyframe(side+'_hand')
				cmds.setKeyframe(side+'_elbow')

				for f in frames:
					cmds.currentTime(f)
					pk_selector_switchIKFK.switchIkFk()
					mel.eval('human_switchFkIk -sl')
					
			#elif o in ['l_knee', 'l_foot', 'l_heelIk', 'r_knee', 'r_foot', 'r_heelIk']:
				#cmds.cutKey(side+'_upLeg')
				#cmds.cutKey(side+'_leg')
				#cmds.cutKey(side+'_heelFk')
				#cmds.cutKey(side+'_toeFk')
				#cmds.setKeyframe(side+'_upLeg')
				#cmds.setKeyframe(side+'_leg')
				#cmds.setKeyframe(side+'_heelFk')
				#cmds.setKeyframe(side+'_toeFk')

				#for f in frames:
					#cmds.currentTime(f)
					#pk_selector_switchIKFK.switchIkFk()
					#mel.eval('human_switchFkIk -sl')

			#elif o in ['l_upLeg', 'l_leg', 'l_heelFk', 'l_toeFk', 'r_upLeg', 'r_leg', 'r_heelFk', 'r_toeFk']:
				#cmds.cutKey(side+'_knee')
				#cmds.cutKey(side+'_foot')
				#cmds.cutKey(side+'_toeIk')
				#cmds.setKeyframe(side+'_knee')
				#cmds.setKeyframe(side+'_foot')
				#cmds.setKeyframe(side+'_toeIk')

				#for f in frames:
					#cmds.currentTime(f)
					#pk_selector_switchIKFK.switchIkFk()
					#mel.eval('human_switchFkIk -sl')

		mel.eval('human_switchFkIk -sl')
	
	def switchIkFk(self):
		logger.debug("switchIkFk")

		o = cmds.ls(sl=1)[0]

		if o.split("_")[0] == 'l':
			side = 'l'
		elif o.split("_")[0] == 'r':
			side = 'r'

		if side == 'r' or side == 'l':
			if o in ['l_hand', 'l_elbow', 'r_hand', 'r_elbow', 'r_wrist', 'l_wrist']:
				pk_selector_switchIKFK.switchIkFk()	
		
	def switchParentRange(self):
		sel = cmds.ls(sl=True)
	
		if len(sel) == 0:
			cmds.warning("select control with parent attribute")
			return
	
		sel = sel[0]
	
		if not cmds.attributeQuery( 'parent', node=sel, exists=True ):
			cmds.warning("select control with parent attribute")
			return	

		frames = cmds.keyframe(sel+'.tx', q=1, timeChange=1)
		if type(frames) == types.NoneType:
			frames = cmds.keyframe(sel+'.ry', q=1, timeChange=1)

		initFrame = cmds.currentTime(q=1)
		initParent = cmds.getAttr(sel+'.parent')
		
		for f in frames:
			cmds.currentTime(f)
			cmds.setAttr(sel+'.parent', initParent)
			self.switchParent()
			
		#return
		#nextParent = initParent + 1
		#if nextParent > cmds.attributeQuery('parent',n=sel, max=1)[0]:
			#nextParent = 0
		#cmds.setAttr(sel+'.parent', nextParent)
		pass
		
	def switchParent(self):
		sel = cmds.ls(sl=True)
	
		if len(sel) == 0:
			cmds.warning("select control with parent attribute")
			return
		
		sel = sel[0]
	
		if not cmds.attributeQuery( 'parent', node=sel, exists=True ):
			cmds.warning("select control with parent attribute")
			return		
	
		if sel.split('_')[0] != 'r':
			print 'Switch by xfrom'
			# Get transform
			tr = cmds.xform( sel, q=True, t=True, ws=True)
			rt = cmds.xform( sel, q=True, ro=True, ws=True)
		
			# get size of parent attribute enum
			list = mel.eval('attributeQuery -node %s -listEnum "parent"' %sel)
			size = len(list[0].split(":"))
		
			# get current parent
			currParentId = cmds.getAttr(sel+".parent")
			# next parent
			nextParentId = int(currParentId) + 1
			if nextParentId >= size:
				nextParentId = 0

			
			# get old visibility two handed ctrl
			#oldTwoHandedVis = cmds.getAttr('twoHanded_xform.v')

			# set next parent
			cmds.setAttr(sel+".parent", nextParentId)
		
			# get new visibility two handed ctrl
			#newTwoHandedVis = cmds.getAttr('twoHanded_xform.v')
			
			# move two handed ctrl if needed
			#if not oldTwoHandedVis and newTwoHandedVis:
				#tr = cmds.xform( 'twoHanded_loc', q=True, t=True, ws=True)
				#rt = cmds.xform( 'twoHanded_loc', q=True, ro=True, ws=True)				
				#cmds.move( tr[0], tr[1], tr[2], 'twoHanded', rotatePivotRelative=True)
				#cmds.rotate(rt[0], rt[1], rt[2], 'twoHanded', ws=True)						
		
			# Set Transform
			cmds.move( tr[0], tr[1], tr[2], sel, rotatePivotRelative=True)
			cmds.rotate(rt[0], rt[1], rt[2], sel, ws=True)			
			
		else:
			print 'Switch by constraint'
			l = cmds.spaceLocator()[0]
			p = cmds.listRelatives(sel, parent=1)[0]
			l2 = cmds.spaceLocator()[0]
			
			cmds.parent(l2, p)
			cmds.parentConstraint(l, l2, mo=0)
			cmds.setAttr(l2+'.sx', 1)
			cmds.setAttr(l2+'.sy', 1)
			cmds.setAttr(l2+'.sz', 1)
			cmds.parent(sel, l2)
			
			# get size of parent attribute enum
			list = mel.eval('attributeQuery -node %s -listEnum "parent"' %sel)
			size = len(list[0].split(":"))
			
			# get current parent
			currParentId = cmds.getAttr(sel+".parent")
			# next parent
			nextParentId = int(currParentId) + 1
			if nextParentId >= size:
				nextParentId = 0
			
			# set next parent
			cmds.setAttr(sel+".parent", nextParentId)
			
			cmds.parent(sel, p)
			cmds.delete(l, l2)			
		
	def alignTwoHanded(self):
		logger.debug("alignTwoHanded")
		
		if not cmds.getAttr('twoHanded_xform.v'):
			return
		
		if not cmds.objExists('twoHanded_loc'):
			l = cmds.spaceLocator(n='twoHanded_loc')[0]
			l_l = cmds.spaceLocator(n='l_twoHanded_loc')[0]
			r_l = cmds.spaceLocator(n='r_twoHanded_loc')[0]
		
			cmds.parent(l, 'twoHanded_rig')
			cmds.parent(l_l, 'l_arm_limbB_end_skinJoint')
			cmds.parent(r_l, 'r_arm_limbB_end_skinJoint')
		
			cmds.setAttr(l_l+'.tx', 0.12)
			cmds.setAttr(l_l+'.ty', -0.06)
			cmds.setAttr(l_l+'.tz', 0.05)
			cmds.setAttr(l_l+'.rx', 15)
			cmds.setAttr(l_l+'.ry', 0)
			cmds.setAttr(l_l+'.rz', -20)
		
			cmds.setAttr(r_l+'.tx', -0.12)
			cmds.setAttr(r_l+'.ty', -0.06)
			cmds.setAttr(r_l+'.tz', 0.05)
			cmds.setAttr(r_l+'.rx', 15)
			cmds.setAttr(r_l+'.ry', 0)
			cmds.setAttr(r_l+'.rz', 20)
		
			cmds.pointConstraint(l_l, r_l, l, mo=0)
			cmds.aimConstraint(l_l, l, mo=0, aimVector=(0,0,1))
			cmds.hide(l_l, r_l, l)
			
			cmds.select(clear=1)
			
		def beforeAlign(o):
			if not cmds.objExists(o):
				return
			l = cmds.spaceLocator(n=o+'_1_th_loc')[0]
			p = cmds.listRelatives(o, parent=1)[0]
			l2 = cmds.spaceLocator(n=o+'_2_th_loc')[0]
			
			cmds.parent(l2, p)
			cmds.parentConstraint(l, l2, mo=0)
			cmds.setAttr(l2+'.sx', 1)
			cmds.setAttr(l2+'.sy', 1)
			cmds.setAttr(l2+'.sz', 1)
			cmds.parent(o, l2)
		
		def afterAlign(o, p):	
			if not cmds.objExists(o):
				return
			cmds.parent(o, p)
			cmds.delete(o+'_1_th_loc', o+'_2_th_loc')				
		
		beforeAlign('l_hand')
		beforeAlign('r_hand')
		beforeAlign('l_weapon_1_ctrl')
		beforeAlign('r_weapon_1_ctrl')
				
		# Get transform
		tr = cmds.xform( 'twoHanded_loc', q=True, t=True, ws=True)
		rt = cmds.xform( 'twoHanded_loc', q=True, ro=True, ws=True)			
	
		cmds.move( tr[0], tr[1], tr[2], 'twoHanded', rotatePivotRelative=True)
		cmds.rotate(rt[0], rt[1], rt[2], 'twoHanded', ws=True)			
		
		afterAlign('l_hand', 'l_hand_SN')
		afterAlign('r_hand', 'r_hand_SN')	
		afterAlign('l_weapon_1_ctrl', 'l_weapon_1_ctrl_OFFSET')
		afterAlign('r_weapon_1_ctrl', 'r_weapon_1_ctrl_OFFSET')	
		
		cmds.select('twoHanded')
		
	def alignTwoHandedBake(self):
		logger.debug("alignTwoHandedBake")
				
		#l_hand_loc = cmds.spaceLocator(n='l_hand_bakeLoc')[0]
		#r_hand_loc = cmds.spaceLocator(n='r_hand_bakeLoc')[0]
		#l_weapon_loc = cmds.spaceLocator(n='l_weapon_bakeLoc')[0]
		#r_weapon_loc = cmds.spaceLocator(n='r_weapon_bakeLoc')[0]
		#center_loc = cmds.spaceLocator(n='center_bakeLoc')[0]
		
		#cmds.parentConstraint('r_weapon_1_ctrl', r_weapon_loc, mo=0)
		#cmds.parentConstraint('l_weapon_1_ctrl', l_weapon_loc, mo=0)
		#cmds.parentConstraint('l_hand', l_hand_loc, mo=0)
		#cmds.parentConstraint('r_hand', r_hand_loc, mo=0)
		#cmds.pointConstraint(l_hand_loc, r_hand_loc, center_loc, mo=0)
		#cmds.aimConstraint(l_hand_loc, center_loc, mo=0, aimVector=(0,0,1))		
		
		#cmds.select(l_hand_loc, r_hand_loc, l_weapon_loc, r_weapon_loc, center_loc)
		#mel.eval("string $minTime = `playbackOptions -q -minTime`;")
		#mel.eval("string $maxTime = `playbackOptions -q -maxTime`;")
		#mel.eval('string $range = $minTime + ":" + $maxTime;')
		#mel.eval('bakeResults -simulation true -t $range -hierarchy below -sampleBy 1 -disableImplicitControl true -preserveOutsideKeys false -sparseAnimCurveBake false -removeBakedAttributeFromLayer false -bakeOnOverrideLayer false -minimizeRotation true -at "tx" -at "ty" -at "tz" -at "rx" -at "ry" -at "rz";')					
		
		#cmds.cutKey('l_weapon_1_ctrl')    
		#cmds.cutKey('r_weapon_1_ctrl')    
		#cmds.cutKey('l_hand')    
		#cmds.cutKey('r_hand')   		
		#cmds.cutKey('twoHanded')   		
		
		#c1 = cmds.parentConstraint(l_weapon_loc, 'l_weapon_1_ctrl', mo=0)
		#c2 = cmds.parentConstraint(r_weapon_loc, 'r_weapon_1_ctrl', mo=0)
		#c3 = cmds.parentConstraint(l_hand_loc, 'l_hand', mo=0)
		#c4 = cmds.parentConstraint(r_hand_loc, 'r_hand', mo=0)
		#c5 = cmds.parentConstraint(center_loc, 'twoHanded', mo=0)
		
		#cmds.select('l_weapon_1_ctrl', 'r_weapon_1_ctrl', 'l_hand', 'r_hand', 'twoHanded')
		#mel.eval("string $minTime = `playbackOptions -q -minTime`;")
		#mel.eval("string $maxTime = `playbackOptions -q -maxTime`;")
		#mel.eval('string $range = $minTime + ":" + $maxTime;')
		#mel.eval('bakeResults -simulation true -t $range -hierarchy below -sampleBy 1 -disableImplicitControl true -preserveOutsideKeys false -sparseAnimCurveBake false -removeBakedAttributeFromLayer false -bakeOnOverrideLayer false -minimizeRotation true -at "tx" -at "ty" -at "tz" -at "rx" -at "ry" -at "rz";')					

		#cmds.delete(c1,c2,c3,c4,c5)
		minTime = cmds.playbackOptions(q=1, minTime=1)
		maxTime = cmds.playbackOptions(q=1, maxTime=1)
		
		for i in range(minTime, maxTime+1):
			cmds.currentTime(i)		
			self.alignTwoHanded()

		
	def switchExcludeList(self):
		logger.debug("switchExcludeList")
		
		vis = self.exclude_groupBox.isChecked()
		self.exclude_frame.setVisible(vis)
		
		if vis:
			#self.resize(self.minimumSizeHint())
			self.resize(100,600)
		else:
			self.resize(100,100)
				
	def hotExport(self):
		logger.debug("hotExport")
	
		cmds.showHidden(self.root, 'Geometry')
		
		meshes = pm.listRelatives('Geometry')
		pm.parent(meshes, world=1)
		
		self.bakeSceleton()
		
		app_dir = cmds.internalVar(userAppDir=True)
		filePath = app_dir + 'projects/default/scenes/temporaryFbx.fbx'
		cmds.select(self.root, meshes)
		mel.eval('file -force -options "v=0;" -typ "FBX export" -pr -es "%s";' %filePath)		
	
		pm.parent(meshes, 'Geometry')
		cmds.hide(self.root, 'Geometry')

	def connect(self, src, tgt):   
		#print "connect", src, tgt
		pm.connectAttr(src.tx, tgt.tx)
		pm.connectAttr(src.ty, tgt.ty)
		pm.connectAttr(src.tz, tgt.tz)
		pm.connectAttr(src.rx, tgt.rx)
		pm.connectAttr(src.ry, tgt.ry)
		pm.connectAttr(src.rz, tgt.rz)
		orX = pm.getAttr(src.jointOrientX)
		orY = pm.getAttr(src.jointOrientY)
		orZ = pm.getAttr(src.jointOrientZ)
		pm.setAttr(tgt.jointOrientX, orX)
		pm.setAttr(tgt.jointOrientY, orY)
		pm.setAttr(tgt.jointOrientZ, orZ)

	def disconnect(self, src, tgt):
		#print "disconnect", src, tgt
		try:
			pm.disconnectAttr(src.t, tgt.t)
			pm.disconnectAttr(src.r, tgt.r)
		except: pass
		
		try:
			pm.disconnectAttr(src.tx, tgt.tx)
			pm.disconnectAttr(src.ty, tgt.ty)
			pm.disconnectAttr(src.tz, tgt.tz)
			pm.disconnectAttr(src.rx, tgt.rx)
			pm.disconnectAttr(src.ry, tgt.ry)
			pm.disconnectAttr(src.rz, tgt.rz)
		except: pass

	def hotImport(self):
		logger.debug("hotImport")
		
		cmds.currentTime(0)
		
		controls = utils.getSetObjects('controlSet')
		def getControl(tgt):
			for c in controls:
				#print c.name()
				if c.name().split('|')[-1] == tgt:
					return c
		
		data = utils.attrToPy('character.uiMatchButtons')
		self.sidePos = utils.attrToPy('character.sidePos')
			
		def connect(src, tgt, con="par", sym=False, offset=False):
			#print "connect ", src, tgt
			tgt = getControl(tgt)
			pm.delete(tgt, channels=1, unitlessAnimationCurves=False, hierarchy="none")
			srcJnt = data[src]

			if src == "" or srcJnt == "":
				return
			#print "matched ", src, tgt
			if sym:
				if self.sidePos == "prefix":
					srcJnt = "input_" + self.r_name + srcJnt[7:]
				elif self.sidePos == "suffix":
					srcJnt = srcJnt[:-1] + self.r_name
				elif self.sidePos == "suffix_merged" or self.sidePos == "middle":
					srcJnt = srcJnt.replace(self.l_name, self.r_name)
			
			loc = tgt.split('|')[-1]+"_connectRig_loc"
			print loc , tgt
			
			if con == "t":
				pm.pointConstraint(loc , tgt, mo=0)
			elif con == "r":
				pm.orientConstraint(loc , tgt, mo=0)
			else:
				pm.parentConstraint(loc , tgt, mo=0)
			
		# connect rig controls to input sceleton -----------------------------------------
		connect("pelvis", "pelvis", "par", False)
		connect("chest", "chest", "par", False)
		connect("neck", "neck", "par", False)
		connect("shoulder", "l_shoulder", "par", False)
		connect("shoulder", "r_shoulder", "par", True)
		connect("head", "head", "par", False)
		connect("hand", "l_hand", "par", False)
		connect("hand", "r_hand", "par", True)
		connect("foot", "l_foot", "par", False)
		connect("foot", "r_foot", "par", True)
		connect("toe", "l_toeIk", "r", False)
		connect("toe", "r_toeIk", "r", True)
		connect("toe", "l_toeFk", "r", False)
		connect("toe", "r_toeFk", "r", True)
		connect("foot", "l_heelFk", "r", False)
		connect("foot", "r_heelFk", "r", True)
		connect("leg", "l_leg", "r", False)
		connect("leg", "r_leg", "r", True)
		connect("hip", "l_upLeg", "r", False)
		connect("hip", "r_upLeg", "r", True)
		connect("forearm", "l_arm", "r", False)
		connect("forearm", "r_arm", "r", True)
		connect("arm", "l_forearm", "r", False)
		connect("arm", "r_forearm", "r", True)
		connect("hand", "l_wrist", "r", False)
		connect("hand", "r_wrist", "r", True)	
		
		def parent(src, tgt):
			pm.delete(tgt, channels=1, unitlessAnimationCurves=False, hierarchy="none")
			pm.parentConstraint(src, tgt, mo=0)
		
		parent("input_biceps_twist_l", "l_forearm_2_ctrl")
		parent("input_forearm_twist_l", "l_arm_2_ctrl")
		parent("input_biceps_twist_r", "r_forearm_2_ctrl")
		parent("input_forearm_twist_r", "r_arm_2_ctrl")
		parent("input_thigh_twist_l", "l_hip_2_ctrl")
		parent("input_thigh_twist_r", "r_hip_2_ctrl")
		parent("input_stomach", "spine_2_ctrl")
		parent("input_scapular_l", "l_acc_1_ctrl")
		parent("input_scapular_r", "r_acc_1_ctrl")
		parent("input_f_big1_l", "l_finger_1_1_ctrl")
		parent("input_f_big2_l", "l_finger_1_2_ctrl")
		parent("input_f_big3_l", "l_finger_1_3_ctrl")
		parent("input_f_pointer1_l", "l_finger_2_1_ctrl")
		parent("input_f_pointer2_l", "l_finger_2_2_ctrl")
		parent("input_f_pointer3_l", "l_finger_2_3_ctrl")
		parent("input_f_main1_l", "l_finger_3_1_ctrl")
		parent("input_f_main2_l", "l_finger_3_2_ctrl")
		parent("input_f_main3_l", "l_finger_3_3_ctrl")
		parent("input_f_big1_r", "r_finger_1_1_ctrl")
		parent("input_f_big2_r", "r_finger_1_2_ctrl")
		parent("input_f_big3_r", "r_finger_1_3_ctrl")
		parent("input_f_pointer1_r", "r_finger_2_1_ctrl")
		parent("input_f_pointer2_r", "r_finger_2_2_ctrl")
		parent("input_f_pointer3_r", "r_finger_2_3_ctrl")
		parent("input_f_main1_r", "r_finger_3_1_ctrl")
		parent("input_f_main2_r", "r_finger_3_2_ctrl")
		parent("input_f_main3_r", "r_finger_3_3_ctrl")
		parent("l_shoulder_connectRig_loc", "l_shoulder")
		parent("r_shoulder_connectRig_loc", "r_shoulder")
		parent("input_weapon_l", "l_weapon_1_ctrl")
		parent("input_weapon_r", "r_weapon_1_ctrl")
		
		
		def connectVectorSystem(loc, ctrl):
			ctrl = getControl(ctrl)
			pm.delete(ctrl, channels=1, unitlessAnimationCurves=False, hierarchy="none")
			# connect vector control to system		
			pm.pointConstraint(loc, ctrl, mo=0)[0]

		connectVectorSystem("locator81", "l_knee")
		connectVectorSystem("locator84", "r_knee")
		connectVectorSystem("locator90", "r_elbow")
		connectVectorSystem("locator87", "l_elbow")


		# import animation -----------------------------------------
		app_dir = cmds.internalVar(userAppDir=True)
		filePath = app_dir + 'projects/default/scenes/temporaryFbx.fbx'		
		cmds.file(filePath, pr=1, i=1, type="FBX", namespace="temporaryFbx", mergeNamespacesOnClash=False, options="v=0;", ra=True)
				
				
		# connect input sceleton -----------------------------------------
		orig_joints = []
		joints = pm.listRelatives(self.root, children=1, type="joint", allDescendents=1)
		for j in joints:
			orig_joints.append(j)				

		for j in orig_joints:
			try:
				name = j.name().split('|')[-1]
				self.connect(j, pm.PyNode('input_'+name))
			except: print "miss in connect joints after bakeControls ", j		
			
	
			
		# bake controls -----------------------------------------
		self.bakeControls()
		
	def importDefaultFbx(self):
		# import animation -----------------------------------------
		app_dir = cmds.internalVar(userAppDir=True)
		filePath = app_dir + 'projects/default/scenes/temporaryFbx.fbx'		
		cmds.file(filePath, pr=1, i=1, type="FBX", namespace="temporaryFbx", mergeNamespacesOnClash=False, options="v=0;", ra=True)
		