from tkinter import *

# msg = Message(text='Oh by the way, which one`s Pink?')
# msg.config(bg='pink', font=('times', 16, 'italic'))
# msg.pack(expand=YES, fill=X)
# mainloop()

from GUI.gui.quitter import Quitter


def fetch():
    print('Input => "%s"' % ent.get())


root = Tk()
ent = Entry(root)
ent.delete(0, END)               # сперва удалить текст с начала до конца
# ent.insert(END, '_xxx')

ent.insert(0, 'Type words here')
ent.pack(side=TOP, fill=X)
ent.focus()
ent.bind('<Return>', (lambda event: fetch()))
btn = Button(root, text='Fetch', command=fetch)
btn.pack(side=LEFT)
Quitter(root).pack(side=RIGHT)
root.mainloop()
