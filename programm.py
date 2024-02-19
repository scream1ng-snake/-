from PyQt5.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget, QLabel, QPushButton, QHBoxLayout, QFileDialog

class MainWindow(QWidget):
    name = 'Станция распознования'
    dirPath = ''

    def getDirectory(self):
        self.dirPath = QFileDialog.getExistingDirectory(self,"Выбрать папку","/")
        self.pathInput.setText(self.dirPath)

    def showInput(self):
        pathInputLabel = QLabel('Выберите путь с файлами для распознавания', parent=self)

        self.pathInput = QLineEdit(parent=self)
        self.pathInput.setPlaceholderText('путь к папке')

        browseButton = QPushButton('Browse', parent=self)
        browseButton.clicked.connect(self.getDirectory)

        row = QHBoxLayout()
        row.addWidget(self.pathInput)
        row.addWidget(browseButton)

        column = QVBoxLayout()
        column.addWidget(pathInputLabel)
        column.addLayout(row)
        self.setLayout(column)
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle(self.name)
        self.resize(600, 300)
        self.showInput()
        

app = QApplication([])
window = MainWindow()
window.show()
app.exec()