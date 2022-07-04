
import os

try:

    from mygui import lgrid
except:
    os.system('pip install mygui')
    from mygui import lgrid

from tkinter import Tk

root = Tk()
root.minsize(300, 100)
lgrid(root, 'Label placed in grid 5,5', 5, 5)
lgrid(root, 'Label placed in grid 6,6', 6, 6)

root.mainloop()
