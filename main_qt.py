import sys
from ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableView
from PyQt5 import QtSql
from PyQt5 import QtCore
import qdarkgraystyle

class form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('webapp/db.sqlite3')
        self.model = QtSql.QSqlTableModel()
        self.model.setTable('abcalarm_alarm')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal,"id")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal,"title")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "message")
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, "status")
        self.model.setHeaderData(4, QtCore.Qt.Horizontal,"created_date")
        self.ui.tableWidget.setModel(self.model)
        #self.ui.pushButton.clicked.connect(self.addToDb)
        self.show()
        #self.ui.pushButton_2.clicked.connect(self.updaterow)
        #self.ui.pushButton_3.clicked.connect(self.delrow)
        #self.i = self.model.rowCount()
        #self.ui.lcdNumber.display(self.i)
        print(self.ui.tableWidget.currentIndex().row())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkgraystyle.load_stylesheet())
    frm = form()
    sys.exit(app.exec_())