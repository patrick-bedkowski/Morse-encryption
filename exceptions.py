'''
This module holds EXCEPTIONS
'''

class NoTextToProcess(ValueError):
    def __init__(self, input_txt):
        super().__init__('\n> No text was inserted')
        self.input_txt = input_txt

class FileNotFound(ValueError):
    def __init__(self, input_file):
        super().__init__('\n> File was not found')
        self.input_file = input_file
