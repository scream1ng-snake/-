import uuid
from PySide6 import QtCore
from PySide6.QtWebSockets import QWebSocketProtocol, QWebSocket
from PySide6.QtCore import QUrl
from PySide6.QtNetwork import QAbstractSocket
from json import dumps


def isUUID(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False



class WsClient(QtCore.QObject):
    client = None
    def __init__(self, parent, host:str):
        super().__init__(parent)
        self.host = host

    def connect(self, onReject):
        try:
            if not self.client:
                def on_error(error_code):
                    onReject()
                    self.error(error_code)

                self.client = QWebSocket("", QWebSocketProtocol.Version13, None)
                self.client.error.connect(on_error)
                self.client.pong.connect(self.onPong)
                self.client.connected.connect(self.onConnected)
                self.client.disconnected.connect(lambda: print('disconnected'))
                self.client.textMessageReceived.connect(lambda msg: print(msg))
                self.client.open(QUrl(self.host))
            
        except Exception as e:
            print(e)
            print('qqqqqqqqqqq')

    def sendMessage(self, obj):
        print("client: send_message")
        self.client.sendTextMessage(dumps(obj))

    def onPong(self, elapsedTime, payload):
        print(payload)


    def error(self, error_code):
        print('Somthing wents wrong')
        print("error code: {}".format(error_code))
        print(self.client.errorString())

    def close(self):
        self.client.close()

    def onConnected(self):
        print('connected')

    def isConnected(self):
        return self.client.state() == QAbstractSocket.SocketState.ConnectedState