from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout,QMainWindow
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QBasicTimer
import sys,os,subprocess

class Mypoweroff(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.window1 = QWidget()
		self.setGeometry(700,470,300,150)
		self.text = QLabel('Вы уверены?',self)
		self.text.move(100,0)
		self.yes = QPushButton('ДА', self)
		self.no = QPushButton('НЕТ',self)
		self.yes.setGeometry(20,70,120,70)
		self.no.setGeometry(160,70,120,70)
		self.yes.clicked.connect(self.powerofff)
		self.no.clicked.connect(self.exit)
		self.show()
	def powerofff(self):
		subprocess.call(["shutdown", "-f", "-s", "-t", "1"])
	def exit(self):
		exit()
app = QApplication(sys.argv)
my_window = Mypoweroff()
app.exec_()