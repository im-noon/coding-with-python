import os
import re
def rename_files():
    #get the list of files
    file_path = "/Users/Slimn/Desktop/Work/Project/Python/Programming Foundations with Python/prank"
#    file_list = os.listdir(r"/Users/Slimn/Desktop/Work/Project/Python/Programming Foundations with Python/prank")
    file_list = os.listdir(file_path)   
    print(file_list)

    #change working directory
    os.chdir(file_path)
    #rename all file
    for file_name in file_list:
        print("Old Name - " +file_name)
        print("New Name - " +re.sub("[0-9]","", file_name))
        os.rename(file_name, re.sub("[0-9]","", file_name))
    os.chdir(file_path)

rename_files()
