import uuid
from PySide6 import QtCore
from PySide6.QtWebSockets import QWebSocketProtocol, QWebSocket
from PySide6.QtCore import QUrl
from PySide6.QtNetwork import QAbstractSocket
from json import dumps, loads


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
                self.client.textMessageReceived.connect(self.onMessage)
                self.client.open(QUrl(self.host))
            
        except Exception as e:
            print(e)
            print('qqqqqqqqqqq')

    def sendMessage(self, obj):
        # print("[client]: send_message - ", dumps(obj))
        self.client.sendTextMessage(dumps(obj))

    def onPong(self, elapsedTime, payload):
        print(payload)


    def error(self, error_code):
        print("[client]: error_code: {}".format(error_code))
        print("[client]: error_text: ", self.client.errorString())

    def close(self):
        print('[client]: closed')
        self.client.close()

    def onConnected(self):
        print('[client]: connected')


    # тут будут обработчики входящих сообщений
    subscriptions = []
    
    # с помощью этого метода мы добавляем свой редюсер 
    # в массив обработчиков сообщений
    def subscribeToMessage(self, handler):
        if handler in self.subscriptions:
            pass
        else:
            self.subscriptions.append(handler)
    
    def onMessage(self, msg: str):
        print('[client]: recieve_message - ', msg)
        msgObj = loads(msg)
        # а тут мы проходим циклом по всем редюсерам
        for subscription in self.subscriptions:
            subscription(msgObj)

    def isConnected(self):
        return self.client.state() == QAbstractSocket.SocketState.ConnectedState