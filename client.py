import socket
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

message = ''
serv=''

class Client:
    def __init__(self, host, port):
        self.__port = port
        self.__host = host
        self.__message = ''
        self.socket = socket.socket()



    def envoie(self, message):
            self.socket.send(message.encode())


    def reception(self, conn):
        while True:
            serv = conn.recv(1024).decode()
            print(serv)


    def host(self, host):
        self.__host = host

    def port(self, port):
        self.__port = port


    def Connect(self):
        self.socket.connect((self.__host, self.__port))



class GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.cmd = ''
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)

        self.__IP = QLabel("Serveur")
        self.__PORT = QLabel("Port")
        self.__CONNECTION = QPushButton("Connexion")
        self.__IP_EDIT = QLineEdit("localhost")
        self.__PORT_EDIT = QLineEdit("10000")
        self.__SOCKET = socket.socket()
        self.__TB = QTextBrowser()
        self.__client = Client(self.__IP, self.__PORT)
        self.__TB.setAcceptRichText(True)
        self.__MESSAGE_LABEL = QLabel("Message : ")
        self.__MESSAGE_EDIT = QLineEdit("")
        self.__ENVOYER = QPushButton("Envoyer")
        self.__EFFACER = QPushButton("Effacer")
        self.__QUITTER = QPushButton("Quitter")
        self.__ESPACE = QLabel("")

        grid.addWidget(self.__IP, 0, 0)
        grid.addWidget(self.__PORT, 1, 0)
        grid.addWidget(self.__IP_EDIT, 0, 1, 1,2)
        grid.addWidget(self.__PORT_EDIT, 1, 1, 1,2)
        grid.addWidget(self.__CONNECTION, 2, 0, 1,3)
        grid.addWidget(self.__TB, 3, 0, 1, 3)
        grid.addWidget(self.__MESSAGE_LABEL, 4, 0)
        grid.addWidget(self.__MESSAGE_EDIT, 4, 1, 1,2)
        grid.addWidget(self.__ENVOYER, 5, 0, 1,3)
        grid.addWidget(self.__ESPACE, 6, 0)
        grid.addWidget(self.__EFFACER, 7, 0)
        grid.addWidget(self.__QUITTER, 7, 2, 1,1)

        self.__CONNECTION.clicked.connect(self._connexion)
        self.__ENVOYER.clicked.connect(self._envoie)
        self.__QUITTER.clicked.connect(self._quitter)
        self.__EFFACER.clicked.connect(self._clear)

        self.setWindowTitle("Un logiciel de tchat")

    def _connexion(self):
        host = str( self.__IP_EDIT.text())
        port = int(self.__PORT_EDIT.text())
        self.__SOCKET = Client(host, port)
        self.__SOCKET.Connect()
        self.__CONNECTION.setText("Deconnexion")


    def _reception(self):
        data = self.__SOCKET.recv(1024).decode()
        self.__TB.append(data)


    def _envoie(self):
        msg = self.__MESSAGE_EDIT.text()
        self.__TB.append(msg)


    def _quitter(self):
        QCoreApplication.instance().quit()
        data = 'deco-server'
        self.__TB.append(data)


    def _clear(self):
        self.__TB.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    app.exec()
