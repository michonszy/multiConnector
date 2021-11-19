import PyQt5
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui,QtCore
from PyQt5.QtGui import QCursor
import getpass
import socket
from colorama import Fore, Back, Style
#define
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("MultiConnector")
window.move(500,200)
window.setFixedHeight(600)
window.setFixedWidth(1000)
window.setStyleSheet(
    "background-color: #202020;"
)
grid=QGridLayout()

#####make


#tabs on top
tabs = QTabWidget()
tab1 = QWidget()
layoutTab1 = QGridLayout()

tab1.setLayout(layoutTab1)

def addProjectTab(self):
    tab = QWidget()
    layoutTab = QGridLayout()
    tab.setLayout(layoutTab)
    groupBoxSftp = QGroupBox("Files")
    groupBoxSsh = QGroupBox("Commands")
    layoutTab.addWidget(groupBoxSftp,1,1)
    layoutTab.addWidget(groupBoxSsh,1,2,1,3)
    tabs.addTab(tab, "FQDN.pm.pl.xxxxpack.de")

btnAddTab = QPushButton()
btnAddTab.clicked.connect(addProjectTab)
btnAddTab.setText('New connection')

#tab1
groupBoxSftp = QGroupBox("Files")
groupBoxSftp.setFixedWidth(400)
sftplayout = QGridLayout()
groupBoxSftp.setLayout(sftplayout)
model = QFileSystemModel()
dir_path = "/"
model.setRootPath(dir_path)
tree =  QTreeView()
tree.setModel(model)

tree.setRootIndex(model.index(dir_path))
tree.setColumnWidth(0, 250)
tree.setAlternatingRowColors(True)
sftplayout.addWidget(tree,0,0)


groupBoxSsh = QGroupBox("Commands")
sshlayout = QGridLayout()
groupBoxSsh.setLayout(sshlayout)
username = getpass.getuser()
hostname = socket.gethostname()
txt = username+"@"+hostname+":"+""+"$"
cmdLine = QLineEdit(txt)
sshlayout.addWidget(cmdLine,1,1)

def on_line_edit1_returnPressed():
    print("Enter wcisniety")
cmdLine.returnPressed.connect(on_line_edit1_returnPressed)

layoutTab1.addWidget(groupBoxSftp,1,1)
layoutTab1.addWidget(groupBoxSsh,1,2)


tabs.addTab(tab1, "FQDN.pm.pl.xxxxpack.de")





grid.addWidget(tabs,1,0,1,1)
grid.addWidget(btnAddTab,0,0)
#execute
window.show()
window.setLayout(grid)
sys.exit(app.exec())