# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Pavel\Dropbox\mayaScripts\matchRig\matchRig_bakeWindow.ui'
#
# Created: Wed Aug 30 19:25:43 2017
#      by: pyside-uic 0.2.14 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 593)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(250, 420))
        MainWindow.setMaximumSize(QtCore.QSize(250, 1000))
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.import_frame = QtGui.QFrame(self.centralwidget)
        self.import_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.import_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.import_frame.setObjectName("import_frame")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.import_frame)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rigs_comboBox = QtGui.QComboBox(self.import_frame)
        self.rigs_comboBox.setObjectName("rigs_comboBox")
        self.horizontalLayout_3.addWidget(self.rigs_comboBox)
        self.addRig_btn = QtGui.QPushButton(self.import_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addRig_btn.sizePolicy().hasHeightForWidth())
        self.addRig_btn.setSizePolicy(sizePolicy)
        self.addRig_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.addRig_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.addRig_btn.setObjectName("addRig_btn")
        self.horizontalLayout_3.addWidget(self.addRig_btn)
        self.removeRig_btn = QtGui.QPushButton(self.import_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeRig_btn.sizePolicy().hasHeightForWidth())
        self.removeRig_btn.setSizePolicy(sizePolicy)
        self.removeRig_btn.setMinimumSize(QtCore.QSize(40, 20))
        self.removeRig_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.removeRig_btn.setObjectName("removeRig_btn")
        self.horizontalLayout_3.addWidget(self.removeRig_btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.importRig_btn = QtGui.QPushButton(self.import_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importRig_btn.sizePolicy().hasHeightForWidth())
        self.importRig_btn.setSizePolicy(sizePolicy)
        self.importRig_btn.setMinimumSize(QtCore.QSize(50, 25))
        self.importRig_btn.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.importRig_btn.setObjectName("importRig_btn")
        self.verticalLayout_6.addWidget(self.importRig_btn)
        self.verticalLayout.addWidget(self.import_frame)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.connectRig_btn = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectRig_btn.sizePolicy().hasHeightForWidth())
        self.connectRig_btn.setSizePolicy(sizePolicy)
        self.connectRig_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.connectRig_btn.setObjectName("connectRig_btn")
        self.horizontalLayout.addWidget(self.connectRig_btn)
        self.bakeControls_btn = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bakeControls_btn.sizePolicy().hasHeightForWidth())
        self.bakeControls_btn.setSizePolicy(sizePolicy)
        self.bakeControls_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.bakeControls_btn.setObjectName("bakeControls_btn")
        self.horizontalLayout.addWidget(self.bakeControls_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.main_frame = QtGui.QFrame(self.centralwidget)
        self.main_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.main_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.main_frame)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.bakeIkFk_btn = QtGui.QToolButton(self.main_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bakeIkFk_btn.sizePolicy().hasHeightForWidth())
        self.bakeIkFk_btn.setSizePolicy(sizePolicy)
        self.bakeIkFk_btn.setMinimumSize(QtCore.QSize(50, 24))
        self.bakeIkFk_btn.setMaximumSize(QtCore.QSize(1000, 24))
        self.bakeIkFk_btn.setObjectName("bakeIkFk_btn")
        self.gridLayout.addWidget(self.bakeIkFk_btn, 1, 1, 1, 1)
        self.switchParent_btn = QtGui.QToolButton(self.main_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.switchParent_btn.sizePolicy().hasHeightForWidth())
        self.switchParent_btn.setSizePolicy(sizePolicy)
        self.switchParent_btn.setMinimumSize(QtCore.QSize(50, 24))
        self.switchParent_btn.setMaximumSize(QtCore.QSize(1000, 24))
        self.switchParent_btn.setObjectName("switchParent_btn")
        self.gridLayout.addWidget(self.switchParent_btn, 2, 0, 1, 1)
        self.switchIkFk_btn = QtGui.QToolButton(self.main_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.switchIkFk_btn.sizePolicy().hasHeightForWidth())
        self.switchIkFk_btn.setSizePolicy(sizePolicy)
        self.switchIkFk_btn.setMinimumSize(QtCore.QSize(50, 24))
        self.switchIkFk_btn.setMaximumSize(QtCore.QSize(1000, 24))
        self.switchIkFk_btn.setObjectName("switchIkFk_btn")
        self.gridLayout.addWidget(self.switchIkFk_btn, 1, 0, 1, 1)
        self.switchParentRange_btn = QtGui.QToolButton(self.main_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.switchParentRange_btn.sizePolicy().hasHeightForWidth())
        self.switchParentRange_btn.setSizePolicy(sizePolicy)
        self.switchParentRange_btn.setMinimumSize(QtCore.QSize(50, 24))
        self.switchParentRange_btn.setMaximumSize(QtCore.QSize(1000, 24))
        self.switchParentRange_btn.setObjectName("switchParentRange_btn")
        self.gridLayout.addWidget(self.switchParentRange_btn, 2, 1, 1, 1)
        self.alignTwoHanded_btn = QtGui.QToolButton(self.main_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alignTwoHanded_btn.sizePolicy().hasHeightForWidth())
        self.alignTwoHanded_btn.setSizePolicy(sizePolicy)
        self.alignTwoHanded_btn.setMinimumSize(QtCore.QSize(50, 24))
        self.alignTwoHanded_btn.setMaximumSize(QtCore.QSize(1000, 24))
        self.alignTwoHanded_btn.setObjectName("alignTwoHanded_btn")
        self.gridLayout.addWidget(self.alignTwoHanded_btn, 3, 0, 1, 1)
        self.alignTwoHandedRange_btn = QtGui.QToolButton(self.main_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alignTwoHandedRange_btn.sizePolicy().hasHeightForWidth())
        self.alignTwoHandedRange_btn.setSizePolicy(sizePolicy)
        self.alignTwoHandedRange_btn.setMinimumSize(QtCore.QSize(50, 24))
        self.alignTwoHandedRange_btn.setMaximumSize(QtCore.QSize(1000, 24))
        self.alignTwoHandedRange_btn.setObjectName("alignTwoHandedRange_btn")
        self.gridLayout.addWidget(self.alignTwoHandedRange_btn, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.line_3 = QtGui.QFrame(self.main_frame)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.bakeSceleton_btn = QtGui.QPushButton(self.main_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bakeSceleton_btn.sizePolicy().hasHeightForWidth())
        self.bakeSceleton_btn.setSizePolicy(sizePolicy)
        self.bakeSceleton_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.bakeSceleton_btn.setObjectName("bakeSceleton_btn")
        self.verticalLayout_2.addWidget(self.bakeSceleton_btn)
        self.line_2 = QtGui.QFrame(self.main_frame)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.exclude_groupBox = QtGui.QGroupBox(self.main_frame)
        self.exclude_groupBox.setFlat(False)
        self.exclude_groupBox.setCheckable(True)
        self.exclude_groupBox.setChecked(True)
        self.exclude_groupBox.setObjectName("exclude_groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.exclude_groupBox)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.exclude_frame = QtGui.QFrame(self.exclude_groupBox)
        self.exclude_frame.setEnabled(True)
        self.exclude_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.exclude_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.exclude_frame.setObjectName("exclude_frame")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.exclude_frame)
        self.verticalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtGui.QLabel(self.exclude_frame)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.listWidget = QtGui.QListWidget(self.exclude_frame)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_4.addWidget(self.listWidget)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.add_btn = QtGui.QToolButton(self.exclude_frame)
        self.add_btn.setMinimumSize(QtCore.QSize(50, 0))
        self.add_btn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.add_btn.setObjectName("add_btn")
        self.verticalLayout_5.addWidget(self.add_btn)
        self.remove_btn = QtGui.QToolButton(self.exclude_frame)
        self.remove_btn.setMinimumSize(QtCore.QSize(50, 0))
        self.remove_btn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.remove_btn.setObjectName("remove_btn")
        self.verticalLayout_5.addWidget(self.remove_btn)
        self.clear_btn = QtGui.QToolButton(self.exclude_frame)
        self.clear_btn.setMinimumSize(QtCore.QSize(50, 0))
        self.clear_btn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clear_btn.setObjectName("clear_btn")
        self.verticalLayout_5.addWidget(self.clear_btn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addWidget(self.exclude_frame)
        self.verticalLayout_2.addWidget(self.exclude_groupBox)
        self.clearKeys_btn = QtGui.QPushButton(self.main_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearKeys_btn.sizePolicy().hasHeightForWidth())
        self.clearKeys_btn.setSizePolicy(sizePolicy)
        self.clearKeys_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.clearKeys_btn.setObjectName("clearKeys_btn")
        self.verticalLayout_2.addWidget(self.clearKeys_btn)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.export_btn = QtGui.QPushButton(self.main_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_btn.sizePolicy().hasHeightForWidth())
        self.export_btn.setSizePolicy(sizePolicy)
        self.export_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.export_btn.setObjectName("export_btn")
        self.horizontalLayout_2.addWidget(self.export_btn)
        self.import_btn = QtGui.QPushButton(self.main_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_btn.sizePolicy().hasHeightForWidth())
        self.import_btn.setSizePolicy(sizePolicy)
        self.import_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.import_btn.setObjectName("import_btn")
        self.horizontalLayout_2.addWidget(self.import_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Bake Match Rig", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "1. Open animation scene                                                      2. Import match rig                                                                        3. click Connect Rig and Bake Controls buttons                                          4. After edit animation, click Bake Sceleton", None, QtGui.QApplication.UnicodeUTF8))
        self.addRig_btn.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.removeRig_btn.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.importRig_btn.setText(QtGui.QApplication.translate("MainWindow", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.connectRig_btn.setText(QtGui.QApplication.translate("MainWindow", "Connect Rig", None, QtGui.QApplication.UnicodeUTF8))
        self.bakeControls_btn.setText(QtGui.QApplication.translate("MainWindow", "Bake Controls", None, QtGui.QApplication.UnicodeUTF8))
        self.bakeIkFk_btn.setText(QtGui.QApplication.translate("MainWindow", "Range", None, QtGui.QApplication.UnicodeUTF8))
        self.switchParent_btn.setText(QtGui.QApplication.translate("MainWindow", "Switch Parent", None, QtGui.QApplication.UnicodeUTF8))
        self.switchIkFk_btn.setText(QtGui.QApplication.translate("MainWindow", "Switch Ik/Fk", None, QtGui.QApplication.UnicodeUTF8))
        self.switchParentRange_btn.setText(QtGui.QApplication.translate("MainWindow", "Range", None, QtGui.QApplication.UnicodeUTF8))
        self.alignTwoHanded_btn.setText(QtGui.QApplication.translate("MainWindow", "Align TwoHanded", None, QtGui.QApplication.UnicodeUTF8))
        self.alignTwoHandedRange_btn.setText(QtGui.QApplication.translate("MainWindow", "Range", None, QtGui.QApplication.UnicodeUTF8))
        self.bakeSceleton_btn.setText(QtGui.QApplication.translate("MainWindow", "Bake Sceleton", None, QtGui.QApplication.UnicodeUTF8))
        self.exclude_groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Exclude List", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "This objects not clear translate keys.", None, QtGui.QApplication.UnicodeUTF8))
        self.add_btn.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_btn.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_btn.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.clearKeys_btn.setText(QtGui.QApplication.translate("MainWindow", "Clear Keys", None, QtGui.QApplication.UnicodeUTF8))
        self.export_btn.setText(QtGui.QApplication.translate("MainWindow", "Hot Export", None, QtGui.QApplication.UnicodeUTF8))
        self.import_btn.setText(QtGui.QApplication.translate("MainWindow", "Hot Import", None, QtGui.QApplication.UnicodeUTF8))

