import os
import sys
from PySide6.QtCore import QSettings, QAbstractTableModel, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from Routes import Routes
from Windows import BeginWindowLogic, RunningWindowLogic
from uuid import uuid4
from utils import isUUID, WsClient


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
    ws: WsClient
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
    SETTINGS_CLIENT_ID = 'settings/clientID'

    # Список имен файлов для распознавния
    files = []
    filesCount = 0

    def __init__(self):
        super(LexemaRecognitionStantion, self).__init__()
        self.settings = QSettings('app', 'app', self)
        self.checkMyClientID()
        for route in self.routes:
            self.routes[route].setupUi(self)

        self.ws = WsClient(self, 'ws://localhost:3000')

        def onWsError():
            self.navigateTo(Routes.Begin)
            self.showError('Соединения потеряно')
        
        self.ws.connect(onReject=onWsError)

    # простая авторизация чтобы хоть как-то понимать кто есть кто
    def checkMyClientID(self): 
        clientID = self.settings.value(self.SETTINGS_CLIENT_ID, '', type=str)
        if not clientID:
            self.clientID = str(uuid4())
            self.settings.setValue(self.SETTINGS_CLIENT_ID, self.clientID)
            self.settings.sync()
        elif isinstance(clientID, str) and isUUID(clientID):
            self.clientID = clientID
    
    def showError(self, text: str):
        QMessageBox.critical(None, text, text, QMessageBox.Ok)

            

if(__name__ == '__main__'):
    app = QApplication(sys.argv)
    window = LexemaRecognitionStantion()
    window.show()
    sys.exit(app.exec())