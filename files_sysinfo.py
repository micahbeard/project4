from sys import argv
import os


def list_info(path):
    try:
        # Directory File List
        dir_path = os.listdir(path)
        print(dir_path)
        # Environment Variables
        for name, value in os.environ.items():
            print("{0}: {1}".format(name, value))
    except: # Error Handling
        print("Not Correct Input")