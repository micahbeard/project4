import glob


def find_files():
    ext = input("File Ext: ")
    files = glob.glob('*.'+ext)
    for file in files:
        print(file)