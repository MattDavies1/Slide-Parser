from tkinter import *
from view.gui import GUI
import sys

print("Python Code starting")

def destroy():
    print("destroying")
    sys.exit()
        
def main():
    try:
        root = Tk()
        root.title('Slide Parser')
        
        app = GUI(root)
        app.root.protocol("WM_DELETE_WINDOW", destroy)
        app.root.mainloop()

    except Exception as err:
        print(err)
if __name__ == '__main__':
    main()
