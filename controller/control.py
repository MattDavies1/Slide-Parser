from model.labeler import preview_labling
from model.parser import slide_parsing_routine

def preview_parsing(file_location_input):
    """
    ...
    """
    # layup 

    output = preview_labling(file_location_input)
    return output

def parse_file(file_location_input: str, folder_location_output: str, input_sample_name: str):
    """
    ...
    """
    # layup

    output = slide_parsing_routine(file_location_input, folder_location_output, input_sample_name)
    return output

def choose_input_file():
    """
    ...
    """
    return
