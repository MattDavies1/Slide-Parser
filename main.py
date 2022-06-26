from tkinter import *
from view.gui import GUI

        
def main():
    root = Tk()
    w,h  = 700,700
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x  = (ws/2) - (w/2)
    y  = (hs/2) - (h/2)
    root.geometry(f"{w}x{h}+{x:.0f}+{y:.0f}")
    # root.resizable(False, False)
    app = GUI()
    root.mainloop()

if __name__ == '__main__':
    main()
