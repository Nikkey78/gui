from tkinter import *


def show_pos_event(event):
    print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))


def show_all_event(event):
    print(event)
    for attr in dir(event):
        if not attr.startswith('__'):
            print(attr, '=>', getattr(event, attr))


def on_key_press(event):
    if event.keycode == 8:
        print('Got "Return" key press')
    else:
        print('Got key press:', event.char)


def on_arrow_key(event):
    print('Got up arrow key press')


def on_enter_key(event):
    print('Got "Enter" key press')


def on_left_click(event):
    print('Got left mouse button click:', end=' ')
    show_pos_event(event)


def on_right_click(event):
    print('Got right mouse button click:', end=' ')
    show_pos_event(event)


def on_middle_click(event):
    print('Got middle mouse button click:', end=' ')
    show_pos_event(event)
    show_all_event(event)


def on_left_drag(event):
    print('Got left mouse button drag:', end=' ')
    show_pos_event(event)


def on_double_left_click(event):
    print('Got double left mouse click:', end=' ')
    show_pos_event(event)
    tkroot.quit()


tkroot = Tk()
lablefont = ('courier', 20, 'bold')
widget = Label(tkroot, text='Hello bind world')
widget.config(bg='red', font=lablefont)
widget.config(height=5, width=20)
widget.pack(expand=YES, fill=BOTH)

widget.bind('<Button-1>', on_left_click)
widget.bind('<Button-3>', on_right_click)
widget.bind('<Button-2>', on_middle_click)

widget.bind('<Double-1>', on_double_left_click)
widget.bind('<B1-Motion>', on_left_drag)
widget.bind('<KeyPress>', on_key_press)
widget.bind('<Up>', on_arrow_key)
widget.bind('<Return>', on_enter_key)
widget.focus()

tkroot.title('Click Me')
tkroot.mainloop()

# <ButtonRelease>
# <ButtonPress>
# <Motion>
# <Enter>
# <Leave>
# <Configure>
# <Destroy>
# <FocusIn>
# <FocusOut>
# <Map>
# <Unmap>
# <Escape> <Key-Escape>
# <BackSpace>
# <Tab>
# Down>, <Left> и <Right>
# <KeyPress-a> <Key-a> генерируется только при нажатии клавиши «a».
# <<PasteText>>


