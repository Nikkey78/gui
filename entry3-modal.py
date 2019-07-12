# значения могут извлекаться из StringVar и после уничтожения виджета
from tkinter import *
from GUI.gui.entry3 import make_form, fetch, fields


def show(variables, popup):
    popup.destroy()     # здесь порядок не имеет значения
    fetch(variables)    # переменные сохраняются после уничтожения окна


def ask():
    popup = Toplevel()  # отображение формы в модальном диалоге
    vars = make_form(popup, fields)
    Button(popup, text='OK', command=(lambda: show(vars, popup))).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()  # ждать уничтожения окна


root = Tk()
Button(root, text='Dialog', command=ask).pack()
root.mainloop()
