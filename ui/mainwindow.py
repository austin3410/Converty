# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Converty(object):
    def setupUi(self, Converty):
        Converty.setObjectName("Converty")
        Converty.setEnabled(True)
        Converty.resize(755, 444)
        Converty.setMinimumSize(QtCore.QSize(755, 444))
        Converty.setAnimated(True)
        Converty.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Converty)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.removeSelectio = QtWidgets.QPushButton(self.centralwidget)
        self.removeSelectio.setMaximumSize(QtCore.QSize(146, 25))
        self.removeSelectio.setObjectName("removeSelectio")
        self.gridLayout.addWidget(self.removeSelectio, 0, 2, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 3, 0, 11, 4)
        self.loadFile = QtWidgets.QPushButton(self.centralwidget)
        self.loadFile.setMaximumSize(QtCore.QSize(126, 25))
        self.loadFile.setObjectName("loadFile")
        self.gridLayout.addWidget(self.loadFile, 5, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.ItemCount = QtWidgets.QLabel(self.centralwidget)
        self.ItemCount.setEnabled(True)
        self.ItemCount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ItemCount.setText("")
        self.ItemCount.setAlignment(QtCore.Qt.AlignCenter)
        self.ItemCount.setObjectName("ItemCount")
        self.gridLayout.addWidget(self.ItemCount, 11, 5, 2, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.loadFolder = QtWidgets.QPushButton(self.centralwidget)
        self.loadFolder.setMaximumSize(QtCore.QSize(126, 25))
        self.loadFolder.setObjectName("loadFolder")
        self.gridLayout.addWidget(self.loadFolder, 4, 5, 1, 1)
        self.setOutput = QtWidgets.QPushButton(self.centralwidget)
        self.setOutput.setMaximumSize(QtCore.QSize(126, 25))
        self.setOutput.setObjectName("setOutput")
        self.gridLayout.addWidget(self.setOutput, 13, 5, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 16, 0, 1, 4)
        self.clearList = QtWidgets.QPushButton(self.centralwidget)
        self.clearList.setMaximumSize(QtCore.QSize(147, 25))
        self.clearList.setObjectName("clearList")
        self.gridLayout.addWidget(self.clearList, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(126, 44))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 7, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.convert = QtWidgets.QPushButton(self.centralwidget)
        self.convert.setMinimumSize(QtCore.QSize(126, 25))
        self.convert.setMaximumSize(QtCore.QSize(126, 25))
        self.convert.setObjectName("convert")
        self.gridLayout.addWidget(self.convert, 16, 5, 1, 1)
        self.isRecursive = QtWidgets.QCheckBox(self.centralwidget)
        self.isRecursive.setChecked(True)
        self.isRecursive.setObjectName("isRecursive")
        self.gridLayout.addWidget(self.isRecursive, 3, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMaximumSize(QtCore.QSize(126, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 8, 5, 1, 1)
        self.isGreyscale = QtWidgets.QCheckBox(self.centralwidget)
        self.isGreyscale.setObjectName("isGreyscale")
        self.gridLayout.addWidget(self.isGreyscale, 9, 5, 1, 1, QtCore.Qt.AlignHCenter)
        Converty.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(Converty)
        self.statusBar.setObjectName("statusBar")
        Converty.setStatusBar(self.statusBar)
        self.actionLoadFolder = QtWidgets.QAction(Converty)
        self.actionLoadFolder.setObjectName("actionLoadFolder")
        self.actionLoad_File = QtWidgets.QAction(Converty)
        self.actionLoad_File.setObjectName("actionLoad_File")
        self.actionQuit = QtWidgets.QAction(Converty)
        self.actionQuit.setObjectName("actionQuit")

        self.retranslateUi(Converty)
        self.loadFile.clicked.connect(Converty.browserFileSlot)
        self.convert.clicked.connect(Converty.beginConvert)
        self.setOutput.clicked.connect(Converty.browserSetOutput)
        self.clearList.clicked.connect(Converty.clearList)
        self.removeSelectio.clicked.connect(Converty.clearSelection)
        self.loadFolder.clicked.connect(Converty.browserFolderSlot)
        QtCore.QMetaObject.connectSlotsByName(Converty)
        Converty.setTabOrder(self.loadFile, self.listWidget)

    def retranslateUi(self, Converty):
        _translate = QtCore.QCoreApplication.translate
        Converty.setWindowTitle(_translate("Converty", "Converty"))
        Converty.setWindowIcon(QtGui.QIcon("logo4.ico"))
        self.removeSelectio.setText(_translate("Converty", "Remove Selection"))
        self.listWidget.setSortingEnabled(True)
        self.loadFile.setToolTip(_translate("Converty", "<html><head/><body><p>Loads the selected image file.</p></body></html>"))
        self.loadFile.setText(_translate("Converty", "< Load File"))
        self.loadFolder.setToolTip(_translate("Converty", "<html><head/><body><p>Loads all of the supported content of a folder.<br/>---------<br/>If &quot;Recursive&quot; is enabled, it also loads the contents of all of the child folders within the selected folder.</p></body></html>"))
        self.loadFolder.setText(_translate("Converty", "<< Load Folder"))
        self.setOutput.setText(_translate("Converty", "Set Output Path.."))
        self.progressBar.setFormat(_translate("Converty", "%p%"))
        self.clearList.setText(_translate("Converty", "Clear List"))
        self.label.setText(_translate("Converty", "Convert to..."))
        self.convert.setText(_translate("Converty", "Convert!"))
        self.isRecursive.setToolTip(_translate("Converty", "<html><head/><body><p>When enabled, &quot;Load Folder&quot; will also load the contents of all the folders within it.</p></body></html>"))
        self.isRecursive.setText(_translate("Converty", "Recursive"))
        self.comboBox.setItemText(0, _translate("Converty", "PNG"))
        self.comboBox.setItemText(1, _translate("Converty", "JPG"))
        self.comboBox.setItemText(2, _translate("Converty", "PDF"))
        self.isGreyscale.setToolTip(_translate("Converty", "<html><head/><body><p>When enabled, Converty will attempt to convert the image into a black and white (Greyscale) version.</p></body></html>"))
        self.isGreyscale.setText(_translate("Converty", "Greyscale"))
        self.actionLoadFolder.setText(_translate("Converty", "Load Folder..."))
        self.actionLoad_File.setText(_translate("Converty", "Load File..."))
        self.actionQuit.setText(_translate("Converty", "Quit"))
