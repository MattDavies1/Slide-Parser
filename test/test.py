from tkinter import *
from tkinter import filedialog
from PIL import  Image,ImageTk


class GUI(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        w,h = 1000, 1000 # define relative to window size
        master.minsize(width=w, height=h)

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)

        self.pack(side=BOTTOM)

        # File selectiuon Cluster
        self.input = Label(self, text="Input File").pack(side = TOP, pady=5, padx=5)
        self.file = Button(self, text='Choose...', command=self.choose)

        # Photo of slide book
        self.image = PhotoImage(file='')
        self.label = Label(image=self.image)

        frame = Frame(self, relief=RAISED, borderwidth=5)
        frame.pack(fill=BOTH, expand=True)

        self.parseButton = Button(self, text="Parse!")

        self.file.pack()
        self.label.pack(pady=50, padx=50, side=TOP)
        self.parseButton.pack(side = TOP, pady=5, padx=5)

    # Function to pull photo, resize, and display in the App. Refers to self.label
    def choose(self):
        ifile = filedialog.askopenfile(parent=self,mode='rb',title='Choose a file')
        # set width of scaled img
        basewidth = round(root.winfo_width()*0.6)
        print(basewidth)
        # open img
        img = Image.open(ifile)
        # resize using img dimensions
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        # reset img vasriable
        self.image2 = ImageTk.PhotoImage(img)
        self.label.configure(image=self.image2)
        self.label.image=self.image2


root = Tk()
root.title("Slide Parser v0.1")
app = GUI(master=root)
app.mainloop()
root.destroy()