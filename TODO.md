# TODO

Nice to Have: 

Preview Boxes: 
- Preview the edges of thresholding


Needed:

- Image box recoginition made relative so that it determines to the size of the image

- Executable - SINA

- Scaling of gui -  Sina
- Parse button needs functionality - Sina
- Output Functionality - Sina
- relative position of gui - Sina
- READ ME

Future:
- ignore slides


Lab -> Cancer 
tissue sample on praphine -> hepatology


Gui to Control to model

choose_input_file:
I need you to have a image location -> image_location -> preview image

{
    "Inputs":{"file_location_input":"C:.///"}
    "Outputs":{"PreviewImage": Object}
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
    "Outputs":{"LabeledPreviewImage": array}
}
