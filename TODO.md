# TODO

## Nice to Have: 

* [ ] tunable sensitivity for box size. -Matt
* [X] Preview the edges of thresholding -Matt --DONE
* [ ] Scale Image with GUI -> Nice to Have Post Testing 
* [ ] Normalize Image Size 




## Required To Have:
### Sina

- [X] Executable - SINA
- [X] Scaling of gui -  Sina
- [X] Parse button needs functionality - Sina --DONE
- [X] Output Functionality - Sina --DONE
- [X] Message box for errors of non selection - Sina --Done
- [X] Message box for time consuming functions on gui - Sina -> will stop program -> checked multithread and matplot lib isnt supported -> DW bout it
- [X] Implement Directory Difference - Sina
- [X] Icons addition -> Will Be Delivered - Sina


### Matt
- [X] Image box recoginition made relative so that it determines to the size of the image -Matt -DONE
- [X] relative position of gui - Matt -DONE
- [X] Check Input and Output are not the same directorty -Matt

## Future Improvements:
- [ ] ignore slides

## Issues:

### Sina
- [X] Running Thread to close -> tkinter thread - Sina --Done
### Matt
- [ ] Box recognition has max size issue - Matt 

### Unassigned

### To Discuss

- [X] Theme changes -> 
- [X] Install wizard -> DW bout it
- [ ] Run Book


## Notes
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

