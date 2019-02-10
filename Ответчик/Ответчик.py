# -*- coding: utf-8 -*-

import re, sys
import urllib.request
from urllib import request
from urllib.parse import quote
import html2text
from poisk import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, QBasicTimer

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.mySearch)
    def mySearch(self):
        self.ui.textEdit.setText("")
        z = self.ui.lineEdit.text()
        s = 'http://go.mail.ru/search?fm=1&q='+quote(z)
        doc = urllib.request.urlopen(s).read().decode('cp1251',errors='ignore')

        o=re.compile('"url":"(.*?)"')
        l=o.findall(doc)
        sp=[]
        for x in l:
            if((x.rfind('youtube')==-1) and(x.rfind('yandex')==-1) and(x.rfind('mail.ru')==-1) and(x.rfind('.jpg')==-1) and(x.rfind('.png')==-1) and(x.rfind('.gif')==-1)):
                sp.append(x)
        sp = dict(zip(sp, sp)).values()
        sp1=[]
        for s in sp:
            sp1.append(s)
        sp=sp1
        self.progresscount=int(100/len(sp))
        self.progresscount2=int(100/len(sp))
        self.texts=[]
        self.ui.progressBar.setValue(0)   
        for s in sp:
            try:
                self.ui.progressBar.setValue(self.progresscount2)
                self.progresscount2 = self.progresscount2 + self.progresscount
                doc = urllib.request.urlopen(s).read().decode('utf-8',errors='ignore')
                h = html2text.HTML2Text()
                h.ignore_links = True
                h.body_width = False
                h.ignore_images = True
                doc = h.handle(doc)
                summa=""
                ss=doc.split("\n")
                for xx in ss:
                    xx=xx.strip()
                    if((len(xx)>50) and (xx.startswith('&')==False) and (xx.startswith('Wikipedia®')==False) and (xx.startswith('>')==False) and (xx.startswith('1.')==False) and (xx.startswith('2.')==False) and (xx.startswith('3.')==False) and (xx.startswith('4.')==False) and (xx.startswith('5.')==False) and (xx.startswith('6.')==False) and (xx.startswith('7.')==False) and (xx.startswith('7.')==False) and (xx.startswith('8.')==False) and (xx.startswith('9.')==False) and (xx.startswith('10.')==False) and (xx.startswith('*')==False) and (xx.startswith('\\')==False)and (xx.startswith('Текущая версия страницы')==False) and (xx.startswith('<')==False) and (xx.startswith('(')==False) and (xx.startswith('#')==False) and (xx.endswith('.') or xx.endswith('?') or xx.endswith('!') or xx.endswith(';'))):
                        summa = summa + xx + "\n \n"
                if(len(summa)>100):
                    self.texts.append(summa)
            except Exception:
                pass
        self.flagok=0
        self.maxflagok=len(self.texts)
        self.ui.textEdit.setText(self.texts[0])
        self.ui.progressBar.setValue(100)
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
