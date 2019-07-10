from tkinter import *
import sys

                            # Lable
# widget = Label(None, text='Hello GUI world!')
# widget.pack(side=TOP)
# widget.mainloop()

# root = Tk()
# Label(root, text='Hello GUI world!').pack(expand=YES, fill=BOTH)
# root.mainloop()

# root = Tk()
# widjet = Label()
# widjet['text'] = 'Hello GUI world!'
# widjet.pack(side=TOP)
# root.mainloop()

# Label(None, {'text': 'Hello GUI world!', Pack: {'side': 'top'}}).mainloop()

# options = {'text': 'Hello GUI world!'}
# layout = {'side': 'top'}
# Label(None, **options).pack(**layout)
# mainloop()

# root = Tk()
# widjet = Label(root)
# widjet.config(text='Hello GUI world!')
# widjet.pack(side=TOP, expand=YES, fill=BOTH)
# root.title('gui1g.py')
# root.mainloop()

                            # Button
# widjet = Button(None, text='Press me!', command=sys.exit)
# widjet.pack()
# widjet.mainloop()

# root = Tk()
# Button(None, text='Press me!', command=root.quit)\
#     .pack(side=LEFT, expand=YES, fill=BOTH)
# root.mainloop()


# def quit():
#     print('Hello, I must be going...')
#     sys.exit()

# widjet = Button(None, text='Hello event world', command=quit)
# widjet.pack()
# widjet.mainloop()


# widjet = Button(None, text='Hello event world',
#                 command=(lambda: print('Hello lambda world') or
#                 print('One more hello lamda') or sys.exit()))
# widjet.pack()
# widjet.mainloop()


# def handler(a: int, b: str):
#     print(str(a), b)
#
# x = 20 # глобальная переменная
#
# widjet = Button(None, text='Hello event world',
#                 command=(lambda: handler(x, 'is a number') or sys.exit()))
# widjet.pack()
# widjet.mainloop()


# def handler(a: int, b: str):
#     print(str(a), b)
#
# x = 21 # глобальная переменная
#
# def func():
#     handler(x, 'is a number')
#
# widjet = Button(None, text='Hello event world', command=func)
# widjet.pack()
# widjet.mainloop()


# def handler(a: int, b: str):
#     print(str(a), b)
#
# def makegui():
#     x = 21
#     Button(None, text='Hello event world', command=(lambda: handler(x, 'is a number'))).pack()
#     Button(None, text='Hello event world', command=(lambda X=x: handler(X, 'is a number'))).pack()
#
# makegui()
# mainloop()

#
# class Gui:
#     def handler(self, a: int, b: str):
#         print(str(a), b)
#
#     def makegui(self):
#         x = 21
#         Button(text='Button', command=(lambda: self.handler(x, 'spam'))).pack()
#
# Gui().makegui()
# mainloop()



# # просто переменная, это замыкание, будет ссылка только на последнее значение
# def odd():
#     funcs = []
#     for c in 'abcdefg':
#         funcs.append((lambda: c))   # поиск переменной c будет выполнен позднее
#     return funcs                    # не сохраняет текущее значение c
#
# for func in odd():
#     print(func(), end=' ')          # Опа!: выведет 7 символов g, а не a,b,c,... !


# # переменная вводится как значение по умолчанию, учитывается каждое текущее значение
# def odd():
#     funcs = []
#     for c in 'abcdefg':
#         funcs.append((lambda c=c: c))   # запомнить текущее значение c
#     return funcs                        # значения по умолчанию вычисляются немедленно
#
# for func in odd():
#     print(func(), end=' ')              # OK: теперь выведет a,b,c,...











