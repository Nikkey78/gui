from tkinter import *

gifdir = './images/'
win = Tk()
img = PhotoImage(file=gifdir + 'spin.gif')
Button(win, image=img).pack(padx=100, pady=100)

# can = Canvas(win)
# can.pack(fill=BOTH)
# # can.config(width=img.width(), height=img.height())
# can.create_image(2, 2, image=img, anchor=NW)    # координаты x, y
win.mainloop()



