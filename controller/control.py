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

def is_same_path(source_file_path, target_dir_path):
    result = None
    if source_file_path.rfind(target_dir_path) != -1:
        if source_file_path.rfind(target_dir_path) == 0:
            test_obj_1 = file_path.split(target_dir_path)[1]
            test_obj_2 = test_obj_1.split('/')[1]
            test_obj_3 = test_obj_2.rfind('/')
            if test_obj_3 == -1:
                result = True
    else:
        result = False
    return result
