import sys, os, subprocess, signal
from fbs import path, SETTINGS
from fbs_runtime import platform
from fbs_runtime.application_context import ApplicationContext, cached_property
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLabel, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import webbrowser
import qdarkgraystyle
import socket
from threading import Thread
from socketserver import ThreadingMixIn


class ServerThread(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.window = window

    def run(self):
        TCP_IP = '0.0.0.0'
        TCP_PORT = 7000
        BUFFER_SIZE = 20
        tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpServer.bind((TCP_IP, TCP_PORT))
        threads = []

        tcpServer.listen(4)
        while True:
            print("Multithreaded Python server : Waiting for connections from TCP clients...")
            global conn
            (conn, (ip, port)) = tcpServer.accept()
            newthread = ClientThread(ip, port, window)
            newthread.start()
            threads.append(newthread)

        for t in threads:
            t.join()


class ClientThread(Thread):

    def __init__(self, ip, port, window):
        Thread.__init__(self)
        self.window = window
        self.ip = ip
        self.port = port
        print("[+] New server socket thread started for " + ip + ":" + str(port))

    def run(self):
        while True:
            # (conn, (self.ip,self.port)) = serverThread.tcpServer.accept()
            global conn
            data = conn.recv(2048)
            window.chat.append(data.decode("utf-8"))
            print(data)

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtWidgets.QMenu(parent)
        openAlarmViewerAction = menu.addAction("Open AlarmViewer")
        openAlarmViewerAction.triggered.connect(self.openAlarmViewer)
        updateAction = menu.addAction("Update")
        updateAction.triggered.connect(self.updateAlarmClient)
        exitAction = menu.addAction("Exit")
        exitAction.triggered.connect(parent.close)
        self.setContextMenu(menu)

    def openAlarmViewer(self):
        webbrowser.open('http://localhost:%s' % self.public_settings['webapp_port'])

    def updateAlarmClient(self):
        print("update")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        text = QLabel()
        text.setWordWrap(True)
        button = QPushButton('Next quote >')
        button.clicked.connect(lambda: text.setText(_get_quote()))
        layout = QVBoxLayout()
        layout.addWidget(text)
        layout.addWidget(button)
        layout.setAlignment(button, Qt.AlignHCenter)
        self.setLayout(layout)

class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext

    def run(self):
        print(self.public_settings['main_module'])
        print(self.public_settings['webapp_port'])
        if(platform.is_windows()):
            self.proc = subprocess.Popen(['webapp/webapp', 'runserver', '0.0.0.0:%s' % self.public_settings['webapp_port']],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)

        #window = QMainWindow()
        #window.setWindowTitle("pyqtalarm")
        #window.resize(250, 150)
        stylesheet = self.get_resource('styles.qss')
        dark_stylesheet = qdarkgraystyle.load_stylesheet()
        self.app.setStyleSheet(dark_stylesheet)
        #self.app.setStyleSheet(open(stylesheet).read())
        self.window.resize(250, 150)
        self.window.show()
        trayIcon = SystemTrayIcon(QtGui.QIcon(self.app_icon), self.window)
        trayIcon.show()
        #serverThread = ServerThread(window)
        #serverThread.start()
        return self.app.exec_()                 # 3. End run() with this line

    @cached_property
    def window(self):
        return MainWindow()

if __name__ == '__main__':
    subprocess.call("taskkill /f /IM webapp.exe")
    #exit()
    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run()                   # 5. Invoke run()
    appctxt.proc.terminate()
    sys.exit(exit_code)