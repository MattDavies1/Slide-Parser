from tkinter import *
from tkinter import ttk

from controller.control import *


class GUI():
    def __init__(self, root):
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

def chooseInputFile():
    pass
def chooseOutputFolder():
    pass
def showPreviewParser():
    pass
def startParsingImage():
    pass
