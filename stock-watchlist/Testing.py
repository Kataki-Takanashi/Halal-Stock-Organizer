from tkinter.tix import Form

# import MyGUI as MyGUI
#import self as self
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

# print(MyGUI.clicked1)
# num = MyGUI.clicked1()
# print(num)
# if num == 1:
#     button1 = True
# elif num == 2:
#     button2 = True
# elif num == 3:
#     button3 = True
# elif num == 4:
#     button4 = True
# elif num == 5:
#     button5 = True
# elif num == 6:
#     button6 = True
# else: print("Error: not an option1.1")


# variables
# if
# Button1 =
# Functions

def main():
    app = QApplication([])
    window = MyGUI()
    # form = Form()
    # form.setupUi(window)

    # window.setGeometry(100, 100, 200, 300)
    # window.setWindowTitle("Stock Watchlist & Logger")
    #
    # # label = QLabel(window)
    # # label.setText("Press button for a suprise!")
    # #
    # # label.setText("Hoi Kataki")
    # # label.setFont(QFont("Arial", 16))
    # # label.move(50, 100)
    #
    # layout = QVBoxLayout()
    # label = QLabel("Press button for a suprise!")
    # textbox = QTextEdit()
    #
    # label.setFont(QFont("Arial", 16))
    # label.move(50, 100)
    # button = QPushButton("Press me for a suprise!")
    # button.clicked.connect(lambda: on_clicked(textbox.toPlainText()))
    # layout.addWidget(label)
    # layout.addWidget(textbox)
    # layout.addWidget(button)
    #
    # window.setLayout(layout)


    window.show()
    app.exec_()




def on_clicked(msg):
    print("Button Clicked!!!")
    message = QMessageBox()
    message.setText(msg)
    message.exec_()


if __name__ == '__main__':
    # # num = MyGUI.clicked1(MyGUI)
    # while MyGUI.button1 != True:

    main()


