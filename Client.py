import socket
import time
import clientui
import PyQt6
from PyQt6 import QtCore, QtGui, QtWidgets

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
class Messenger(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sendButton.pressed.connect(self.send_message)

    def send_message(self):
        while True:
            self.chatBrowser.append('Try connect to the server...')
            try:
                client.connect(('localhost', 5000))
                print('Connected')
                break
            except:
                self.chatBrowser.append('Disconected')
                time.sleep(2)
        nickName = 'User'
        if len(self.nickNameLineEdit.text()) > 0:
            nickName = self.nickNameLineEdit.text()

        #if len(self.inputEditor.toPlainText()) > 0:
           
            
    ''' def connect(self):
        while True:
            self.clientui.Ui_MainWindow.setupUi.chatBrowser.append('Try connect to the server...')
            try:
                client.connect(('localhost', 5000))
                print('Connected')
                break
            except:
                print('Disconected')
                time.sleep(2)'''

app = QtWidgets.QApplication([])
window = Messenger()
window.show()
app.exec()

'''class Messenger(QtWidgets.QMainWindow, clientui.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.clientui(self)

    def connect(self):
        while True:
            self.clientui.Ui_MainWindow.setupUi.chatBrowser.append('Try connect to the server...')
            try:
                client.connect(('localhost', 5000))
                print('Connected')
                break
            except:
                print('Disconected')
                time.sleep(2)

    while True:
        try:
            client.send(input().encode('utf-8'))
        except:
            connect()'''

