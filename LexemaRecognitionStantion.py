import os
import sys
from PySide6.QtCore import QSettings, QAbstractTableModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from Routes import Routes
from Windows import BeginWindowLogic, RunningWindowLogic


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


class LexemaRecognitionStantion(QMainWindow):
    # доступные экраны в приложении
    routes = {Routes.Watching: RunningWindowLogic(),
              Routes.Begin: BeginWindowLogic()}

    # текущий экран
    route: Routes = Routes.Begin

    # переключить экран
    def navigateTo(self, route: Routes):
        self.hide()
        self.route = route
        self.currentWindow = self.routes[route]
        self.currentWindow.setupUi(self)
        self.show()

    # место сохранения настроек для приложения
    SETTINGS_PATH = 'settings/path'

    def __init__(self):
        super(LexemaRecognitionStantion, self).__init__()
        self.settings = QSettings('app', 'app', self)
        for route in self.routes:
            self.routes[route].setupUi(self)

if(__name__ == '__main__'):
    app = QApplication(sys.argv)
    window = LexemaRecognitionStantion()
    window.show()
    sys.exit(app.exec())