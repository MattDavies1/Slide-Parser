from multiprocessing.sharedctypes import Value
from tkinter import *
from PIL import  Image,ImageTk, UnidentifiedImageError
from tkinter import filedialog, messagebox

from pyparsing import Or
from controller.control import *


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

        self.sampleName = Entry(frame2)
        self.sampleName.pack(side=LEFT, anchor=N, padx=5, pady=5)

        # Input and Output Selector

        frame3 = Frame(self, relief=GROOVE, borderwidth = 1, height=100)
        frame3.pack(fill=BOTH)

        # Input
        inputFrame = Frame(frame3, relief=GROOVE, borderwidth = 1)
        inputFrame.pack(side=LEFT, fill=BOTH, expand=1)\

        lbl5 = Label(inputFrame, text="Input")
        lbl5.pack(side=LEFT, anchor=N, padx=5, pady=5)

        self.inputText = StringVar()
        input_text = Entry(inputFrame, text=self.inputText)
        input_text.pack()

        selectInput = Button(inputFrame, text="Choose...", command=self.chooseInputFile)
        selectInput.pack()

        # Output
        outputFrame = Frame(frame3, relief=GROOVE, borderwidth = 1)
        outputFrame.pack(side=RIGHT, fill=BOTH, anchor=E, expand=1)

        lbl6 = Label(outputFrame, text="Output")
        lbl6.pack(side=LEFT, anchor=N, padx=5, pady=5)

        self.outputText = StringVar()
        outputEntry = Entry(outputFrame, text=self.outputText)
        outputEntry.pack()

        selectOutput = Button(outputFrame, text="Choose...", command=self.chooseOutputFolder)
        selectOutput.pack()

        # The button!

        frame4 = Frame(self, relief=GROOVE, borderwidth = 1, height=50)
        frame4.pack(fill=BOTH)

        previewButton = Button(frame4, text="Preview", command=self.showPreviewParser)
        previewButton.pack()

        parseButton = Button(frame4, text="Parse!", command=self.startParsingImage)
        parseButton.pack()

    ########## Functions ##########
    # Pull photo, resize, and display in the App. Refers to self.label
    def chooseInputFile(self):
        
        ifile = filedialog.askopenfile(parent=self,mode='rb',title='Choose a file')
        if ifile == None:
            messagebox.showerror("No Selection", "Please select a file!")
        else:
            try:
                # set width of scaled img
                basewidth = 420
                start = str(ifile).find("name='")
                file_location = str(ifile)[start+6:-2]
                self.inputText.set(file_location)
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
            except UnidentifiedImageError as imageerr:
                print("check file type")
                messagebox.showerror("Image File Issue", "The input file was not entered or does not point to a jpg image!")
    
    def chooseOutputFolder(self):
        ofile = filedialog.askdirectory(parent=self,mustexist=True,title='Choose a folder')
        if ofile == None:
            messagebox.showerror("No Selection", "Please select a file!")
        else:
            self.outputText.set(ofile)
            print(self.outputText.get())

    def showPreviewParser(self):
        
        ifile = self.inputText.get()
        if ifile == None:
            messagebox.showerror("No Selection", "Please select a file!")
        else:
            try:
                img = preview_parsing(ifile)

                # reset img variable
                self.image2 = ImageTk.PhotoImage(img)
                self.label.configure(image=self.image2)
                self.label.image=self.image2
            except AttributeError as err:
                messagebox.showerror("Image File Issue", "The input file was not entered or does not point to a jpg image!")
            except ValueError as valerr:
                print("check file type")
                messagebox.showerror("Image File Issue", "The input file was not entered or does not point to a jpg image!")
            except UnidentifiedImageError as imageerr:
                print("check file type")
                messagebox.showerror("Image File Issue", "The input file was not entered or does not point to a jpg image!")

    def startParsingImage(self):
        
        inputfile_location = self.inputText.get()
        outputfolder_location = self.outputText.get()
        outputfile_name = self.sampleName.get()
        if (inputfile_location == None) or (outputfolder_location == None) or (outputfile_name == None):
            messagebox.showerror("No Selection", "one or all missing from input file location, output folder location or file name")
        else:
            parse_file(inputfile_location,outputfolder_location,outputfile_name)