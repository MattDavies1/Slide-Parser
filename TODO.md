# TODO

Nice to Have: 

- tunable sensitivity for box size.
Preview Boxes: 
- Preview the edges of thresholding --DONE


Needed:

- Image box recoginition made relative so that it determines to the size of the image -Matt -DONE

- Executable - SINA

- Scaling of gui -  Sina
- Parse button needs functionality - Sina --DONE
- Output Functionality - Sina --DONE
- relative position of gui - Matt -DONE
- READ ME
- Check Input and Output are not the same directorty -Matt
- Message box for errors of non selection - Sina


Future:
- ignore slides


Issue:
- Running Thread to close -> tkinter thread - Sina
- Box recognition has max size issue - Matt


Lab -> Cancer 
tissue sample on praphine -> hepatology


Gui to Control to model

choose_input_file:
I need you to have a image location -> image_location -> preview image

{
    "Inputs":{"file_location_input":"C:.///"}
    "Outputs":{"preview_image": Object}
}

parse_file:
Will provide outputlocation, inputlocation
{
    "Inputs":{"file_location_input":"C:.///",
                "folder_location_output":"C:.///",
                "input_sample_name":"string"}
}

preview_parsing:

{
    "Inputs":{"file_location_input":"C:.///"}
    "Outputs":{"labelled_preview_imgae": array}
}






message box: 
from tkinter import messagebox

messagebox.showerror("Title", "Message")