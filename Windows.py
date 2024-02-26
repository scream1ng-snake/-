from Routes import Routes
from RunningWindowUI import RunningWindowUI
from BeginWindowUI import BeginWindowUI
from PySide6.QtCore import QSettings, QAbstractTableModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from os import path

# логика


class RunningWindowLogic:
    # сам UI из Qt Designera
    ui = RunningWindowUI()

    # монтируем весь UI от Qt Designera
    def setupUi(self, MainWindow):
        self.ui.setupUi(MainWindow)

# логика


class BeginWindowLogic:
    # сам UI из Qt Designera
    ui = BeginWindowUI()

    # монтируем весь UI от Qt Designera
    def setupUi(self, MainWindow):
        self.ui.setupUi(MainWindow)

        # бахаем обработчики
        self.ui.path_browse_button.clicked.connect(self.selectPath)
        self.ui.start_recogntion.clicked.connect(self.beginWork)

        # вспоминаем прошлые настройки
        self.path = MainWindow.settings.value(MainWindow.SETTINGS_PATH, '', type=str)
        if(self.path):
            self.ui.path_browse_input.setText(self.path)
            self.ui.error_path_alert.hide()
        else:
            self.ui.error_path_alert.show()  
            self.ui.error_path_alert.setText('Папка не выбрана*')  
        self.parrent = MainWindow

    def selectPath(self):
        self.path = QFileDialog.getExistingDirectory(self.parrent, "Выбрать папку", "/")
        if (self.path):
            self.ui.path_browse_input.setText(self.path)
            self.ui.error_path_alert.hide()
            self.parrent.settings.setValue(self.parrent.SETTINGS_PATH, self.path)
            self.parrent.settings.sync()
        else:
            self.ui.error_path_alert.show()  
            self.ui.error_path_alert.setText('Папка не выбрана*')  
    
    def beginWork(self):
        typedPath = self.ui.path_browse_input.text()

        if (typedPath):
            if (path.isdir(typedPath)):
                self.startWork()
            else:
                errText = 'Такой папки не существует*'
                self.ui.error_path_alert.setText(errText)
                self.showError(errText)
        else:
            errText = 'Папка не выбрана*'
            self.ui.error_path_alert.setText(errText)
            self.showError(errText)

    def showError(self, text: str):
        QMessageBox.critical(None, text, text, QMessageBox.Ok)

    def startWork(self):
        pass
