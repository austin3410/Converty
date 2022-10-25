from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
from PIL import Image
from math import floor

import ui.mainwindow as Ui_MainWindow
from covnerty_tools.convert2 import Convert2

import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.output_path = None
        self.m_ui = Ui_MainWindow.Ui_Converty()
        self.m_ui.setupUi(self)

        self.convert_flags = {
            "PNG": {"PIL_FLAG": "RGBA", "EXT": ".png"}, 
            "JPG": {"PIL_FLAG": "RGB", "EXT": ".jpg"}, 
            #"Greyscale": {"PIL_FLAG": "LA", "EXT": "CURRENT"}, 
            "PDF": {"PIL_FLAG": "RGB", "EXT": ".pdf"}}
        
        self.support_exts = [".png", ".jpg", ".pdf"]

        self.DEFAULT_STYLE = """
QProgressBar{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center
}

QProgressBar::chunk {
    background-color: lightblue;
}
"""
        self.ERROR_STYLE = """
QProgressBar{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center
}

QProgressBar::chunk {
    background-color: red;
}
"""
        self.SUCCESS_STYLE = """
QProgressBar{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center
}

QProgressBar::chunk {
    background-color: green;
}
"""
    
    # Button Functions
    def browserFolderSlot(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)

        if dlg.exec_():
            folderpath = dlg.selectedFiles()[0]
            recursive = self.m_ui.isRecursive.isChecked()
            self.parse_folder(folderpath, self.m_ui.listWidget, recursive)
    
    def browserFileSlot(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Filter.Files)

        if dlg.exec_():
            filename = dlg.selectedFiles()[0]
            recursive = self.m_ui.isRecursive.isChecked()
            self.parse_folder(filename, self.m_ui.listWidget, recursive)
    
    def browserSetOutput(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)

        if dlg.exec_():
            self.output_path = dlg.selectedFiles()[0]
    
    def beginConvert(self):
        if self.output_path != None:
            list = self.m_ui.listWidget
            items = []
            for i in range(list.count()):
                items.append(list.item(i).text())
            
            if items == []:
                return self.popup_msg("No Items in List...", "Please add at least 1 item to the list!", "WARNING")
            convert_to = self.m_ui.comboBox.currentText()
            self.convert_images(items, convert_to, self.output_path)
        else:
            self.popup_msg("Set Output Path", "Please set an output path!", "ERROR")
    
    def clearList(self):
        self.m_ui.listWidget.clear()
        self.m_ui.ItemCount.setText(f"{self.m_ui.listWidget.count()} Items")
    
    def clearSelection(self):
        selected = self.m_ui.listWidget.selectedItems()
        if not selected: return
        for item in selected:
            self.m_ui.listWidget.takeItem(self.m_ui.listWidget.row(item))
            self.m_ui.ItemCount.setText(f"{self.m_ui.listWidget.count()} Items")

    # Supporting Functions

    def parse_folder(self, folderpath, list, recursive):
        if os.path.isdir(folderpath):
            for item in os.listdir(folderpath):
                if os.path.isdir(folderpath + "/" + item) and recursive == True:
                    new_folderpath = folderpath + "/" + item
                    self.parse_folder(new_folderpath, list, recursive)
                elif os.path.isfile(folderpath + "/" + item):
                    self.add_item_to_list(folderpath, list, item)
                else:
                    #print(item)
                    pass
        else:
            item = os.path.basename(folderpath)
            folderpath = os.path.dirname(folderpath)
            self.add_item_to_list(folderpath, list, item)
        self.m_ui.ItemCount.setText(f"{list.count()} Items")
    
    def add_item_to_list(self, folderpath, list, item):
        filename, file_ext = os.path.splitext(item)
        if str(file_ext).lower() in self.support_exts:
            if item:
                list.addItem(folderpath + "/" + item)
                self.m_ui.ItemCount.setText(f"{list.count()} Items")
    
    def convert_images(self, items, convert_to, output_path):
        self.m_ui.progressBar.setStyleSheet(self.DEFAULT_STYLE)
        self.m_ui.progressBar.setValue(0)
        self.m_ui.progressBar.setEnabled(True)
        greyscale = self.m_ui.isGreyscale.isChecked()
        percent_per_image = floor(100/len(items))
        global error
        error = None
        self.convert_count = 0

        for image in items:
            self.m_ui.ItemCount.setText(f"{self.convert_count}/{self.m_ui.listWidget.count()}\nItems Converted")
            try:
                Convert2(image, convert_to, self.convert_flags, output_path, greyscale)

                current_progressbar_val = self.m_ui.progressBar.value()
                self.m_ui.progressBar.setValue(current_progressbar_val + percent_per_image)
                self.convert_count += 1

            
            except Exception as e:
                print(e)
                error = e
                msg = "Something went wrong!\n"\
                    f"Couldn't convert\n{image}\n to {convert_to}!"
                self.popup_msg("Error", msg, "ERROR")


        self.m_ui.ItemCount.setText(f"{self.convert_count}/{self.m_ui.listWidget.count()}\nItems Converted")
        if error == None:
            self.m_ui.progressBar.setValue(100)
            self.m_ui.progressBar.setStyleSheet(self.SUCCESS_STYLE)
            self.popup_msg("Conversion Completed!", "All images converted successfully!")
        else:
            self.m_ui.progressBar.setStyleSheet(self.ERROR_STYLE)
            self.popup_msg("Partial Completion..", "Conversion partially complete, there were some errors!", "ERROR")
    
    def popup_msg(self, title, msg, flavor=None):
        flavors = {"ERROR": {"ICON": QMessageBox.Icon.Critical, "BUTTON": QMessageBox.Close}, "WARNING": {"ICON": QMessageBox.Icon.Warning, "BUTTON": QMessageBox.Close}}
        popup = QMessageBox()
        popup.setWindowTitle(title)
        popup.setText(msg)

        if flavor:
            icon = flavors[flavor]["ICON"]
            button = flavors[flavor]["BUTTON"]
            popup.setIcon(icon)
            popup.setStandardButtons(button)
        popup.exec_()
    
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()