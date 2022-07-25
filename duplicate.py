import glob
import os
import shutil

# Source directory
src_folder = r"C:\Users\Habib Ur Rehman\Downloads\duplicate check"
# destination folder, Note. Destination folder should not be in source folder.
dst_folder = r"C:\Users\Habib Ur Rehman\Downloads\Programs\New folder"

# Search files with .txt extension in source directory
pattern = r"C:\Users\Habib Ur Rehman\Downloads\duplicate check\**\*1.mp3"
files = glob.glob(src_folder + pattern)

# move the files with txt extension
for item in glob.iglob(pattern, recursive=True):
    # extract file name form file path
    file_name = os.path.basename(item)
    name = file_name + os.path.dirname(item.split('\\')[3])

    try:
        shutil.move(item, dst_folder)
    except Exception as e:
        os.remove(item)

    print(f"Moved: {item} to {dst_folder}")

pattern = r"C:\Users\Habib Ur Rehman\Downloads\duplicate check\**\*1.m4a"
files = glob.glob(src_folder + pattern)

# move the files with txt extension
for item in glob.iglob(pattern, recursive=True):
    # extract file name form file path
    file_name = os.path.basename(item)
    name = file_name + os.path.dirname(item.split('\\')[3])

    try:
        shutil.move(item, dst_folder)
    except Exception as e:
        os.remove(item)

    print(f"Moved: {item} to {dst_folder}")