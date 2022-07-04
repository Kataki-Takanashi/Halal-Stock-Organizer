import os
from tkinter import Tk

from mygui import egrid, lgrid

root = Tk()
root.minsize(300, 100)
lgrid(root, 'Label placed in grid 0,0', 0, 0)
lgrid(root, 'Label placed in grid 0,1', 0, 1)
egrid(root, 1, 0)
root.mainloop()
