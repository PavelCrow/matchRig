# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Pavel\Dropbox\mayaScripts\matchRig\matchRig_bakeWindow.ui'
#
# Created: Fri Jul 19 17:55:15 2019
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 606)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(250, 360))
        MainWindow.setMaximumSize(QtCore.QSize(250, 1000))
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.import_frame = QtWidgets.QFrame(self.centralwidget)
        self.import_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.import_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.import_frame.setObjectName("import_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.import_frame)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rigs_comboBox = QtWidgets.QComboBox(self.import_frame)
        self.rigs_comboBox.setObjectName("rigs_comboBox")
        self.horizontalLayout_3.addWidget(self.rigs_comboBox)
        self.addRig_btn = QtWidgets.QPushButton(self.import_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addRig_btn.sizePolicy().hasHeightForWidth())
        self.addRig_btn.setSizePolicy(sizePolicy)
        self.addRig_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.addRig_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.addRig_btn.setObjectName("addRig_btn")
        self.horizontalLayout_3.addWidget(self.addRig_btn)
        self.removeRig_btn = QtWidgets.QPushButton(self.import_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeRig_btn.sizePolicy().hasHeightForWidth())
        self.removeRig_btn.setSizePolicy(sizePolicy)
        self.removeRig_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.removeRig_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.removeRig_btn.setObjectName("removeRig_btn")
        self.horizontalLayout_3.addWidget(self.removeRig_btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.importRig_btn = QtWidgets.QPushButton(self.import_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importRig_btn.sizePolicy().hasHeightForWidth())
        self.importRig_btn.setSizePolicy(sizePolicy)
        self.importRig_btn.setMinimumSize(QtCore.QSize(50, 25))
        self.importRig_btn.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.importRig_btn.setObjectName("importRig_btn")
        self.verticalLayout_6.addWidget(self.importRig_btn)
        self.importDefaultFbx_btn = QtWidgets.QPushButton(self.import_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importDefaultFbx_btn.sizePolicy().hasHeightForWidth())
        self.importDefaultFbx_btn.setSizePolicy(sizePolicy)
        self.importDefaultFbx_btn.setMinimumSize(QtCore.QSize(50, 25))
        self.importDefaultFbx_btn.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.importDefaultFbx_btn.setObjectName("importDefaultFbx_btn")
        self.verticalLayout_6.addWidget(self.importDefaultFbx_btn)
        self.verticalLayout.addWidget(self.import_frame)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.connectRig_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectRig_btn.sizePolicy().hasHeightForWidth())
        self.connectRig_btn.setSizePolicy(sizePolicy)
        self.connectRig_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.connectRig_btn.setObjectName("connectRig_btn")
        self.horizontalLayout.addWidget(self.connectRig_btn)
        self.bakeControls_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bakeControls_btn.sizePolicy().hasHeightForWidth())
        self.bakeControls_btn.setSizePolicy(sizePolicy)
        self.bakeControls_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.bakeControls_btn.setObjectName("bakeControls_btn")
        self.horizontalLayout.addWidget(self.bakeControls_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.ikfk_frame = QtWidgets.QFrame(self.centralwidget)
        self.ikfk_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ikfk_frame.setObjectName("ikfk_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.ikfk_frame)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.switchIkFk_btn = QtWidgets.QPushButton(self.ikfk_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.switchIkFk_btn.sizePolicy().hasHeightForWidth())
        self.switchIkFk_btn.setSizePolicy(sizePolicy)
        self.switchIkFk_btn.setMinimumSize(QtCore.QSize(50, 24))
        self.switchIkFk_btn.setMaximumSize(QtCore.QSize(1000, 24))
        self.switchIkFk_btn.setObjectName("switchIkFk_btn")
        self.gridLayout.addWidget(self.switchIkFk_btn, 1, 0, 1, 1)
        self.switchParent_btn = QtWidgets.QPushButton(self.ikfk_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.switchParent_btn.sizePolicy().hasHeightForWidth())
        self.switchParent_btn.setSizePolicy(sizePolicy)
        self.switchParent_btn.setMinimumSize(QtCore.QSize(50, 24))
        self.switchParent_btn.setMaximumSize(QtCore.QSize(1000, 24))
        self.switchParent_btn.setObjectName("switchParent_btn")
        self.gridLayout.addWidget(self.switchParent_btn, 2, 0, 1, 1)
        self.alignTwoHanded_btn = QtWidgets.QPushButton(self.ikfk_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alignTwoHanded_btn.sizePolicy().hasHeightForWidth())
        self.alignTwoHanded_btn.setSizePolicy(sizePolicy)
        self.alignTwoHanded_btn.setMinimumSize(QtCore.QSize(50, 24))
        self.alignTwoHanded_btn.setMaximumSize(QtCore.QSize(1000, 24))
        self.alignTwoHanded_btn.setObjectName("alignTwoHanded_btn")
        self.gridLayout.addWidget(self.alignTwoHanded_btn, 3, 0, 1, 1)
        self.bakeIkFk_btn = QtWidgets.QPushButton(self.ikfk_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bakeIkFk_btn.sizePolicy().hasHeightForWidth())
        self.bakeIkFk_btn.setSizePolicy(sizePolicy)
        self.bakeIkFk_btn.setMinimumSize(QtCore.QSize(50, 24))
        self.bakeIkFk_btn.setMaximumSize(QtCore.QSize(1000, 24))
        self.bakeIkFk_btn.setObjectName("bakeIkFk_btn")
        self.gridLayout.addWidget(self.bakeIkFk_btn, 1, 1, 1, 1)
        self.switchParentRange_btn = QtWidgets.QPushButton(self.ikfk_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.switchParentRange_btn.sizePolicy().hasHeightForWidth())
        self.switchParentRange_btn.setSizePolicy(sizePolicy)
        self.switchParentRange_btn.setMinimumSize(QtCore.QSize(50, 24))
        self.switchParentRange_btn.setMaximumSize(QtCore.QSize(1000, 24))
        self.switchParentRange_btn.setObjectName("switchParentRange_btn")
        self.gridLayout.addWidget(self.switchParentRange_btn, 2, 1, 1, 1)
        self.alignTwoHandedRange_btn = QtWidgets.QPushButton(self.ikfk_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alignTwoHandedRange_btn.sizePolicy().hasHeightForWidth())
        self.alignTwoHandedRange_btn.setSizePolicy(sizePolicy)
        self.alignTwoHandedRange_btn.setMinimumSize(QtCore.QSize(50, 24))
        self.alignTwoHandedRange_btn.setMaximumSize(QtCore.QSize(1000, 24))
        self.alignTwoHandedRange_btn.setObjectName("alignTwoHandedRange_btn")
        self.gridLayout.addWidget(self.alignTwoHandedRange_btn, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.ikfk_frame)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.ikfk_frame)
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.frame = QtWidgets.QFrame(self.main_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.hipTZero_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hipTZero_btn.sizePolicy().hasHeightForWidth())
        self.hipTZero_btn.setSizePolicy(sizePolicy)
        self.hipTZero_btn.setMinimumSize(QtCore.QSize(50, 24))
        self.hipTZero_btn.setMaximumSize(QtCore.QSize(16777215, 24))
        self.hipTZero_btn.setObjectName("hipTZero_btn")
        self.horizontalLayout_7.addWidget(self.hipTZero_btn)
        self.hipRZero_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hipRZero_btn.sizePolicy().hasHeightForWidth())
        self.hipRZero_btn.setSizePolicy(sizePolicy)
        self.hipRZero_btn.setMinimumSize(QtCore.QSize(50, 24))
        self.hipRZero_btn.setMaximumSize(QtCore.QSize(16777215, 24))
        self.hipRZero_btn.setObjectName("hipRZero_btn")
        self.horizontalLayout_7.addWidget(self.hipRZero_btn)
        self.pelvisTZero_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pelvisTZero_btn.sizePolicy().hasHeightForWidth())
        self.pelvisTZero_btn.setSizePolicy(sizePolicy)
        self.pelvisTZero_btn.setMinimumSize(QtCore.QSize(50, 24))
        self.pelvisTZero_btn.setMaximumSize(QtCore.QSize(1000, 24))
        self.pelvisTZero_btn.setObjectName("pelvisTZero_btn")
        self.horizontalLayout_7.addWidget(self.pelvisTZero_btn)
        self.pelvisRZero_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pelvisRZero_btn.sizePolicy().hasHeightForWidth())
        self.pelvisRZero_btn.setSizePolicy(sizePolicy)
        self.pelvisRZero_btn.setMinimumSize(QtCore.QSize(50, 24))
        self.pelvisRZero_btn.setMaximumSize(QtCore.QSize(1000, 24))
        self.pelvisRZero_btn.setObjectName("pelvisRZero_btn")
        self.horizontalLayout_7.addWidget(self.pelvisRZero_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.frame_2 = QtWidgets.QFrame(self.main_frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.matchFrom_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.matchFrom_lineEdit.setReadOnly(True)
        self.matchFrom_lineEdit.setObjectName("matchFrom_lineEdit")
        self.horizontalLayout_6.addWidget(self.matchFrom_lineEdit)
        self.matchFromSet_btn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matchFromSet_btn.sizePolicy().hasHeightForWidth())
        self.matchFromSet_btn.setSizePolicy(sizePolicy)
        self.matchFromSet_btn.setMinimumSize(QtCore.QSize(50, 20))
        self.matchFromSet_btn.setMaximumSize(QtCore.QSize(16777215, 20))
        self.matchFromSet_btn.setObjectName("matchFromSet_btn")
        self.horizontalLayout_6.addWidget(self.matchFromSet_btn)
        self.matchTo_lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.matchTo_lineEdit.setReadOnly(True)
        self.matchTo_lineEdit.setObjectName("matchTo_lineEdit")
        self.horizontalLayout_6.addWidget(self.matchTo_lineEdit)
        self.matchToSet_btn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matchToSet_btn.sizePolicy().hasHeightForWidth())
        self.matchToSet_btn.setSizePolicy(sizePolicy)
        self.matchToSet_btn.setMinimumSize(QtCore.QSize(50, 20))
        self.matchToSet_btn.setMaximumSize(QtCore.QSize(16777215, 20))
        self.matchToSet_btn.setObjectName("matchToSet_btn")
        self.horizontalLayout_6.addWidget(self.matchToSet_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.matchBake_btn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matchBake_btn.sizePolicy().hasHeightForWidth())
        self.matchBake_btn.setSizePolicy(sizePolicy)
        self.matchBake_btn.setMinimumSize(QtCore.QSize(50, 24))
        self.matchBake_btn.setMaximumSize(QtCore.QSize(1000, 24))
        self.matchBake_btn.setObjectName("matchBake_btn")
        self.verticalLayout_3.addWidget(self.matchBake_btn)
        self.verticalLayout_2.addWidget(self.frame_2)
        spacerItem3 = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.line_3 = QtWidgets.QFrame(self.main_frame)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.main_frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.skeletonRoot_lineEdit = QtWidgets.QLineEdit(self.main_frame)
        self.skeletonRoot_lineEdit.setObjectName("skeletonRoot_lineEdit")
        self.horizontalLayout_5.addWidget(self.skeletonRoot_lineEdit)
        self.setSceletonRoot_btn = QtWidgets.QPushButton(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setSceletonRoot_btn.sizePolicy().hasHeightForWidth())
        self.setSceletonRoot_btn.setSizePolicy(sizePolicy)
        self.setSceletonRoot_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.setSceletonRoot_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.setSceletonRoot_btn.setObjectName("setSceletonRoot_btn")
        self.horizontalLayout_5.addWidget(self.setSceletonRoot_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.bakeSceleton_btn = QtWidgets.QPushButton(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bakeSceleton_btn.sizePolicy().hasHeightForWidth())
        self.bakeSceleton_btn.setSizePolicy(sizePolicy)
        self.bakeSceleton_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.bakeSceleton_btn.setObjectName("bakeSceleton_btn")
        self.verticalLayout_2.addWidget(self.bakeSceleton_btn)
        self.line_2 = QtWidgets.QFrame(self.main_frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.export_btn = QtWidgets.QPushButton(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_btn.sizePolicy().hasHeightForWidth())
        self.export_btn.setSizePolicy(sizePolicy)
        self.export_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.export_btn.setObjectName("export_btn")
        self.horizontalLayout_2.addWidget(self.export_btn)
        self.import_btn = QtWidgets.QPushButton(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_btn.sizePolicy().hasHeightForWidth())
        self.import_btn.setSizePolicy(sizePolicy)
        self.import_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.import_btn.setObjectName("import_btn")
        self.horizontalLayout_2.addWidget(self.import_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.main_frame)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Bake Match Rig", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "1. Open animation scene                                                      2. Import match rig                                                                        3. click Connect Rig and Bake Controls buttons                                                                  4. After edit animation, click Bake Sceleton", None, -1))
        self.addRig_btn.setText(QtWidgets.QApplication.translate("MainWindow", "+", None, -1))
        self.removeRig_btn.setText(QtWidgets.QApplication.translate("MainWindow", "-", None, -1))
        self.importRig_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Import", None, -1))
        self.importDefaultFbx_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Import Default FBX", None, -1))
        self.connectRig_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Connect Rig and Bake", None, -1))
        self.bakeControls_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Bake Controls", None, -1))
        self.switchIkFk_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Switch Ik/Fk", None, -1))
        self.switchParent_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Switch Parent", None, -1))
        self.alignTwoHanded_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Align TwoHanded", None, -1))
        self.bakeIkFk_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Range", None, -1))
        self.switchParentRange_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Range", None, -1))
        self.alignTwoHandedRange_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Range", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Switches", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Convert to Zero", None, -1))
        self.hipTZero_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Hip T", None, -1))
        self.hipRZero_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Hip R", None, -1))
        self.pelvisTZero_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Pelvis T", None, -1))
        self.pelvisRZero_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Pelvis R", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Match Anmation", None, -1))
        self.matchFrom_lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "From..", None, -1))
        self.matchFromSet_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.matchTo_lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "To..", None, -1))
        self.matchToSet_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.matchBake_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Match Bake", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Skeleton Root", None, -1))
        self.skeletonRoot_lineEdit.setText(QtWidgets.QApplication.translate("MainWindow", "Armature", None, -1))
        self.setSceletonRoot_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Set", None, -1))
        self.bakeSceleton_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Bake Skeleton", None, -1))
        self.export_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Hot Export", None, -1))
        self.import_btn.setText(QtWidgets.QApplication.translate("MainWindow", "Hot Import", None, -1))

