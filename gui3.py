from tkinter import *

# def greeting():
#     print('Hello stdout world')
#
# win = Frame()
# win.pack(expand=YES, fill=BOTH)
# # Button(win, text='Hello', command=greeting).pack(side=LEFT, fill=Y)
# # Label(win, text='Hello container world').pack(side=TOP)
# # Button(win, text='Quit', command=win.quit).pack(side=RIGHT, fill=X, expand=YES)
#
# Button(win, text='Hello', command=greeting).pack(side=LEFT, anchor=N)
# Label(win, text='Hello container world').pack(side=TOP)
# Button(win, text='Quit', command=win.quit).pack(side=RIGHT)
# win.mainloop()


class HelloButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.pack()
        self.config(fg='red', bg='black', font=('courier, 12'),
                    relief=RAISED, command=self.callback)

    def callback(self):
        print('Goodbye world...')
        self.quit()

if __name__ == '__main__':
    HelloButton(text='Hello subclass world').mainloop()
