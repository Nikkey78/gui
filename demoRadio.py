"создает группу переключателей, которые вызывают демонстрационные диалоги"
from tkinter import *
from GUI.gui.dialogTable import demos
from GUI.gui.quitter import Quitter


class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text='Radio demos').pack(side=TOP)
        self.var = StringVar()
        for key in demos:
            Radiobutton(self, text=key,
                        command=self.onPress,
                        variable=self.var,
                        value=key).pack(anchor=NW)
        self.var.set(key)          # при запуске выбрать последний переключатель
        Button(self, text='State', command=self.report).pack(fill=X)
        Quitter(self).pack(fill=X)

    def onPress(self):
        pick = self.var.get()
        print('you pressed', pick)
        print('result:', demos[pick]())

    def report(self):
        print(self.var.get())


if __name__ == '__main__':
    Demo().mainloop()



# """
# переключатели, сложный способ (без переменных)
# обратите внимание, что метод deselect переключателя просто устанавливает пустую
# строку в качестве его значения, поэтому нам по-прежнему требуется присвоить
# переключателям уникальные значения или использовать флажки;
# """
# from tkinter import *
#
# state = ''
#
# buttons = []
#
#
# def onPress(i):
#     global state
#     state = i
#     for btn in buttons:
#         btn.deselect()
#     buttons[i].select()
#
#
# root = Tk()
# for i in range(10):
#     rad = Radiobutton(root, text=str(i),
#                             value=str(i),
#                             command=(lambda i=i: onPress(i)) )
#     rad.pack(side=LEFT)
#     buttons.append(rad)
# onPress(0)      # первоначально выбрать первый переключатель
# root.mainloop()
# print(state)        # вывести информацию о состоянии перед выходом


# переключатели, простой способ
# from tkinter import *
#
# root = Tk()             # IntVar также можно использовать
# var = IntVar(0)         # выбрать 0-й переключатель при запуске
# for i in range(10):
#     rad = Radiobutton(root, text=str(i), value=i, variable=var)
#     rad.pack(side=LEFT)
# root.mainloop()
# print(var.get())        # вывести информацию о состоянии перед выходом
















