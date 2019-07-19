# флажки, сложный способ (без переменных)
# from tkinter import *
#
# states = []
#
#
# def onPress(i):
#     states[i] = not states[i]           # изменяет False->True, True->False
#
#
# root = Tk()
# for i in range(10):
#     check = Checkbutton(root, text=str(i), command=(lambda i=i: onPress(i)))
#     check.pack(side=LEFT)
#     states.append(False)
#
# root.mainloop()
# print(states)



# проверка состояния флажков, простой способ
from tkinter import *

root = Tk()
states = []


for i in range(10):
    var = IntVar()
    check = Checkbutton(root, text=str(i), variable=var)
    check.pack(side=LEFT)
    states.append(var)

root.mainloop()
print([var.get() for var in states])
print(list(map(IntVar.get, states)))
print(list(map(lambda var: var.get(), states)))

