# from PyQt5 import uic
# from PyQt5.QtWidgets import QApplication
#
# Form, Window = uic.loadUiType("Stock-Watchlist-Logger.ui")
#
# app = QApplication([])
# window = Window()
# form = Form()
# form.setupUi(window)
# window.show()
# app.exec()

# Imports
# import tkinter as tk
#
#
# window = tk.Tk()
#
# window.geometry("500x500")
# window.title("Stock Watchlist & Logger")
#
# label = tk.Label(window, text="Tester", font=('Ariel', 18))
# label.pack(padx=20, pady=20)
#
#
# textbox = tk.Text(window, height=3, font=('Ariel', 16))
# textbox.pack(padx=10, pady=10)
#
# numbuttframe = tk.Frame(window)
# numbuttframe.columnconfigure(0, weight=1)
#
# yesnobuttframe = tk.Frame(window)
# yesnobuttframe.columnconfigure(1, weight=1)
#
# button1 = tk.Button(numbuttframe, text="1", font=('Arial', 18))
# button1.grid(row=0, column=0, sticky=tk.W+tk.E)
#
# button2 = tk.Button(numbuttframe, text="2", font=('Arial', 18))
# button2.grid(row=0, column=1, sticky=tk.W+tk.E)
#
# button3 = tk.Button(numbuttframe, text="3", font=('Arial', 18))
# button3.grid(row=0, column=2, sticky=tk.W+tk.E)
#
# button4 = tk.Button(numbuttframe, text="4", font=('Arial', 18))
# button4.grid(row=0, column=3, sticky=tk.W+tk.E)
#
# button5 = tk.Button(numbuttframe, text="5", font=('Arial', 18))
# button5.grid(row=0, column=4, sticky=tk.W+tk.E)
#
# button6 = tk.Button(numbuttframe, text="6", font=('Arial', 18))
# button6.grid(row=0, column=5, sticky=tk.W+tk.E)
#
# yesbutton = tk.Button(yesnobuttframe, text="Yes", font=('Arial', 18))
# yesbutton.grid(row=0, column=0, sticky=tk.W+tk.E)
#
# nobutton = tk.Button(yesnobuttframe, text="No", font=('Arial', 18))
# nobutton.grid(row=0, column=1, sticky=tk.W+tk.E)
#
# numbuttframe.pack(fill='x')
# yesnobuttframe.pack(fill='x')
#
# if button1:
#     print("CELEBRATE!")
#
# window.mainloop()

import tkinter as tk
FONT = ('Ariel', 18)
class MyGui:

    def __init__(self):

        window = tk.Tk()

        window.geometry("500x500")
        window.title("Stock Watchlist & Logger")

        lbl = tk.Label(window, text="Tester", font=FONT)
        lbl.pack(padx=20, pady=20)

        text_box = tk.Text(window, height=3, font=('Ariel', 16))
        text_box.pack(padx=10, pady=10)

        num_btn = tk.Frame(window)
        yes_no_btn = tk.Frame(window)

        num_btn.pack(fill='x')
        yes_no_btn.pack(fill='x')

        buttons = []

        for i in range(1, 7):
            btn = tk.Button(num_btn, text=f"{i}", font=FONT)
            btn.pack(side="left", fill='x', expand=True)
            buttons.append(btn)


        yes_btn = tk.Button(yes_no_btn, text="Yes", font=FONT)
        yes_btn.pack(side="left", fill='x', expand=True)

        no_btn = tk.Button(yes_no_btn, text="No", font=FONT)
        no_btn.pack(side="left", fill='x', expand=True)






        window.mainloop()

if __name__ == "__main__":
    MyGui()