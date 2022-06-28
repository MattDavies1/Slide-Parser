from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk, UnidentifiedImageError

from controller.control import *


class GUI():
    def __init__(self, root):
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
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
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.init_widgets()

    def init_widgets(self):
        #sample name text entry widget
        sample_name_textentry = StringVar()
        feet_entry = ttk.Entry(self.mainframe, width=20, textvariable=sample_name_textentry)
        feet_entry.grid(column=2, row=2, sticky=(W, E))
        
        sample_name_label = ttk.Label(self.mainframe, text="Sample Name")
        sample_name_label.grid(column=1, row=2, sticky=(E,W))

        #Input Location text entry widget
        self.input_location_textentry = StringVar()
        feet_entry = ttk.Entry(self.mainframe, width=20, textvariable=self.input_location_textentry)
        feet_entry.grid(column=2, row=3, sticky=(W, E))
        
        ttk.Label(self.mainframe, text="Input").grid(column=1, row=3, sticky=(E,W))
        self.choose_input_loc_button = ttk.Button(self.mainframe, text="...", command=self.choose_input_file)
        self.choose_input_loc_button.grid(column=3, row=3, sticky=(E,W))

        #Output Location text entry widget
        self.output_location_textentry = StringVar()
        feet_entry = ttk.Entry(self.mainframe, width=20, textvariable=self.output_location_textentry)
        feet_entry.grid(column=5, row=3, sticky=(W, E))
        
        ttk.Label(self.mainframe, text="Output").grid(column=4, row=3, sticky=(E,W))
        self.choose_output_loc_button = ttk.Button(self.mainframe, text="...", command=self.choose_output_folder)
        self.choose_output_loc_button.grid(column=6, row=3, sticky=(E,W))

        # parsing button widget
        self.preview_button = ttk.Button(self.mainframe, text="preview", command=self.start_parsing_image)
        self.preview_button.grid(columnspan=3, column=1, row=4, sticky=(E,W))

        # preview button widget
        self.parse_button = ttk.Button(self.mainframe, text="parse", command=self.show_preview_image)
        self.parse_button.grid(columnspan=4, column=4,row=4, sticky=(E,W))

        # image widget    
        self.sample_image_PhotoImage = Image.open('./test/outputs/Black-test_1.png')
        photo = ImageTk.PhotoImage(self.sample_image_PhotoImage)
        self.image_label = Label(self.mainframe, image = photo)
        self.image_label.image = photo
        self.image_label.grid(column=1, row=1, columnspan=6, sticky=(N,S,E,W))

        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        
    def choose_input_file(self):
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
        print("choose output file")
    def show_preview_image(self):
        print("choose preview image")
    def start_parsing_image(self):
        print("choose parsing start")
