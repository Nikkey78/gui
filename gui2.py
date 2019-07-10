import sys
from tkinter import *

                        # Связанные методы как обработчики событий
# class HellClass:
#     def __init__(self):
#         widjet = Button(None, text='Press me', command=self.quit)
#         widjet.pack()
#
#     def quit(self):
#         print('Hello class method quit world')      # self.quit - связанный метод
#         sys.exit()
#
# HellClass()
# mainloop()

                        # Объекты вызываемых классов
# как обработчики событий
# class HelloCallable:
#     def __init__(self):
#         self.msg = 'Hello __call__ world'
#
#     def __call__(self, *args, **kwargs):
#         print(self.msg)                     # __call__ вызывается при попытке обратиться
#         sys.exit()                          # к объекту класса как к функции
#
# widjet = Button(None, text='Press me', command=HelloCallable())
# widjet.pack()
# widjet.mainloop()

                        # Связывание событий

def hello(event):
    print('Press twice to exit')

def quit(event):
    print('Hello, I must be going...')
    sys.exit()

widjet = Button(None, text='Press me')
widjet.pack()
widjet.bind('<Button-1>', hello)
widjet.bind('<Double-1>', quit)
widjet.mainloop()





























