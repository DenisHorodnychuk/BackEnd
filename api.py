from PyQt5.QtCore import Qt
from PyQt5.QtNetwork import QTcpServer, QHostAddress
from PyQt5.QtWidgets import QApplication
import sys

class MyServer(QTcpServer):
    def __init__(self):
        super().__init__()

    def incomingConnection(self, socket_descriptor):
        socket = self.nextPendingConnection()
        socket.write(b'HTTP/1.1 200 OK\r\n')
        socket.write(b'Content-Type: text/html\r\n')
        socket.write(b'\r\n')
        socket.write(b'<!DOCTYPE html><html><body><h1>Empty API</h1></body></html>')
        socket.disconnectFromHost()

def main():
    app = QApplication(sys.argv)
    server = MyServer()

    if not server.listen(QHostAddress.Any, 8080):
        print('Could not start server.')
        return

    print('Server is running on port 8080...')
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
