from exceptions import (
    FileNotFound,
    NoTextToProcess
)

def read_txt_file(input_file):
    '''
    This function receives path to .txt file that later returns as string
    '''
    try:
        with open(input_file, "r") as file_handle:  # open file
            lines = file_handle.readlines()  # file's lines
            # if file is empty, raise error
            if all(len(line.strip()) == 0 for line in lines):
                raise NoTextToProcess('No text was inserted')
            else:
                string_data = ''
                for line in lines:
                    for character in line:
                        string_data += character
                return string_data  # return string text
    except FileNotFoundError:
        raise FileNotFound('File was not found')