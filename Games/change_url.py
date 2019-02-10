# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QPushButton, QGridLayout,QMainWindow, QWidget
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QBasicTimer
import sys
from time import sleep
from os import system

class Work(QMainWindow):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.window = QWidget()
    self.alert = QLabel("Enter query", self)
    self.alert.move(100,0)
    self.value = QLineEdit('', self)
    self.value.move(100,30)
    self.save= QPushButton('Save', self)
    self.save.move(100,60)
    self.save.clicked.connect(self.hello)
    #self.result = QLabel('Результат: ', self)
    #self.help = QLabel('http:// или https://')
    #self.help.move(0,110)
    self.setGeometry(700,470,300,150)    
    self.show()
  
  def hello(self):
    variable = self.value.text()
    if 'http://' in variable or 'https://' in variable:
      self.value.setText(' ') 
      #self.result.setText('Результат: Успешно!', self)
      with open('Docs/file.txt', 'a') as f:
        f.write(variable)
        f.write('\n')
      system('sudo python3 Docs/code.py')
          
    else:
        #self.result.setText('Результат: Ссылка не подходит :(')
        sleep(0.5)
        exit()

app = QApplication(sys.argv)
work = Work()
app.exec_()
