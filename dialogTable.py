# определяет таблицу имя:обработчик с демонстрационными примерами

from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askquestion, showerror
from tkinter.simpledialog import askfloat

demos = {
    'Open': lambda: askopenfilename(filetypes=[("all files", "*"),
                                               ('text files', '*.txt'),
                                               ('DO files', '*.DO')]),
    'Color': askcolor,
    'Query': lambda: askquestion('Warning', 'You typed "rm * "\nConfirm?'),
    'Error': lambda: showerror('Error', 'He`s dead, Jim'),
    'Input': lambda: askfloat('Entry', 'Enter credit card number')
}

# initialdir, initialfile, title, defaultextension, parent