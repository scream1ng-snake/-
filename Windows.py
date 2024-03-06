from Routes import Routes
from RunningWindowUI import RunningWindowUI
from BeginWindowUI import BeginWindowUI
from PySide6.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem, QHeaderView
from os import path, listdir
from enum import Enum
from fnmatch import fnmatch
import os
import base64

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
    POST_FILES = "POST_FILES"

class FileStates():
    # файл ожиадет в очереди
    WAITING = 'WAITING'
    # файл полностью распознан
    RECOGNIZED = 'RECOGNIZED'
    # файл распозанется
    RECOGNIZING = 'RECOGNIZING'
    # файл на верификации
    ON_VERIFICATION = 'ON_VERIFICATION'
    # ошибка при распознавании
    FAILED = 'FAILED'

FileStatesPhrases = {
    # файл ожиадет в очереди
    FileStates.WAITING: "В очереди",
    # файл полностью распознан
    FileStates.RECOGNIZED: "Распознан",
    # файл распозанется
    FileStates.RECOGNIZING: "Распознается",
    # файл на верификации
    FileStates.ON_VERIFICATION: "Верификация",
    # ошибка при распознавании
    FileStates.FAILED: "Ошибка",
}

# логика
class RunningWindowLogic:
    state = ProgramStates.Initail

    filesTableModel = []


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
                "type": WsCommands.START,
                "clientID": self.parrent.clientID
            }
            self.parrent.ws.sendMessage(msgObj)
        elif(state == ProgramStates.Stoped):
            self.ui.startButton.setEnabled(True)
            self.ui.stopButton.setDisabled(True)
            self.ui.progressBarLabel.setText(StatesLabels.Stoped)
            msgObj = {
                "type": WsCommands.STOP,
                "clientID": self.parrent.clientID
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
        # подписали свой редюсер к экземпляру веб сокета
        self.parrent.ws.subscribeToMessage(self.onWsMessage)
        
        self.renderTable()

    def onWsMessage(self, msgObj):
        if msgObj["type"] == 'GET_FILES':
            # папка
            folder = self.parrent.settings.value(self.parrent.SETTINGS_PATH, '', type=str)
            # первые N файлов которые со статусом "В очереди"
            waitingFiles = []
            for fileRow in self.filesTableModel:
                if len(waitingFiles) < msgObj["count"]:
                    if fileRow[1] == FileStates.WAITING:
                        filename = fileRow[0]
                        fullpath = os.path.join(folder, filename).replace("\\","/")
                        print("reading - ", fullpath)
                        content = open(fullpath, mode="rb").read()
                        encoded_b64 = base64.b64encode(content)
                        waitingFiles.append({
                            "filename": filename,
                            "content": encoded_b64.decode('utf-8')
                        })
                        
                else:
                    break
            # затем эти файлы отправляем на сервер
            self.parrent.ws.sendMessage({
                "type": WsCommands.POST_FILES,
                "clientID": self.parrent.clientID,
                "files": waitingFiles
            })
                
        elif msgObj["type"] == 'SET_FILE_STATE':
            filename = msgObj["filename"]
            state = msgObj["state"]
            self.updateFileInTable(filename, state)

    def updateFileInTable(self, filename:str, state:str):
        results = [(i, fr) for i, fr in enumerate(self.filesTableModel) if fr[0] == filename]
        rowIndex = results[0][0]
        if rowIndex != None:
            self.filesTableModel[rowIndex] = [filename, state]
            self.renderTable()
            
            
    
    def renderTable(self):
        self.ui.tableWidget.setRowCount(len(self.parrent.files))
        self.ui.tableWidget.setColumnCount(len(self.tableHeader))
        self.ui.tableWidget.setHorizontalHeaderLabels(self.tableHeader)
        header = self.ui.tableWidget.horizontalHeader() 
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.Stretch)

        # если модель таблицы пустая
        if not len(self.filesTableModel):
            # то сначала собираем модель таблицы
            for i, file in enumerate(self.parrent.files):
                self.filesTableModel.append([file, FileStates.WAITING])
            
            # а уже потом саму таблицу обновляем по модели
            for i, fileRow in enumerate(self.filesTableModel):
                filename = QTableWidgetItem(fileRow[0])
                status = QTableWidgetItem(FileStatesPhrases[fileRow[1]])
                more = QTableWidgetItem("...")
                self.ui.tableWidget.setItem(i, 0, filename)
                self.ui.tableWidget.setItem(i, 1, status)
                self.ui.tableWidget.setItem(i, 2, more)

        else:
            for i, fileRow in enumerate(self.filesTableModel):
                filename = QTableWidgetItem(fileRow[0])
                status = QTableWidgetItem(FileStatesPhrases[fileRow[1]])
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
