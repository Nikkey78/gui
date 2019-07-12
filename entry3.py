"""
использует переменные StringVar
компоновка по колонкам: вертикальные координаты виджетов могут не совпадать
(смотрите entry2)
"""
from tkinter import *
from GUI.gui.quitter import Quitter

fields = ('Name', 'Job', 'Pay')


def fetch(variables):
    for var in variables:
        print('Input => "%s"' % var.get())


def make_form(root, fields):
    form = Frame(root)
    left = Frame(form)
    right = Frame(form)
    form.pack(fill=X)
    left.pack(side=LEFT)
    right.pack(side=RIGHT, expand=YES, fill=X)

    variables = []
    for field in fields:
        lab = Label(left, width=5, text=field)
        ent = Entry(right)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X)
        var = StringVar()
        ent.config(textvariable=var)
        var.set('enter here')
        variables.append(var)
    return variables


if __name__ == '__main__':
    root = Tk()
    vars = make_form(root, fields)
    Button(root, text='Fetch', command=(lambda: fetch(vars))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: fetch(vars)))
    root.mainloop()
