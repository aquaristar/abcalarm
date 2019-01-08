import sys, os, subprocess, signal
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QSystemTrayIcon, \
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp, QTableWidget, QTableWidgetItem, QMessageBox, \
    QTableView, QWidget, QPushButton, QVBoxLayout
from PyQt5 import Qt, QtCore, QtGui, QtWidgets, QtSql
import webbrowser
import qdarkgraystyle

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 320)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("alarm.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        #self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        #self.horizontalLayout.setObjectName("horizontalLayout")

        self.Text = QtWidgets.QLabel(self.centralwidget)
        self.Text.setObjectName("Text")
        self.gridLayout.addWidget(self.Text, 1, 0, 1, 1)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.qtable = QtWidgets.QTableView(self.centralwidget)
        self.qtable.setObjectName("qtable")
        self.qtable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        header = self.qtable.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.gridLayout.addWidget(self.qtable, 3, 0, 1, 2)

        self.ButtonRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonRefresh.setObjectName("ButtonRefresh")
        self.gridLayout.addWidget(self.ButtonRefresh, 4, 0, 1, 1)

        self.ButtonRemove = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonRemove.setObjectName("ButtonRemove")
        self.gridLayout.addWidget(self.ButtonRemove, 4, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)
        #self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 387, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ABCAlarm Main Menu"))
        self.Text.setText(
            _translate("MainWindow", "Welcome to the ABCWarehouse Alarm Software Version 1.5"))
        self.label.setText(_translate("MainWindow", "Copyright @ ABCWarehouse Dec, 2018"))

        self.ButtonRemove.setText(_translate("MainWindow", "Remove all alarms"))
        self.ButtonRefresh.setText(_translate("MainWindow", "Refresh"))


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('webapp/db.sqlite3')
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('abcalarm_alarm')
        self.model.select()
        #self.model = QtSql.QSqlQueryModel()
        #self.model.setQuery("select * from abcalarm_alarm")
        #self.model.query()
        print(self.model)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Title")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Content")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Date")

        self.ui.qtable.setModel(self.model)
        self.ui.qtable.setColumnHidden(4, True)
        self.ui.qtable.setColumnHidden(5, True)
        self.ui.qtable.setColumnHidden(6, True)
        self.ui.qtable.setColumnHidden(7, True)

        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)

        self.ui.ButtonRemove.clicked.connect(self.removeAllAlarms)
        self.ui.ButtonRefresh.clicked.connect(self.refresh)
        #self.ui.pushButton_3.clicked.connect(self.delrow)
        #self.i = self.model.rowCount()
        #self.ui.lcdNumber.display(self.i)
        #print(self.ui.tableWidget.currentIndex().row())

        #self.app_icon = "alarm.ico"
        #trayIcon = SystemTrayIcon(QtGui.QIcon(self.app_icon), self)
        #trayIcon.show()

    def refresh(self):
        self.model.select()

    def removeAllAlarms(self):
        query = QtSql.QSqlQuery()
        query.exec_("DELETE FROM abcalarm_alarm")
        self.refresh()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        s = subprocess.check_output('tasklist', shell=True)
        print(s)
        if "webapp.exe" in str(s):
            print(s)
            subprocess.call("taskkill /f /IM webapp.exe")

        self.proc = subprocess.Popen(['dist/webapp/webapp', 'runserver', '0.0.0.0:8000'], stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        self.main = Main()
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtWidgets.QMenu(parent)
        openAlarmViewerAction = menu.addAction("View Alarms")
        openAlarmViewerAction.triggered.connect(self.openAlarmViewer)
        updateAction = menu.addAction("Update")
        updateAction.triggered.connect(self.updateAlarmClient)
        aboutAction = menu.addAction("About")
        aboutAction.triggered.connect(self.aboutApp)
        exitAction = menu.addAction("Exit")
        exitAction.triggered.connect(self.exitApp) #parent.close
        self.setContextMenu(menu)

    def openAlarmViewer(self):
        webbrowser.open('http://localhost:8000')

    def updateAlarmClient(self):
        print("update")
        self.showMessage(
            "Tray Program",
            "Application was minimized to Tray",
            QSystemTrayIcon.Information,
            2000
        )

    def exitApp(self):
        os.killpg(os.getpgid(self.proc.pid), signal.SIGTERM)
        QtCore.QCoreApplication.exit()

    def aboutApp(self):
        #main = Main()
        self.main.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkgraystyle.load_stylesheet())
    w = QtWidgets.QWidget()
    trayIcon = SystemTrayIcon(QtGui.QIcon("alarm.ico"), w)
    trayIcon.show()
    #main = Main()
    #main.show()
    #subprocess.call("taskkill /f /IM webapp.exe")
    sys.exit(app.exec_())