from tkinter.tix import Form

# import MyGUI as MyGUI
import self as self
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication


# Form, Window = uic.loadUiType("Stock-Watchlist-Logger.ui")

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("Stock-Watchlist-Logger.ui", self)
        self.show()

        self.Button1.clicked.connect(self.clicked1)
        print(self)
        # button1 = self.Button1.clicked.connect(self.clicked)
        # button2 =\
        self.Button2.clicked.connect(self.clicked2)
        # button3 =\
        self.Button3.clicked.connect(self.clicked3)
        # button4 =\
        self.Button4.clicked.connect(self.clicked4)
        # button5 = \
        self.Button5.clicked.connect(self.clicked5)
        # button6 =\
        self.Button6.clicked.connect(self.clicked6)
        self.YesButton.clicked.connect(self.clickedyes)
        self.NoButton.clicked.connect(self.clickedno)



    button1 = False
    button2 = False
    button3 = False
    button4 = False
    button5 = False
    button6 = False
    yesbutton = False
    nobutton = False

    def clicked1(self):
        MyGUI.button1 = True
        print(MyGUI.button1)
        # return button1
    def clicked2(self):
        button2 = True
        return button2
    def clicked3(self):
        button3 = True
        return button3
    def clicked4(self):
        button4 = True
        return button4
    def clicked5(self):
        button5 = True
        return button5
    def clicked6(self):
        button6 = True
        return button6
    def clickedyes(self):
        yesbutton = True
        return yesbutton
    def clickedno(self):
        nobutton = True
        return nobutton
    print(button1)

# what is the ticker
def q1():
    pass

def main():
    app = QApplication([])
    window = MyGUI()

    window.show()
    app.exec_()




def on_clicked(msg):
    print("Button Clicked!!!")
    message = QMessageBox()
    message.setText(msg)
    message.exec_()


if __name__ == '__main__':
    main()