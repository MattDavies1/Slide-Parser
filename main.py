from tkinter import *
from view.gui import GUI

        
def main():
    root = Tk()
    root.geometry("700x700")
    # root.resizable(False, False)
    app = GUI()
    root.mainloop()

if __name__ == '__main__':
    main()
