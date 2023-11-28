import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from ui import Ui_Dialog
import random



class Example(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.do_paint = None
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        width = self.size().width()
        height = self.size().height()
        xrAngle = random.randint(0, width - 1)
        yrAngle = random.randint(0, height - 1)
        diam = random.randint(0, int(width + height / 2))
        colorC1, colorC2, colorC3 = random.randint(0, 255), random.randint(0, 255),random.randint(0, 255)
        if xrAngle + diam > width:
            diam = width - xrAngle
        if yrAngle + diam > height:
            diam = height - yrAngle
        # Нарисуйте цветной круг
        pen = QPen(QColor(colorC1, colorC2, colorC3), 2, Qt.SolidLine)
        qp.setPen(pen)
        qp.setBrush(QColor(colorC1, colorC2, colorC3))
        qp.drawEllipse(int(xrAngle), int(yrAngle), int(diam), int(diam))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
