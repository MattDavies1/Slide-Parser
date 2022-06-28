from tkinter import *
from tkinter import ttk

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

        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        
    def choose_input_file(self):
        print("choose input file")
    def choose_output_folder(self):
        print("choose output file")
    def show_preview_image(self):
        print("choose preview image")
    def start_parsing_image(self):
        print("choose parsing start")
