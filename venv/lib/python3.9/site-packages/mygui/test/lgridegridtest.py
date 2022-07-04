import os
import sys
from tkinter import Entry, Label, Text, Tk

from mygui import egrid, lgrid

root = Tk()
root.minsize(800, 500)
root.title('Egrid and Lgrid')
mylabels = ['0,0', '1,1', '2,2', '3,3', '4,4', '3,5', '2,6', '1,7', '0,8']
myentrys = ['1,0', '2,1', '3,2', '4,3', '5,4', '4,5', '3,6', '2,7', '1,8']
print(mylabels)

for i in (mylabels):
    lgrid(root, 'Text COLUMN =  '+i[2] + '  ROW = '+i[0], i[0], i[2])

for a in (myentrys):
    egrid(root, a[0], a[2])

message = "lgrid(self, text, gridcol, gridrow, **args)\nLabel Maker for quick labels in a GUI window.\n\nExample: \n\nlgrid(root, 'text to enter', 0, 0, **args)\n\nWhere root is the instance of tkinter, \n\n'Text to enter' is just that,\n0, 0 is the column and row to place them"
tx1 = Text(root)

tx1.grid(row=10, columnspan=5)
tx1.insert(1.0, message)
root.mainloop()
