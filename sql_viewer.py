#!/usr/bin/venv python

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)
import sys
from PyQt5.QtCore import pyqtSlot
from db import get_db


class SQLViewer(QDialog):
    def __init__(self, parent=None):
        super(SQLViewer, self).__init__(parent)
        self.create_container()

        main_layout = QGridLayout()
        main_layout.addWidget(self.container, 5, 1)
        main_layout.setRowStretch(5, 1)
        main_layout.setColumnStretch(1, 1)
        self.setLayout(main_layout)

        self.setWindowTitle("pysqlviewer")
    
    @pyqtSlot()
    def query_db(self):
        with get_db() as db:
            #results = db.execute('select * from test')
            #print([r for r in results])
            print(dir(self.container)) 
    def create_container(self):
        self.container = QTabWidget()
        self.container.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Ignored)

        tab1 = QWidget()
        tableWidget = QTableWidget(10, 10)

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)        
        tab1.setLayout(tab1hbox)
        
        tab2 = QWidget()
        textEdit = QTextEdit()

        textEdit.setPlainText("Enter SQL here: ")

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        bb = QPushButton('Send query!')
        
        bb.clicked.connect(self.query_db)


        tab2hbox.addWidget(bb)
        tab2.setLayout(tab2hbox)

        self.container.addTab(tab2, "Enter query")
        self.container.addTab(tab1, "Query results")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gallery = SQLViewer()
    gallery.show()
    sys.exit(app.exec_()) 
