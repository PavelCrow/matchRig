# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Pavel\Dropbox\mayaScripts\matchRig\matchRig_mainWindow.ui'
#
# Created: Mon Feb 25 12:10:17 2019
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(425, 743)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(5, 5, 416, 611))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.back_btn = QtWidgets.QPushButton(self.groupBox)
        self.back_btn.setEnabled(False)
        self.back_btn.setGeometry(QtCore.QRect(5, 5, 406, 601))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy)
        self.back_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setIconSize(QtCore.QSize(556, 687))
        self.back_btn.setAutoDefault(True)
        self.back_btn.setFlat(False)
        self.back_btn.setObjectName("back_btn")
        self.shoulder_btn = QtWidgets.QPushButton(self.groupBox)
        self.shoulder_btn.setGeometry(QtCore.QRect(225, 90, 25, 19))
        self.shoulder_btn.setObjectName("shoulder_btn")
        self.foot_btn = QtWidgets.QPushButton(self.groupBox)
        self.foot_btn.setGeometry(QtCore.QRect(260, 525, 25, 19))
        self.foot_btn.setObjectName("foot_btn")
        self.hip_btn = QtWidgets.QPushButton(self.groupBox)
        self.hip_btn.setGeometry(QtCore.QRect(225, 318, 25, 19))
        self.hip_btn.setObjectName("hip_btn")
        self.arm_btn = QtWidgets.QPushButton(self.groupBox)
        self.arm_btn.setGeometry(QtCore.QRect(290, 216, 25, 19))
        self.arm_btn.setObjectName("arm_btn")
        self.hand_btn = QtWidgets.QPushButton(self.groupBox)
        self.hand_btn.setGeometry(QtCore.QRect(315, 280, 25, 19))
        self.hand_btn.setObjectName("hand_btn")
        self.head_btn = QtWidgets.QPushButton(self.groupBox)
        self.head_btn.setGeometry(QtCore.QRect(185, 60, 25, 19))
        self.head_btn.setObjectName("head_btn")
        self.leg_btn = QtWidgets.QPushButton(self.groupBox)
        self.leg_btn.setGeometry(QtCore.QRect(250, 450, 25, 19))
        self.leg_btn.setObjectName("leg_btn")
        self.chest_btn = QtWidgets.QPushButton(self.groupBox)
        self.chest_btn.setGeometry(QtCore.QRect(184, 126, 25, 19))
        self.chest_btn.setObjectName("chest_btn")
        self.forearm_btn = QtWidgets.QPushButton(self.groupBox)
        self.forearm_btn.setGeometry(QtCore.QRect(262, 130, 25, 19))
        self.forearm_btn.setObjectName("forearm_btn")
        self.pelvis_btn = QtWidgets.QPushButton(self.groupBox)
        self.pelvis_btn.setGeometry(QtCore.QRect(183, 240, 27, 19))
        self.pelvis_btn.setObjectName("pelvis_btn")
        self.spine_4_btn = QtWidgets.QPushButton(self.groupBox)
        self.spine_4_btn.setGeometry(QtCore.QRect(188, 166, 16, 16))
        self.spine_4_btn.setText("")
        self.spine_4_btn.setObjectName("spine_4_btn")
        self.neck_btn = QtWidgets.QPushButton(self.groupBox)
        self.neck_btn.setGeometry(QtCore.QRect(184, 96, 25, 19))
        self.neck_btn.setObjectName("neck_btn")
        self.spine_3_btn = QtWidgets.QPushButton(self.groupBox)
        self.spine_3_btn.setGeometry(QtCore.QRect(188, 184, 16, 16))
        self.spine_3_btn.setText("")
        self.spine_3_btn.setObjectName("spine_3_btn")
        self.spine_2_btn = QtWidgets.QPushButton(self.groupBox)
        self.spine_2_btn.setGeometry(QtCore.QRect(188, 202, 16, 16))
        self.spine_2_btn.setText("")
        self.spine_2_btn.setObjectName("spine_2_btn")
        self.spine_1_btn = QtWidgets.QPushButton(self.groupBox)
        self.spine_1_btn.setGeometry(QtCore.QRect(188, 220, 16, 16))
        self.spine_1_btn.setText("")
        self.spine_1_btn.setObjectName("spine_1_btn")
        self.spine_5_btn = QtWidgets.QPushButton(self.groupBox)
        self.spine_5_btn.setGeometry(QtCore.QRect(188, 148, 16, 16))
        self.spine_5_btn.setText("")
        self.spine_5_btn.setObjectName("spine_5_btn")
        self.toe_btn = QtWidgets.QPushButton(self.groupBox)
        self.toe_btn.setGeometry(QtCore.QRect(250, 548, 25, 19))
        self.toe_btn.setObjectName("toe_btn")
        self.forearm_1_btn = QtWidgets.QPushButton(self.groupBox)
        self.forearm_1_btn.setGeometry(QtCore.QRect(302, 116, 16, 16))
        self.forearm_1_btn.setText("")
        self.forearm_1_btn.setObjectName("forearm_1_btn")
        self.forearm_2_btn = QtWidgets.QPushButton(self.groupBox)
        self.forearm_2_btn.setGeometry(QtCore.QRect(302, 134, 16, 16))
        self.forearm_2_btn.setText("")
        self.forearm_2_btn.setObjectName("forearm_2_btn")
        self.forearm_3_btn = QtWidgets.QPushButton(self.groupBox)
        self.forearm_3_btn.setGeometry(QtCore.QRect(302, 152, 16, 16))
        self.forearm_3_btn.setText("")
        self.forearm_3_btn.setObjectName("forearm_3_btn")
        self.arm_3_btn = QtWidgets.QPushButton(self.groupBox)
        self.arm_3_btn.setGeometry(QtCore.QRect(324, 234, 16, 16))
        self.arm_3_btn.setText("")
        self.arm_3_btn.setObjectName("arm_3_btn")
        self.arm_1_btn = QtWidgets.QPushButton(self.groupBox)
        self.arm_1_btn.setGeometry(QtCore.QRect(324, 198, 16, 16))
        self.arm_1_btn.setText("")
        self.arm_1_btn.setObjectName("arm_1_btn")
        self.arm_2_btn = QtWidgets.QPushButton(self.groupBox)
        self.arm_2_btn.setGeometry(QtCore.QRect(324, 216, 16, 16))
        self.arm_2_btn.setText("")
        self.arm_2_btn.setObjectName("arm_2_btn")
        self.hip_3_btn = QtWidgets.QPushButton(self.groupBox)
        self.hip_3_btn.setGeometry(QtCore.QRect(260, 336, 16, 16))
        self.hip_3_btn.setText("")
        self.hip_3_btn.setObjectName("hip_3_btn")
        self.hip_2_btn = QtWidgets.QPushButton(self.groupBox)
        self.hip_2_btn.setGeometry(QtCore.QRect(260, 318, 16, 16))
        self.hip_2_btn.setText("")
        self.hip_2_btn.setObjectName("hip_2_btn")
        self.hip_1_btn = QtWidgets.QPushButton(self.groupBox)
        self.hip_1_btn.setGeometry(QtCore.QRect(260, 300, 16, 16))
        self.hip_1_btn.setText("")
        self.hip_1_btn.setObjectName("hip_1_btn")
        self.leg_3_btn = QtWidgets.QPushButton(self.groupBox)
        self.leg_3_btn.setGeometry(QtCore.QRect(286, 468, 16, 16))
        self.leg_3_btn.setText("")
        self.leg_3_btn.setObjectName("leg_3_btn")
        self.leg_1_btn = QtWidgets.QPushButton(self.groupBox)
        self.leg_1_btn.setGeometry(QtCore.QRect(286, 432, 16, 16))
        self.leg_1_btn.setText("")
        self.leg_1_btn.setObjectName("leg_1_btn")
        self.leg_2_btn = QtWidgets.QPushButton(self.groupBox)
        self.leg_2_btn.setGeometry(QtCore.QRect(286, 450, 16, 16))
        self.leg_2_btn.setText("")
        self.leg_2_btn.setObjectName("leg_2_btn")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(18, 564, 73, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(18, 580, 89, 16))
        self.label_2.setObjectName("label_2")
        self.reset_btn = QtWidgets.QPushButton(self.groupBox)
        self.reset_btn.setGeometry(QtCore.QRect(338, 580, 65, 19))
        self.reset_btn.setObjectName("reset_btn")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 12, 149, 115))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.finger_1_1_btn = QtWidgets.QPushButton(self.groupBox)
        self.finger_1_1_btn.setGeometry(QtCore.QRect(290, 292, 16, 16))
        self.finger_1_1_btn.setText("")
        self.finger_1_1_btn.setObjectName("finger_1_1_btn")
        self.finger_1_2_btn = QtWidgets.QPushButton(self.groupBox)
        self.finger_1_2_btn.setGeometry(QtCore.QRect(290, 310, 16, 16))
        self.finger_1_2_btn.setText("")
        self.finger_1_2_btn.setObjectName("finger_1_2_btn")
        self.finger_1_3_btn = QtWidgets.QPushButton(self.groupBox)
        self.finger_1_3_btn.setGeometry(QtCore.QRect(290, 328, 16, 16))
        self.finger_1_3_btn.setText("")
        self.finger_1_3_btn.setObjectName("finger_1_3_btn")
        self.finger_2_3_btn = QtWidgets.QPushButton(self.groupBox)
        self.finger_2_3_btn.setGeometry(QtCore.QRect(318, 342, 16, 16))
        self.finger_2_3_btn.setText("")
        self.finger_2_3_btn.setObjectName("finger_2_3_btn")
        self.finger_2_2_btn = QtWidgets.QPushButton(self.groupBox)
        self.finger_2_2_btn.setGeometry(QtCore.QRect(318, 324, 16, 16))
        self.finger_2_2_btn.setText("")
        self.finger_2_2_btn.setObjectName("finger_2_2_btn")
        self.finger_2_1_btn = QtWidgets.QPushButton(self.groupBox)
        self.finger_2_1_btn.setGeometry(QtCore.QRect(318, 306, 16, 16))
        self.finger_2_1_btn.setText("")
        self.finger_2_1_btn.setObjectName("finger_2_1_btn")
        self.finger_3_3_btn = QtWidgets.QPushButton(self.groupBox)
        self.finger_3_3_btn.setGeometry(QtCore.QRect(338, 342, 16, 16))
        self.finger_3_3_btn.setText("")
        self.finger_3_3_btn.setObjectName("finger_3_3_btn")
        self.finger_3_2_btn = QtWidgets.QPushButton(self.groupBox)
        self.finger_3_2_btn.setGeometry(QtCore.QRect(338, 324, 16, 16))
        self.finger_3_2_btn.setText("")
        self.finger_3_2_btn.setObjectName("finger_3_2_btn")
        self.finger_3_1_btn = QtWidgets.QPushButton(self.groupBox)
        self.finger_3_1_btn.setGeometry(QtCore.QRect(338, 306, 16, 16))
        self.finger_3_1_btn.setText("")
        self.finger_3_1_btn.setObjectName("finger_3_1_btn")
        self.finger_4_1_btn = QtWidgets.QPushButton(self.groupBox)
        self.finger_4_1_btn.setGeometry(QtCore.QRect(358, 306, 16, 16))
        self.finger_4_1_btn.setText("")
        self.finger_4_1_btn.setObjectName("finger_4_1_btn")
        self.finger_5_1_btn = QtWidgets.QPushButton(self.groupBox)
        self.finger_5_1_btn.setGeometry(QtCore.QRect(378, 306, 16, 16))
        self.finger_5_1_btn.setText("")
        self.finger_5_1_btn.setObjectName("finger_5_1_btn")
        self.finger_4_2_btn = QtWidgets.QPushButton(self.groupBox)
        self.finger_4_2_btn.setGeometry(QtCore.QRect(358, 324, 16, 16))
        self.finger_4_2_btn.setText("")
        self.finger_4_2_btn.setObjectName("finger_4_2_btn")
        self.finger_4_3_btn = QtWidgets.QPushButton(self.groupBox)
        self.finger_4_3_btn.setGeometry(QtCore.QRect(358, 342, 16, 16))
        self.finger_4_3_btn.setText("")
        self.finger_4_3_btn.setObjectName("finger_4_3_btn")
        self.finger_5_3_btn = QtWidgets.QPushButton(self.groupBox)
        self.finger_5_3_btn.setGeometry(QtCore.QRect(378, 342, 16, 16))
        self.finger_5_3_btn.setText("")
        self.finger_5_3_btn.setObjectName("finger_5_3_btn")
        self.finger_5_2_btn = QtWidgets.QPushButton(self.groupBox)
        self.finger_5_2_btn.setGeometry(QtCore.QRect(378, 324, 16, 16))
        self.finger_5_2_btn.setText("")
        self.finger_5_2_btn.setObjectName("finger_5_2_btn")
        self.acc_1_btn = QtWidgets.QPushButton(self.groupBox)
        self.acc_1_btn.setGeometry(QtCore.QRect(244, 66, 16, 16))
        self.acc_1_btn.setText("")
        self.acc_1_btn.setObjectName("acc_1_btn")
        self.weapon_1_btn = QtWidgets.QPushButton(self.groupBox)
        self.weapon_1_btn.setGeometry(QtCore.QRect(364, 268, 31, 19))
        self.weapon_1_btn.setObjectName("weapon_1_btn")
        self.symWeapon_1_btn = QtWidgets.QPushButton(self.groupBox)
        self.symWeapon_1_btn.setGeometry(QtCore.QRect(20, 262, 31, 19))
        self.symWeapon_1_btn.setObjectName("symWeapon_1_btn")
        self.symWeapon_cb = QtWidgets.QCheckBox(self.groupBox)
        self.symWeapon_cb.setGeometry(QtCore.QRect(318, 556, 85, 18))
        self.symWeapon_cb.setChecked(True)
        self.symWeapon_cb.setObjectName("symWeapon_cb")
        self.setRoot_btn = QtWidgets.QPushButton(self.groupBox)
        self.setRoot_btn.setGeometry(QtCore.QRect(335, 15, 66, 19))
        self.setRoot_btn.setDefault(False)
        self.setRoot_btn.setFlat(False)
        self.setRoot_btn.setObjectName("setRoot_btn")
        self.root_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.root_lineEdit.setGeometry(QtCore.QRect(338, 40, 61, 20))
        self.root_lineEdit.setText("")
        self.root_lineEdit.setReadOnly(True)
        self.root_lineEdit.setObjectName("root_lineEdit")
        self.frame_2 = QtWidgets.QFrame(self.groupBox)
        self.frame_2.setGeometry(QtCore.QRect(10, 450, 91, 91))
        self.frame_2.setObjectName("frame_2")
        self.addObject_6_btn = QtWidgets.QPushButton(self.frame_2)
        self.addObject_6_btn.setGeometry(QtCore.QRect(30, 60, 16, 16))
        self.addObject_6_btn.setText("")
        self.addObject_6_btn.setObjectName("addObject_6_btn")
        self.addObject_4_btn = QtWidgets.QPushButton(self.frame_2)
        self.addObject_4_btn.setGeometry(QtCore.QRect(30, 42, 16, 16))
        self.addObject_4_btn.setText("")
        self.addObject_4_btn.setObjectName("addObject_4_btn")
        self.addObject_2_btn = QtWidgets.QPushButton(self.frame_2)
        self.addObject_2_btn.setGeometry(QtCore.QRect(30, 24, 16, 16))
        self.addObject_2_btn.setText("")
        self.addObject_2_btn.setObjectName("addObject_2_btn")
        self.addObject_3_btn = QtWidgets.QPushButton(self.frame_2)
        self.addObject_3_btn.setGeometry(QtCore.QRect(10, 42, 16, 16))
        self.addObject_3_btn.setText("")
        self.addObject_3_btn.setObjectName("addObject_3_btn")
        self.addObject_5_btn = QtWidgets.QPushButton(self.frame_2)
        self.addObject_5_btn.setGeometry(QtCore.QRect(10, 60, 16, 16))
        self.addObject_5_btn.setText("")
        self.addObject_5_btn.setObjectName("addObject_5_btn")
        self.addObject_1_btn = QtWidgets.QPushButton(self.frame_2)
        self.addObject_1_btn.setGeometry(QtCore.QRect(10, 24, 16, 16))
        self.addObject_1_btn.setText("")
        self.addObject_1_btn.setObjectName("addObject_1_btn")
        self.addObject_9_btn = QtWidgets.QPushButton(self.frame_2)
        self.addObject_9_btn.setGeometry(QtCore.QRect(50, 60, 16, 16))
        self.addObject_9_btn.setText("")
        self.addObject_9_btn.setObjectName("addObject_9_btn")
        self.addObject_8_btn = QtWidgets.QPushButton(self.frame_2)
        self.addObject_8_btn.setGeometry(QtCore.QRect(50, 42, 16, 16))
        self.addObject_8_btn.setText("")
        self.addObject_8_btn.setObjectName("addObject_8_btn")
        self.addObject_7_btn = QtWidgets.QPushButton(self.frame_2)
        self.addObject_7_btn.setGeometry(QtCore.QRect(50, 24, 16, 16))
        self.addObject_7_btn.setText("")
        self.addObject_7_btn.setObjectName("addObject_7_btn")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 71, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_6.setMargin(0)
        self.label_6.setIndent(-1)
        self.label_6.setObjectName("label_6")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(6, 698, 415, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.importRig_btn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importRig_btn.sizePolicy().hasHeightForWidth())
        self.importRig_btn.setSizePolicy(sizePolicy)
        self.importRig_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.importRig_btn.setObjectName("importRig_btn")
        self.horizontalLayout.addWidget(self.importRig_btn)
        self.match_btn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.match_btn.sizePolicy().hasHeightForWidth())
        self.match_btn.setSizePolicy(sizePolicy)
        self.match_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.match_btn.setObjectName("match_btn")
        self.horizontalLayout.addWidget(self.match_btn)
        self.connect_btn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connect_btn.sizePolicy().hasHeightForWidth())
        self.connect_btn.setSizePolicy(sizePolicy)
        self.connect_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.connect_btn.setObjectName("connect_btn")
        self.horizontalLayout.addWidget(self.connect_btn)
        self.sides_gb = QtWidgets.QGroupBox(Dialog)
        self.sides_gb.setEnabled(True)
        self.sides_gb.setGeometry(QtCore.QRect(4, 618, 177, 77))
        self.sides_gb.setObjectName("sides_gb")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.sides_gb)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setContentsMargins(4, 2, 2, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.leftSide_lineEdit = QtWidgets.QLineEdit(self.sides_gb)
        self.leftSide_lineEdit.setObjectName("leftSide_lineEdit")
        self.gridLayout.addWidget(self.leftSide_lineEdit, 0, 1, 1, 1)
        self.rigthSide_lineEdit = QtWidgets.QLineEdit(self.sides_gb)
        self.rigthSide_lineEdit.setObjectName("rigthSide_lineEdit")
        self.gridLayout.addWidget(self.rigthSide_lineEdit, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.sides_gb)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.sides_gb)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.sidesSet_btn = QtWidgets.QToolButton(self.sides_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidesSet_btn.sizePolicy().hasHeightForWidth())
        self.sidesSet_btn.setSizePolicy(sizePolicy)
        self.sidesSet_btn.setMinimumSize(QtCore.QSize(50, 0))
        self.sidesSet_btn.setMaximumSize(QtCore.QSize(16777215, 48))
        self.sidesSet_btn.setAutoRaise(True)
        self.sidesSet_btn.setObjectName("sidesSet_btn")
        self.horizontalLayout_2.addWidget(self.sidesSet_btn)
        self.display_gb = QtWidgets.QGroupBox(Dialog)
        self.display_gb.setGeometry(QtCore.QRect(186, 618, 139, 77))
        self.display_gb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.display_gb.setFlat(False)
        self.display_gb.setObjectName("display_gb")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.display_gb)
        self.gridLayout_2.setContentsMargins(5, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.jointsVis_cb = QtWidgets.QCheckBox(self.display_gb)
        self.jointsVis_cb.setChecked(False)
        self.jointsVis_cb.setObjectName("jointsVis_cb")
        self.gridLayout_2.addWidget(self.jointsVis_cb, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 5, 0, 1, 1)
        self.jointsTempl_cb = QtWidgets.QCheckBox(self.display_gb)
        self.jointsTempl_cb.setObjectName("jointsTempl_cb")
        self.gridLayout_2.addWidget(self.jointsTempl_cb, 4, 1, 1, 1)
        self.posersVis_cb = QtWidgets.QCheckBox(self.display_gb)
        self.posersVis_cb.setChecked(False)
        self.posersVis_cb.setObjectName("posersVis_cb")
        self.gridLayout_2.addWidget(self.posersVis_cb, 2, 0, 1, 1)
        self.controlsVis_cb = QtWidgets.QCheckBox(self.display_gb)
        self.controlsVis_cb.setChecked(False)
        self.controlsVis_cb.setObjectName("controlsVis_cb")
        self.gridLayout_2.addWidget(self.controlsVis_cb, 3, 0, 1, 1)
        self.map_gb = QtWidgets.QGroupBox(Dialog)
        self.map_gb.setGeometry(QtCore.QRect(330, 618, 90, 77))
        self.map_gb.setObjectName("map_gb")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.map_gb)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(5, 2, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.save_btn = QtWidgets.QToolButton(self.map_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)
        self.save_btn.setAutoRaise(True)
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout.addWidget(self.save_btn)
        self.load_btn = QtWidgets.QToolButton(self.map_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_btn.sizePolicy().hasHeightForWidth())
        self.load_btn.setSizePolicy(sizePolicy)
        self.load_btn.setAutoRaise(True)
        self.load_btn.setObjectName("load_btn")
        self.verticalLayout.addWidget(self.load_btn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Rig Studio - Matcher", None, -1))
        self.shoulder_btn.setText(QtWidgets.QApplication.translate("Dialog", "Set", None, -1))
        self.foot_btn.setText(QtWidgets.QApplication.translate("Dialog", "Set", None, -1))
        self.hip_btn.setText(QtWidgets.QApplication.translate("Dialog", "Set", None, -1))
        self.arm_btn.setText(QtWidgets.QApplication.translate("Dialog", "Set", None, -1))
        self.hand_btn.setText(QtWidgets.QApplication.translate("Dialog", "Set", None, -1))
        self.head_btn.setText(QtWidgets.QApplication.translate("Dialog", "Set", None, -1))
        self.leg_btn.setText(QtWidgets.QApplication.translate("Dialog", "Set", None, -1))
        self.chest_btn.setText(QtWidgets.QApplication.translate("Dialog", "Set", None, -1))
        self.forearm_btn.setText(QtWidgets.QApplication.translate("Dialog", "Set", None, -1))
        self.pelvis_btn.setText(QtWidgets.QApplication.translate("Dialog", "Set", None, -1))
        self.neck_btn.setText(QtWidgets.QApplication.translate("Dialog", "Set", None, -1))
        self.toe_btn.setText(QtWidgets.QApplication.translate("Dialog", "Set", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "click - Set", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "ctrl+click - Select", None, -1))
        self.reset_btn.setText(QtWidgets.QApplication.translate("Dialog", "Reset", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog", "1. Open Skeleton T-pose file             2. Click Import Rig button                     3. Set joints                                   4. Click Match button                               5. Correct posers if needed                              6. Click Connect button                         7. Save file as match rig", None, -1))
        self.weapon_1_btn.setText(QtWidgets.QApplication.translate("Dialog", "Wpn", None, -1))
        self.symWeapon_1_btn.setText(QtWidgets.QApplication.translate("Dialog", "Wpn", None, -1))
        self.symWeapon_cb.setText(QtWidgets.QApplication.translate("Dialog", "Sym Weapon", None, -1))
        self.setRoot_btn.setText(QtWidgets.QApplication.translate("Dialog", "Set Root", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Dialog", "Add Objects", None, -1))
        self.importRig_btn.setText(QtWidgets.QApplication.translate("Dialog", "Import Rig", None, -1))
        self.match_btn.setText(QtWidgets.QApplication.translate("Dialog", "Match", None, -1))
        self.connect_btn.setText(QtWidgets.QApplication.translate("Dialog", "Connect", None, -1))
        self.sides_gb.setTitle(QtWidgets.QApplication.translate("Dialog", "Sides Naming", None, -1))
        self.leftSide_lineEdit.setText(QtWidgets.QApplication.translate("Dialog", "l", None, -1))
        self.rigthSide_lineEdit.setText(QtWidgets.QApplication.translate("Dialog", "r", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Dialog", "left Side", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("Dialog", "right Side", None, -1))
        self.sidesSet_btn.setText(QtWidgets.QApplication.translate("Dialog", "Set", None, -1))
        self.display_gb.setTitle(QtWidgets.QApplication.translate("Dialog", "Display", None, -1))
        self.jointsVis_cb.setText(QtWidgets.QApplication.translate("Dialog", "Joints", None, -1))
        self.jointsTempl_cb.setText(QtWidgets.QApplication.translate("Dialog", "Templ", None, -1))
        self.posersVis_cb.setText(QtWidgets.QApplication.translate("Dialog", "Posers", None, -1))
        self.controlsVis_cb.setText(QtWidgets.QApplication.translate("Dialog", "Controls", None, -1))
        self.map_gb.setTitle(QtWidgets.QApplication.translate("Dialog", "Map", None, -1))
        self.save_btn.setText(QtWidgets.QApplication.translate("Dialog", "Save..", None, -1))
        self.load_btn.setText(QtWidgets.QApplication.translate("Dialog", "Load..", None, -1))

