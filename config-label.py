# from tkinter import *
#
# root = Tk()
# root.geometry('460x300+300+300')
# labelfont = ('times', 20, 'bold underline italic')
# widget = Label(root, text='Hello config world')
# widget.config(bg='#6200ee', fg='#ffffff', relief=FLAT, bd=3, cursor='hand2')
# widget.config(font=labelfont)
# widget.config(height=3, width=20)
# widget.pack(expand=YES, fill=X)
# root.mainloop()

import sys
from tkinter import Toplevel, Label, Button

win1 = Toplevel()
win2 = Toplevel()

Button(win1, text='Spam1', command=sys.exit).pack()
Button(win2, text='Spam2', command=sys.exit).pack()

Label(text='Popups').pack()
win1.mainloop()


