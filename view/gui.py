from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk, UnidentifiedImageError
import sys

from controller.control import *


class GUI():
    """Gui class to add the functionality to the root frame
    """
    def __init__(self, root):
        """Initialize the general layout of the gui.
        mainframe is the parent of all widgets after root. 
        column and row configure is the scaling of the grid layout

        Args:
            root (Tk): the root object of tkinter -> root = Tk()
            
        """
        self.root = root
        self.mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, S, E, W))
        self.mainframe.columnconfigure(1, weight=0)
        self.mainframe.columnconfigure(2, weight=1)
        self.mainframe.columnconfigure(3, weight=0)
        self.mainframe.columnconfigure(4, weight=0)
        self.mainframe.columnconfigure(5, weight=1)
        self.mainframe.columnconfigure(6, weight=0)
        self.mainframe.rowconfigure(1, weight=1)
        self.mainframe.rowconfigure(2, weight=0)
        self.mainframe.rowconfigure(3, weight=0)
        self.mainframe.rowconfigure(4, weight=0)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.minsize(400,300)

        self.init_widgets()

    def init_widgets(self):
        """initialize all widgets in their default form.
        """
        #sample name text entry widget
        self.sample_name_textentry = StringVar()
        sample_name_textentry = ttk.Entry(self.mainframe, width=20, textvariable=self.sample_name_textentry)
        sample_name_textentry.grid(column=2, row=2, sticky=(W, E))
        
        sample_name_label = ttk.Label(self.mainframe, text="Sample Name")
        sample_name_label.grid(column=1, row=2, sticky=(E,W))

        #Input Location text entry widget
        self.input_location_textentry = StringVar()
        input_location_textentry = ttk.Entry(self.mainframe, width=20, textvariable=self.input_location_textentry)
        input_location_textentry.grid(column=2, row=3, sticky=(W, E))
        
        ttk.Label(self.mainframe, text="Input").grid(column=1, row=3, sticky=(E,W))
        self.choose_input_loc_button = ttk.Button(self.mainframe, text="...", command=self.choose_input_file)
        self.choose_input_loc_button.grid(column=3, row=3, sticky=(E,W))

        #Output Location text entry widget
        self.output_location_textentry = StringVar()
        output_location_textentry = ttk.Entry(self.mainframe, width=20, textvariable=self.output_location_textentry)
        output_location_textentry.grid(column=5, row=3, sticky=(W, E))
        
        ttk.Label(self.mainframe, text="Output").grid(column=4, row=3, sticky=(E,W))
        self.choose_output_loc_button = ttk.Button(self.mainframe, text="...", command=self.choose_output_folder)
        self.choose_output_loc_button.grid(column=6, row=3, sticky=(E,W))

        # parsing button widget
        self.preview_button = ttk.Button(self.mainframe, text="Parse", command=self.start_parsing_image)
        self.preview_button.grid(columnspan=3, column=1, row=4, sticky=(E,W))

        # preview button widget
        self.parse_button = ttk.Button(self.mainframe, text="Preview", command=self.show_preview_image)
        self.parse_button.grid(columnspan=4, column=4,row=4, sticky=(E,W))

        # image widget    
        self.image_label = Label(self.mainframe)
        self.image_label.grid(column=1, row=1, columnspan=6, sticky=(N,S,E,W))

        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
    
    ###Functions###
    #the triggers of the gui
        
    def choose_input_file(self):
        """allows the user to choose the image to be loaded into the program. 
        """
        ifile = filedialog.askopenfile(parent=self.mainframe,mode='rb',title='Choose a file')
        if ifile == None:
            messagebox.showerror("No Selection", "Please select a file!")
        else:
            try:
                # set width of scaled img
                basewidth = 420
                start = str(ifile).find("name='")
                file_location = str(ifile)[start+6:-2]
                self.input_location_textentry.set(file_location)
                # open img
                img = Image.open(ifile)
                # resize using img dimensions
                wpercent = (basewidth/float(img.size[0]))
                hsize = int((float(img.size[1])*float(wpercent)))
                img = img.resize((basewidth,hsize), Image.ANTIALIAS)
                # reset img variable
                image = ImageTk.PhotoImage(img)
                self.image_label.configure(image=image)
                self.image_label.image = image
            except UnidentifiedImageError as imageerr:
                print("check file type")
                messagebox.showerror("Image File Issue", "The input file was not entered or does not point to a jpg image!")
        

    def choose_output_folder(self):
        """allows the user to choose the folder to output the program results.
        """
        ofile = filedialog.askdirectory(parent=self.mainframe,mustexist=True,title='Choose a folder')
        
        if ofile == None or ofile == '':
            messagebox.showerror("No Selection", "Please select a file!")
        else:
            self.output_location_textentry.set(ofile)
            print(self.output_location_textentry.get())
        

    def show_preview_image(self):
        """previews the input image in parsed format.
        """
        ifile = self.input_location_textentry.get()
        if ifile == None:
            messagebox.showerror("No Selection", "Please select a file!")
        else:
            try:
                img = preview_parsing(ifile)

                # reset img variable
                image = ImageTk.PhotoImage(img)
                self.image_label.configure(image=image)
                self.image_label.image=image
            except AttributeError as err:
                messagebox.showerror("Image File Issue", "The input file was not entered or does not point to a jpg image!")
            except ValueError as valerr:
                print("check file type")
                messagebox.showerror("Image File Issue", "The input file was not entered or does not point to a jpg image!")
            except UnidentifiedImageError as imageerr:
                print("check file type")
                messagebox.showerror("Image File Issue", "The input file was not entered or does not point to a jpg image!")
        

    def start_parsing_image(self):
        """runs the parsing algorithm on the input image.
        """
        inputfile_location = self.input_location_textentry.get()
        outputfolder_location = self.output_location_textentry.get()
        print(is_same_path(inputfile_location, outputfolder_location))
        if not is_same_path(inputfile_location, outputfolder_location):    

            outputfile_name = self.sample_name_textentry.get()
            if (inputfile_location == None) or (outputfolder_location == None) or (outputfile_name == None):
                messagebox.showerror("No Selection", "one or all missing from input file location, output folder location or file name")
            else:
                parse_file(inputfile_location,outputfolder_location,outputfile_name)
        
        else:
            messagebox.showerror("Same Directory", f"Please choose a different folder path for the input and output images.\nInput path : {inputfile_location}\nOutput path: {outputfolder_location}")
        
        messagebox.showinfo("Done", f"Your Image Was Parsed and Placed in: {outputfolder_location}")
        
    
    def _check_window_state(self):
        print(self.root.state())
        if self.root.state() != 'normal':
            sys.exit(0)
