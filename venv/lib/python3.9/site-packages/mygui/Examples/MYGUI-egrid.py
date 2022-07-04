import os
from tkinter import Entry, Tk

from mygui import egrid, lgrid

root = Tk()
root.title('EGRID example')
root.minsize(300, 100)
egrid(root, 0, 0)
root.mainloop()
