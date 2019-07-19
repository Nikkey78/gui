"""отображает изображение с помощью стандартного объекта PhotoImage из биб-
# лиотеки tkinter; данная реализация может работать с GIF-файлами, но не может
# обрабатывать изображения в формате JPEG; использует файл с изображением, имя
# которого указано в командной строке, или файл по умолчанию; используйте Canvas
# вместо Label, чтобы обеспечить возможность прокрутки, и т.д.
# """

import os, sys
from tkinter import *
from PIL.ImageTk import PhotoImage

dir = './images/'
photo = 'Lighthouse.jpg'
if len(sys.argv) > 1:
    photo = sys.argv[1]
path = os.path.join(dir, photo)

win = Tk()
win.title(photo)
photo_obj = PhotoImage(file=dir + photo)

Label(win, image=photo_obj).pack()
print(photo_obj.width(), photo_obj.height())
win.mainloop()