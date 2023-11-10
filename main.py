import random
import sys
from PyQt5 import uic
import io
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QColor, QPainter
from math import sin, cos, pi


class  Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('01.ui', self)
        self.resize(1000, 1000)
        self.do_paint = False
        self.n = 1
        self.x = 0
        self.y = 0
        self.jmak.clicked.connect(self.krug)

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            if self.n == 1:
                self.krug()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def krug(self):
        color = QColor(55, 255, 0)
        size = random.randint(20, 100)
        self.qp.setBrush(color)
        self.qp.drawEllipse(int(self.x - size / 2), int(self.y - size / 2), size, size)
