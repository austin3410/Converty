# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setOutputPathDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_setOutputPathDialog(object):
    def setupUi(self, setOutputPathDialog):
        setOutputPathDialog.setObjectName("setOutputPathDialog")
        setOutputPathDialog.resize(282, 66)
        setOutputPathDialog.setMinimumSize(QtCore.QSize(282, 66))
        setOutputPathDialog.setMaximumSize(QtCore.QSize(282, 66))
        self.gridLayout = QtWidgets.QGridLayout(setOutputPathDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(setOutputPathDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.buttonBox = QtWidgets.QDialogButtonBox(setOutputPathDialog)
        self.buttonBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)

        self.retranslateUi(setOutputPathDialog)
        self.buttonBox.accepted.connect(setOutputPathDialog.accept)
        self.buttonBox.rejected.connect(setOutputPathDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(setOutputPathDialog)

    def retranslateUi(self, setOutputPathDialog):
        _translate = QtCore.QCoreApplication.translate
        setOutputPathDialog.setWindowTitle(_translate("setOutputPathDialog", "Set Output Path"))
        self.label.setText(_translate("setOutputPathDialog", "Please set an Output Path!"))
