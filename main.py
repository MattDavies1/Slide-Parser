from tkinter import *
from tkinter import filedialog
from PIL import  Image,ImageTk

class GUI(Frame):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("Slider Parse Bot v0.1")
        self.pack(fill=BOTH, expand=TRUE)

        # Picture Frame

        frame1 = Frame(self, relief=GROOVE, borderwidth = 1)
        frame1.pack(fill=BOTH, expand=1)

        lbl1 = Label(frame1, text="Sample Picture")
        lbl1.pack(anchor=N, padx=5, pady=5)

        image = PhotoImage(file='')
        self.label = Label(frame1, image=image)
        self.label.pack()

        # Frame for Sample Name input

        frame2 = Frame(self, relief=GROOVE, borderwidth = 1)
        frame2.pack(fill=BOTH)

        lbl2 = Label(frame2, text="Sample Name: ")
        lbl2.pack(side=LEFT, anchor=N, padx=5, pady=5)

        sampleName = Entry(frame2)
        sampleName.pack(side=LEFT, anchor=N, padx=5, pady=5)

        # Input and Output Selector

        frame3 = Frame(self, relief=GROOVE, borderwidth = 1, height=100)
        frame3.pack(fill=BOTH)

        # Input
        inputFrame = Frame(frame3, relief=GROOVE, borderwidth = 1)
        inputFrame.pack(side=LEFT, fill=BOTH, expand=1)\

        lbl5 = Label(inputFrame, text="Input")
        lbl5.pack(side=LEFT, anchor=N, padx=5, pady=5)

        self.input_text = Entry(inputFrame)
        self.input_text.pack()

        selectInput = Button(inputFrame, text="Choose...", command=self.chooseInputFile)
        selectInput.pack()

        # Output
        outputFrame = Frame(frame3, relief=GROOVE, borderwidth = 1)
        outputFrame.pack(side=RIGHT, fill=BOTH, anchor=E, expand=1)

        lbl6 = Label(outputFrame, text="Output")
        lbl6.pack(side=LEFT, anchor=N, padx=5, pady=5)

        outputText = StringVar()
        outputEntry = Entry(outputFrame, text=outputText)
        outputEntry.pack()

        selectOutput = Button(outputFrame, text="Choose...", command=self.chooseOutput)
        selectOutput.pack()

        # The button!

        frame4 = Frame(self, relief=GROOVE, borderwidth = 1, height=50)
        frame4.pack(fill=BOTH)

        previewButton = Button(frame4, text="Preview")
        previewButton.pack()

        parseButton = Button(frame4, text="Parse!")
        parseButton.pack()

    ########## Functions ##########
    # Pull photo, resize, and display in the App. Refers to self.label
    def chooseInputFile(self):
        ifile = filedialog.askopenfile(parent=self,mode='rb',title='Choose a file')
        # set width of scaled img
        basewidth = 420
        start = str(ifile).find("name='")
        file_location = str(ifile)[start+6:-2]
        self.input_text.insert(0, file_location)
        # open img
        img = Image.open(ifile)
        # resize using img dimensions
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        # reset img variable
        self.image2 = ImageTk.PhotoImage(img)
        self.label.configure(image=self.image2)
        self.label.image=self.image2
    
    def chooseOutputFolder(self):
        print(self.outputText)
        # self.output_text.delete(0, END)
        # self.output_text.insert(0, text)
        
def main():
    root = Tk()
    root.geometry("700x700")
    # root.resizable(False, False)
    app = GUI()
    root.mainloop()

if __name__ == '__main__':
    main()
