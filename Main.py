#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys 
import random
import time
import os

import webbrowser

import pygame


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout,QMainWindow
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QBasicTimer
from sys import stdin, exit as sys_exit

class Change(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.fon = QPushButton('', self)
		self.fon.setIcon(QIcon('Фон.jpg'))
		self.fon.setGeometry(0,0,1366,768)
		self.fon.setIconSize(QSize(1366,768))
		
		self.time = QPushButton('', self)
		self.time.setIcon(QIcon("pan.png"))
		# self.time.setFlat(True)
		self.time.setGeometry(0, 0, 1366, 30)
		self.time.setIconSize(QSize(1366, 30))

#Фон -------------------------------------------------------        

		self.Big = QWidget()

#------------------------------------------------------------
		self.panel = QPushButton('', self.Big)
		self.panel.setIcon(QIcon("Фото/panel.png"))
		self.panel.setFlat(True)
		self.panel.setGeometry(0, 630, 1366, 150)
		self.panel.setIconSize(QSize(1366, 150))



		self.button_telegram = QPushButton('', self.Big)
		self.button_telegram.setIcon(QIcon("Фото/muzic.png"))
		self.button_telegram.setFlat(True)
		self.button_telegram.setGeometry(400, 650, 150, 100)
		self.button_telegram.setIconSize(QSize(150, 100))
		self.button_telegram.clicked.connect(self.muzic)



		self.button_youtube = QPushButton('', self.Big)
		self.button_youtube.setIcon(QIcon("Фото/youtube.png"))
		self.button_youtube.setFlat(True)
		self.button_youtube.setGeometry(600, 650, 150, 100)
		self.button_youtube.setIconSize(QSize(150, 100))
		self.button_youtube.clicked.connect(self.youtube)


		self.button_panel4 = QPushButton('', self.Big)
		self.button_panel4.setIcon(QIcon("Фото/telegram.png"))
		self.button_panel4.setFlat(True)
		self.button_panel4.setGeometry(800, 650, 150, 100)
		self.button_panel4.setIconSize(QSize(150, 100))
		self.button_panel4.clicked.connect(self.telegram)


		self.button_panel1 = QPushButton('', self.Big)
		self.button_panel1.setIcon(QIcon("Фото/полоска.png"))
		self.button_panel1.setFlat(True)
		self.button_panel1.setGeometry(-50, 650, 400, 100)
		self.button_panel1.setIconSize(QSize(400, 100))
		
		self.button_panel4 = QPushButton('', self.Big)
		self.button_panel4.setIcon(QIcon("Фото/полоска2.png"))
		self.button_panel4.setFlat(True)
		self.button_panel4.setGeometry(1000, 650, 400, 100)
		self.button_panel4.setIconSize(QSize(400, 100))

#--------------------------------------------------------------

#------------------------------------------------------------
		self.button_abc = QPushButton('', self.Big)
		self.button_abc.setIcon(QIcon("Фото/abc.png"))
		self.button_abc.setFlat(True)
		self.button_abc.setGeometry(610, 80, 180, 180)
		self.button_abc.setIconSize(QSize(180, 180))
		self.button_abc.clicked.connect(self.azbuca)

		self.button_films = QPushButton('', self.Big)
		self.button_films.setIcon(QIcon("Фото/films.png"))
		self.button_films.setFlat(True)
		self.button_films.setGeometry(525, 225, 180, 180)
		self.button_films.setIconSize(QSize(180, 180))
		self.button_films.clicked.connect(self.films)

		self.button_tetris = QPushButton('', self.Big)
		self.button_tetris.setIcon(QIcon("Фото/tetr.png"))
		self.button_tetris.setFlat(True)
		self.button_tetris.setGeometry(445, 375, 180, 180)
		self.button_tetris.setIconSize(QSize(180, 180))
		self.button_tetris.clicked.connect(self.tetris)

		self.buttont_zmeyka = QPushButton('', self.Big)
		self.buttont_zmeyka.setIcon(QIcon("Фото/zmeyka.png"))
		self.buttont_zmeyka.setFlat(True)
		self.buttont_zmeyka.setGeometry(445, 80, 180, 180)
		self.buttont_zmeyka.setIconSize(QSize(180, 180))
		self.buttont_zmeyka.clicked.connect(self.zmeyka)

		self.button_car = QPushButton('', self.Big)
		self.button_car.setIcon(QIcon("Фото/Car_game.png"))
		self.button_car.setFlat(True)
		self.button_car.setGeometry(360, 225, 180, 180)
		self.button_car.setIconSize(QSize(180, 180))
		self.button_car.clicked.connect(self.Car)



		self.button_karusel = QPushButton('', self.Big)
		self.button_karusel.setIcon(QIcon("Фото/plus.png"))
		self.button_karusel.setFlat(True)
		self.button_karusel.setGeometry(270, 375, 180, 180)
		self.button_karusel.setIconSize(QSize(180, 180))
		self.button_karusel.clicked.connect(self.add_value_1)


		self.button_disney = QPushButton('', self.Big)
		self.button_disney.setIcon(QIcon("Фото/plus.png"))
		self.button_disney.setFlat(True)
		self.button_disney.setGeometry(270, 80, 180, 180)
		self.button_disney.setIconSize(QSize(180, 180))
		self.button_disney.clicked.connect(self.add_value_2)
		

		self.button_mul = QPushButton('', self.Big)
		self.button_mul.setIcon(QIcon("Фото/plus.png"))
		self.button_mul.setFlat(True)
		self.button_mul.setGeometry(100, 80, 180, 180)
		self.button_mul.setIconSize(QSize(180, 180))
		self.button_mul.clicked.connect(self.add_value_3)

		self.button_nicilodium = QPushButton('', self.Big)
		self.button_nicilodium.setIcon(QIcon("Фото/plus.png"))
		self.button_nicilodium.setFlat(True)
		self.button_nicilodium.setGeometry(190, 225, 180, 180)
		self.button_nicilodium.setIconSize(QSize(180, 180))
		self.button_nicilodium.clicked.connect(self.add_value_4)



		self.buttont_otvet = QPushButton('', self.Big)
		self.buttont_otvet.setIcon(QIcon("Фото/ответчик.png"))
		self.buttont_otvet.setGeometry(695, 225, 180, 180)
		self.buttont_otvet.setFlat(True)
		self.buttont_otvet.setIconSize(QSize(180, 180))
		self.buttont_otvet.clicked.connect(self.Otvethic)


		self.button_calculator = QPushButton('', self.Big)
		self.button_calculator.setIcon(QIcon("Фото/calcutor.png"))
		self.button_calculator.setFlat(True)
		self.button_calculator.setGeometry(615, 370, 180, 180)
		self.button_calculator.setIconSize(QSize(180, 180))
		self.button_calculator.clicked.connect(self.calcutor)


		self.Button_gtz = QPushButton('', self.Big)
		self.Button_gtz.setIcon(QIcon("Фото/gdz.png"))
		self.Button_gtz.setFlat(True)
		self.Button_gtz.setGeometry(780, 80, 180, 180)
		self.Button_gtz.setIconSize(QSize(180, 180))
		self.Button_gtz.clicked.connect(self.gdz)



		self.button_paint = QPushButton('', self.Big)
		self.button_paint.setIcon(QIcon("Фото/paint.png"))
		self.button_paint.setFlat(True)
		self.button_paint.setGeometry(780, 370, 180, 180)
		self.button_paint.setIconSize(QSize(180, 180))
		self.button_paint.clicked.connect(self.paint)

		self.Button_sms = QPushButton('', self.Big)
		self.Button_sms.setIcon(QIcon("Фото/sms.png"))
		self.Button_sms.setFlat(True)
		self.Button_sms.setGeometry(865, 225, 180, 180)
		self.Button_sms.setIconSize(QSize(180, 180))
		self.Button_sms.clicked.connect(self.ally)

		self.button_calculator = QPushButton('', self.Big)
		self.button_calculator.setIcon(QIcon("Фото/on.png"))
		self.button_calculator.setFlat(True)
		self.button_calculator.setGeometry(950, 80, 180, 180)
		self.button_calculator.setIconSize(QSize(180, 180))
		self.button_calculator.clicked.connect(self.parser)



		self.button_a = QPushButton('', self.Big)
		self.button_a.setIcon(QIcon("Фото/off.png"))
		self.button_a.setFlat(True)
		self.button_a.setGeometry(950, 367, 180, 180)
		self.button_a.setIconSize(QSize(180, 180))
		self.button_a.clicked.connect(self.muzic_off)


		self.button_game = QPushButton('', self.Big)
		self.button_game.setIcon(QIcon("Фото/tool.png"))
		self.button_game.setFlat(True)
		self.button_game.setGeometry(1035, 225, 180, 180)
		self.button_game.setIconSize(QSize(160, 160))
		self.button_game.clicked.connect(self.settings)


		self.button_exit = QPushButton('', self.Big)
		self.button_exit.setIcon(QIcon("Фото/exit.png"))
		self.button_exit.setFlat(True)
		self.button_exit.setGeometry(1120, 80, 180, 180)
		self.button_exit.setIconSize(QSize(180, 180))
		self.button_exit.clicked.connect(self.exit)


		

		self.setCentralWidget(self.Big)
#Фон---------------------------------------------------------

		self.setGeometry(0,0, 1366, 768)
		self.setWindowTitle('SPLAYPER')
		self.show()

	def ally(self):
		os.system('sudo python3 Games/ally.py') 

	def muzic_off(self):
		os.system('sudo amixer set Master 0%')

	def settings(self):
		with open('Docs/file.txt', 'w') as f:
			f.write('')

	def zmeyka(self):
		os.system('python3 Games/Змейка.py')

	def tetris(self):
		os.system('python3 Games/Тетрис.py')

	def Otvethic(self):
		os.system('python3 Ответчик/Ответчик.py')

	def films(self):
		os.system('python3 Guess/films.py')

	def calcutor(self):
		os.system('python3 Канкулятор/calkulator.py')

	def paint(self):
		os.system('python3 Paint/pain.py')

	def muzic(self):
		webbrowser.open_new("https://www.music.yandex.ru/")
  
	def azbuca(self):
		os.system('python3 alpha/alpha.py')    

	def youtube(self):
		webbrowser.open_new("https://www.youtube.com/")

	def telegram(self):
		webbrowser.open_new("https://web.telegram.org/")

	def nicelodium(self):
		webbrowser.open_new("http://only-tv.org/nickelodeon.html")

	def parser(self):
		os.system('sudo python3 Games/parser.py')
  
	def gdz(self):
		os.system('xdg-open /home/starrk/coding/Project/page_another/index.html')              
				
	def nazad2(self):
		os.system('python3 main.py')
		sys_exit()  

	def Car(self):
		os.system('python3 Games/game.py')       
   
	def add_value_1(self):
		self.check(0)
	def add_value_2(self):
		self.check(1)
		#os.system('python3 Games/change_url.py')
	def add_value_3(self):
		self.check(2)
		# os.system('python3 Games/change_url.py')
	def add_value_4(self):
		self.check(3)

	def check(self, value):
		with open('Docs/file.txt', 'r') as f:
			variable = f.read().splitlines()
			if len(variable) == 4:#> 0 and len(variable) < 4:
				webbrowser.open_new(variable[value])
			
			else:
				os.system('python3 Games/change_url.py')

	def exit(self):
		sys_exit()
		

app = QApplication(sys.argv)
my_window = Change()
my_window.showFullScreen()
app.exec_() 
