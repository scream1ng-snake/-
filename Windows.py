from Routes import Routes
from RunningWindowUI import RunningWindowUI
from BeginWindowUI import BeginWindowUI
from PySide6.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem, QHeaderView
from os import path, listdir
from enum import Enum
from fnmatch import fnmatch
from utils import WsClient

class ProgramStates(Enum):
    Initail = "Initail"
    Stoped = "Stoped"
    Running = "Running"
    Completed = "Completed"

class StatesLabels():
    Initail = "Готовы к запуску"
    Stoped = "Остановлено"
    Running = "Идёт распознавание..."
    Completed = "Готово"

class WsCommands():
    CONNECT = 'CONNECT'
    START = 'START'
    STOP = 'STOP'

# логика
class RunningWindowLogic:
    state = ProgramStates.Initail
    def setState(self, state:ProgramStates):
        self.state = state

        if(state == ProgramStates.Initail):
            self.ui.startButton.setEnabled(True)
            self.ui.stopButton.setDisabled(True)
            self.ui.progressBarLabel.setText(StatesLabels.Initail)
        elif(state == ProgramStates.Running):
            self.ui.startButton.setDisabled(True)
            self.ui.stopButton.setEnabled(True)
            self.ui.progressBarLabel.setText(StatesLabels.Running)
            msgObj = {
                "type": WsCommands.START
            }
            self.parrent.ws.sendMessage(msgObj)
        elif(state == ProgramStates.Stoped):
            self.ui.startButton.setEnabled(True)
            self.ui.stopButton.setDisabled(True)
            self.ui.progressBarLabel.setText(StatesLabels.Stoped)
            msgObj = {
                "type": WsCommands.STOP
            }
            self.parrent.ws.sendMessage(msgObj)
        elif(state == ProgramStates.Completed):
            self.ui.startButton.setDisabled(True)
            self.ui.stopButton.setDisabled(True)
            self.ui.progressBarLabel.setText(StatesLabels.Completed)
        
    
    # сам UI из Qt Designera
    ui = RunningWindowUI()
    tableHeader = ["Название файла", "Статус", "Дополнительно"]

    # монтируем весь UI от Qt Designera
    def setupUi(self, MainWindow):
        self.ui.setupUi(MainWindow)

        # и сэтаем свою логику
        self.parrent = MainWindow

        self.ui.startButton.clicked.connect(lambda: self.setState(ProgramStates.Running))
        self.ui.stopButton.clicked.connect(lambda: self.setState(ProgramStates.Stoped))
        self.renderTable()

    def renderTable(self):
        self.ui.tableWidget.setRowCount(len(self.parrent.files))
        self.ui.tableWidget.setColumnCount(len(self.tableHeader))
        self.ui.tableWidget.setHorizontalHeaderLabels(self.tableHeader)
        header = self.ui.tableWidget.horizontalHeader() 
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        for i, file in enumerate(self.parrent.files):
            filename = QTableWidgetItem(file)
            status = QTableWidgetItem("В очереди")
            more = QTableWidgetItem("...")
            self.ui.tableWidget.setItem(i, 0, filename)
            self.ui.tableWidget.setItem(i, 1, status)
            self.ui.tableWidget.setItem(i, 2, more)


# логика
class BeginWindowLogic:
    # сам UI из Qt Designera
    ui = BeginWindowUI()

    # монтируем весь UI от Qt Designera
    def setupUi(self, MainWindow):
        self.ui.setupUi(MainWindow)

        # и сэтаем свою логику 
        # бахаем обработчики
        self.ui.path_browse_button.clicked.connect(self.selectPath)
        self.ui.start_recogntion.clicked.connect(self.beginWork)

        # вспоминаем прошлые настройки
        self.path = MainWindow.settings.value(MainWindow.SETTINGS_PATH, '', type=str)
        self.parrent = MainWindow
        self.validatePath(self.path)

    def selectPath(self):
        self.path = QFileDialog.getExistingDirectory(self.parrent, "Выбрать папку", "/")
        self.validatePath(self.path)
    
    def beginWork(self):
        typedPath = self.ui.path_browse_input.text()
        if(self.validatePath(typedPath)):
            self.startWork()

    def validatePath(self, typedPath:str):
        if (typedPath):
            if (path.isdir(typedPath)):
                # если все норм сохраняем настройки
                self.parrent.settings.setValue(self.parrent.SETTINGS_PATH, self.path)
                self.parrent.settings.sync()

                # сетаем текст в поле ввода
                # и прячем красный алерт
                self.ui.path_browse_input.setText(self.path)
                self.ui.error_path_alert.hide()

                # сетаем инфу о файлах в UI
                self.setFilesInfo()
                return True
            else:
                errText = 'Такой папки не существует*'
                self.ui.error_path_alert.setText(errText)
                self.ui.error_path_alert.show()
                self.showError(errText)
                self.ui.files_on_dir_value.setText('0')
                return False
        else:
            errText = 'Папка не выбрана*'
            self.ui.error_path_alert.setText(errText)
            self.ui.error_path_alert.show()
            self.showError(errText)
            self.ui.files_on_dir_value.setText('0')
            return False
    
    def setFilesInfo(self):
        allFiles = [f for f in listdir(self.path) if path.isfile(path.join(self.path, f))]
        self.parrent.files = []
        for file in allFiles:
            if(fnmatch(file, '*.jpeg') 
               or fnmatch(file, '*.jpg') 
               or fnmatch(file, '*.png') 
               or fnmatch(file, '*.pdf')):
                self.parrent.files.append(file)

        self.parrent.filesCount = len(self.parrent.files)
        self.ui.files_on_dir_value.setText(str(self.parrent.filesCount))

    def showError(self, text: str):
        QMessageBox.critical(None, text, text, QMessageBox.Ok)

    def startWork(self):
        self.parrent.ws.sendMessage({
            "type": WsCommands.CONNECT,
            "clientID": self.parrent.clientID
        })
        if self.parrent.ws.isConnected():
            self.parrent.navigateTo(Routes.Watching)
        else:
            self.showError('Сервер недоступен')
