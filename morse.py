from file_management import read_txt_file
from encrypt import encrypt
from exceptions import FileNotFound, NoTextToProcess
import argparse

parser = argparse.ArgumentParser(description='Process some file.')
parser.add_argument('file', type = str, help = "file with text")

def main():
    try:
        args = parser.parse_args()
        path = args.file #file with its path

        # convert file to string
        string = read_txt_file(path)

        #encrypt string
        processed_text = encrypt(string)

        #print processed text to user
        print(processed_text)
    except (FileNotFound, NoTextToProcess) as message:
        # print error message
        print(message)


if __name__ == '__main__':
    main()
