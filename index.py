from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
ui,_ = loadUiType('untitled.ui')
class MainApp(QMainWindow , ui):
    num = []
    op = []
    def __init__(self , parent=None):
        super(MainApp , self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("calc")
        self.B()
    def B(self):
        self.pushButton0.clicked.connect(self.opp0)
        self.pushButton1.clicked.connect(self.opp1)
        self.pushButton2.clicked.connect(self.opp2)
        self.pushButton3.clicked.connect(self.opp3)
        self.pushButton4.clicked.connect(self.opp4)
        self.pushButton5.clicked.connect(self.opp5)
        self.pushButton6.clicked.connect(self.opp6)
        self.pushButton7.clicked.connect(self.opp7)
        self.pushButton8.clicked.connect(self.opp8)
        self.pushButton9.clicked.connect(self.opp9)
        self.pushButton.clicked.connect(self.oop_dot)
        self.pushButton_4.clicked.connect(self.oop_equal)
        self.pushButton_3.clicked.connect(self.oop_division)
        self.pushButton_7.clicked.connect(self.oop_multi)
        self.pushButton_11.clicked.connect(self.oop_munis)
        self.pushButton_15.clicked.connect(self.oop_plus)
        self.pushButton_16.clicked.connect(self.oop_clear)
    def opp1(self):
        a1=int(self.pushButton1.text())
        self.lineEdit.setText(self.lineEdit.text()+str(a1))
    def opp2(self):
        a2=int(self.pushButton2.text())
        self.lineEdit.setText(self.lineEdit.text()+str(a2))
    def opp3(self):
        a3=int(self.pushButton3.text())
        self.lineEdit.setText(self.lineEdit.text()+str(a3))
    def opp4(self):
        a4=int(self.pushButton4.text())
        self.lineEdit.setText(self.lineEdit.text()+str(a4))
    def opp5(self):
        a5=int(self.pushButton5.text())
        self.lineEdit.setText(self.lineEdit.text()+str(a5))
    def opp6(self):
        a6=int(self.pushButton6.text())
        self.lineEdit.setText(self.lineEdit.text()+str(a6))
    def opp7(self):
        a7=int(self.pushButton7.text())
        self.lineEdit.setText(self.lineEdit.text()+str(a7))
    def opp8(self):
        a8=int(self.pushButton8.text())
        self.lineEdit.setText(self.lineEdit.text()+str(a8))
    def opp9(self):
        a9=int(self.pushButton9.text())
        self.lineEdit.setText(self.lineEdit.text()+str(a9))
    def opp0(self):
        a0=int(self.pushButton0.text())
        self.lineEdit.setText(self.lineEdit.text()+str(a0))
    def oop_dot(self):
        dot=self.pushButton.text()
        self.lineEdit.setText(self.lineEdit.text() + dot)
    def oop_plus(self):
        plus = self.pushButton_15.text()
        self.lineEdit.setText(self.lineEdit.text()+" " + plus +" ")
    def oop_munis(self):
        munis = self.pushButton_11.text()
        self.lineEdit.setText(self.lineEdit.text()+" " +munis+" ")
    def oop_division(self):
        div = self.pushButton_3.text()
        self.lineEdit.setText(self.lineEdit.text()+" " + div+" ")
    def oop_multi(self):
        mult = self.pushButton_7.text()
        self.lineEdit.setText(self.lineEdit.text()+" " + mult+" ")
    def oop_equal(self):
        x=self.lineEdit.text()
        self.lineEdit.setText(self.calc(x))
    def calc(self,a):
        def ope(op, x, i):
            if op == "x":
                return int(x[i - 1]) * int(x[i + 1])
            elif op == "-":
                return int(x[i - 1]) - int(x[i + 1])
            elif op == "+":
                return int(x[i - 1]) + int(x[i + 1])
            elif op == "/":
                return int(x[i - 1]) / int(x[i + 1])
        y = a
        a = a.split()
        count = 0
        for i in a:
            if i.isnumeric() == True:
                continue
            else:
                count += 1
        while ("x" in a or "/" in a):
            for i in a:
                if i == "x":
                    d = ope(i, a, a.index(i))
                    h = a.index(i)
                    del a[h]
                    del a[h]
                    for i in range(len(a)):
                        if i == h - 1:
                            a[i] = d
                        else:
                            a[i] = a[i]
            for i in a:
                if i == "/":
                    d = ope(i, a, a.index(i))
                    h = a.index(i)
                    del a[h]
                    del a[h]
                    for i in range(len(a)):
                        if i == h - 1:
                            a[i] = d
                        else:
                            a[i] = a[i]
        while (len(a) >= 3):
            d = ope(a[1], a, 1)
            del a[0]
            del a[0]
            a[0] = d
        return str(a[0])
    def oop_clear(self):
        self.lineEdit.setText("")
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()