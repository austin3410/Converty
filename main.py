from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os

import ui.mainwindow as Ui_MainWindow

import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.m_ui = Ui_MainWindow.Ui_Converty()
        self.m_ui.setupUi(self)
    
    # Button Functions
    def browserFolderSlot(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)

        if dlg.exec_():
            self.m_ui.treeWidget.clear()
            folderpath = dlg.selectedFiles()[0]
            directory_name = os.path.dirname(folderpath)
            self.m_ui.treeWidget.setHeaderLabel(directory_name)
            self.m_ui.treeWidget.setHeaderHidden(False)
            self.load_project_structure(folderpath, self.m_ui.treeWidget)
    
    def browserFileSlot(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Filter.Files)

        if dlg.exec_():
            filename = dlg.selectedFiles()[0]
            self.load_project_structure(filename, self.m_ui.treeWidget)
    
    def beginConvert(self):
        convert_to = self.m_ui.comboBox.currentText()
        tree = self.m_ui.treeWidget
        iterator = QtWidgets.QTreeWidgetItemIterator(tree, QTreeWidgetItemIterator.All)
        while iterator.value():
            item = iterator.value()
            rootpath = tree.headerItem
            print(rootpath)
            filename, file_extension = os.path.splitext(item.text(0))
            print(file_extension)
            iterator += 1

    # Supporting Functions
    
    def load_project_structure(self, startpath, tree):
        if os.path.isdir(startpath):
            for element in os.listdir(startpath):
                path_info = startpath + "/" + element
                if os.path.isdir(path_info):
                    self.add_tree_folder(tree, path_info, element)
                else:
                    
                    self.add_tree_item(tree, element)           
        else:
            self.add_tree_item(tree, startpath)
    
    def add_tree_item(self, tree, element):
        filename, file_extension = os.path.splitext(element)
        file_extension = file_extension.replace(".", "")
        if os.path.exists(f'assets/icons/png/{file_extension}.png'):
            parent_itm = QTreeWidgetItem(tree, [element])
            parent_itm.setIcon(0, QIcon(f'assets/icons/png/{file_extension}.png'))

    def add_tree_folder(self, tree, path_info, element):
        parent_itm = QTreeWidgetItem(tree, [element])
        self.load_project_structure(path_info, parent_itm)
        parent_itm.setIcon(0, QIcon('assets/icons/png/folder.png'))



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()