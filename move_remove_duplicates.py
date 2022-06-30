from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
from pathlib import Path
import shutil
import hashlib

Tk().withdraw()
path = askdirectory(title='Select a directory') # show the dialog box to select a directory 


duplicate_directory = "C:/Duplicate_Files"
# checks if the directory exists, if not it creates it
if not os.path.exists("C:/Duplicate_Files"):
        duplicate_directory = os.mkdir("C:/Duplicate_Files")
walker = os.walk(path)
uniqueFiles = {}
duplicates = []
# loops through the directory and checks for duplicates
for folder,sub_folder,files in walker:
    # loop through the files in the folder
    for file in files:
        filepath = os.path.join(folder,file) # reads the filepath
        # print(filepath)
        # reads the file and hashes it through the hashlib library with the md5 algorithm
        filehash = hashlib.md5(open(filepath,'rb').read()).hexdigest() 
        # checks if the filehash is in the uniqueFiles dictionary
        if filehash in uniqueFiles:
            try:
                # print("Duplicate found: {} and {}".format(filepath, uniqueFiles[filehash]))
                shutil.move(filepath, duplicate_directory) # moves the file to the duplicate directory
            except Exception as e:
                print("Exist files are not moved but deleted")
                os.remove(filepath) # deletes the file if it already exists in the duplicate directory
                
        # if the filehash is not in the uniqueFiles dictionary     
        else:
            uniqueFiles[filehash] = [path] # add filepath to dictionary