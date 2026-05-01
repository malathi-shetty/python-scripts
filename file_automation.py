import os
import shutil

def copy_file(src, dest):
    shutil.copy(src, dest)
    print("File copied")

def rename_file(old, new):
    os.rename(old, new)
    print("File renamed")

def list_files(directory):
    for file in os.listdir(directory):
        print(file)

if __name__ == "__main__":
    list_files(".")
