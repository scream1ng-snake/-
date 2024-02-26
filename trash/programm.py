
import os
import sys
from PySide6.QtCore import QSettings, QAbstractTableModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui_main import Ui_MainWindow

# class MainWindow(QWidget):
#     name = 'Станция распознования'
#     dirPath = ''
#     SETTINGS_PATH = 'settings/path'

#     def getDirectory(self):
#         self.dirPath = QFileDialog.getExistingDirectory(self,"Выбрать папку","/")
#         self.pathInput.setText(self.dirPath)
#         self.settings.setValue(self.SETTINGS_PATH, self.dirPath)
#         self.settings.sync()

#     def showInput(self):
#         self.settings = QSettings('app', 'app', self)
#         path_state = self.settings.value(self.SETTINGS_PATH, '', type=str)
#         pathInputLabel = QLabel('Выберите папку с изображениями для распознавания', parent=self)
#         self.pathInput = QLineEdit(parent=self)
#         self.pathInput.setPlaceholderText('путь к папке')
#         self.pathInput.setText(path_state)
#         self.browseButton = QPushButton('Browse', parent=self)
#         self.browseButton.clicked.connect(self.getDirectory)
#         if(path_state):
#             self.pathInput.setDisabled(True)
        
        
#         row = QHBoxLayout()
#         row.addWidget(self.pathInput)
#         row.addWidget(self.browseButton)

#         column = QVBoxLayout()
#         column.addWidget(pathInputLabel)
#         column.addLayout(row)
#         self.setLayout(column)
            
        
            

        
    
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle(self.name)
#         self.resize(600, 300)
#         self.showInput()
        

# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec()

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])


class RecognitionStantion(QMainWindow): 
    path_state = ''
    SETTINGS_PATH = 'settings/path'
    files = []

    def browseDir(self):
        self.path_state = QFileDialog.getExistingDirectory(self,"Выбрать папку","/")
        self.ui.lineEdit.setText(self.path_state)
        self.settings.setValue(self.SETTINGS_PATH, self.path_state)
        self.settings.sync()
        if(self.path_state == '' or self.path_state == None):
            self.hideElems()
        else:
            self.files = [f for f in os.listdir(self.path_state) if os.path.isfile(os.path.join(self.path_state, f))]
            self.showElems(str(len(self.files)), self.path_state)
        


    def hideElems(self):
        self.ui.tableView.hide()
        self.ui.pushButton_2.hide()
        self.ui.pushButton_3.hide()
        self.ui.label_2.setText('Папка не выбрана')
        self.ui.label_3.hide()
        self.ui.label_4.hide()
        self.ui.label_5.hide()
    
    def showElems(self, count, path):
        self.ui.tableView.show()
        self.ui.pushButton_2.show()
        self.ui.pushButton_3.show()
        self.ui.label_2.setText('Папка:')
        self.ui.label_3.show()
        self.ui.label_4.show()
        self.ui.label_4.setText(path)
        self.ui.label_5.show()
        self.ui.label_5.setText(count)
        self.fillTable(self.files)

    def fillTable(self, fileList):
            
        data = list(map((lambda x: [x]), fileList))

        self.model = TableModel(data)
        self.ui.tableView.setModel(self.model)

    def __init__(self):
        super(RecognitionStantion, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings = QSettings('app', 'app', self)
        self.path_state = self.settings.value(self.SETTINGS_PATH, '', type=str)
        self.ui.pushButton.clicked.connect(self.browseDir)
        
        if(self.path_state == '' or self.path_state == None):
            self.hideElems()
        else:
            self.ui.lineEdit.setText(self.path_state)
            self.files = [f for f in os.listdir(self.path_state) if os.path.isfile(os.path.join(self.path_state, f))]
            self.showElems(str(len(self.files)), self.path_state)

        



if(__name__ == '__main__'):
    app = QApplication(sys.argv)
    window = RecognitionStantion()
    window.show()


    sys.exit(app.exec())