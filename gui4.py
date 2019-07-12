from GUI.gui.gui3 import HelloButton

class MyButton(HelloButton):
    def callback(self):
        print('Ignoging press!...')



if __name__ == '__main__':
    MyButton(text='Press me').mainloop()

# from tkinter import *
#
# class Hello(Frame):
#     def __init__(self, parent=None):
#         Frame.__init__(self, parent)
#         self.pack()
#         self.data = 42
#         self.make_widjets()
#
#     def make_widjets(self):
#         widjet = Button(self, text='Hello frame world', command=self.message)
#         widjet.pack(side=LEFT)
#
#     def message(self):
#         self.data += 1
#         print('Hello frame world %s' % self.data)
#
#
# if __name__ == '__main__':
#     Hello().mainloop()

# Автономные классы-контейнеры
# from tkinter import *
#
# class HelloPackage:
#     def __init__(self, parent=None):
#         self.top = Frame(parent)
#         self.top.pack()
#         self.data = 0
#         self.make_widjets()
#
#     def make_widjets(self):
#         Button(self.top, text='Bye', command=self.top.quit).pack(side=LEFT)
#         Button(self.top, text='Hye', command=self.message).pack(side=RIGHT)
#
#     def message(self):
#         self.data += 1
#         print('Hello number', self.data)
#
#
# if __name__ == '__main__':
#     HelloPackage().top.mainloop()
