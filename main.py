from tkinter import *
from view.gui import GUI

        
def main():
    try:
        root = Tk()
        root.title('Slide Parser')
        
        app = GUI(root)
        root.mainloop()
    
    except Exception as err:
        print(err)
if __name__ == '__main__':
    main()
