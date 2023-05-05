import os
import shutil

class FindFile():
    def find_file(self, file_for_name):
        """
        Searches for a file in all available drives and returns its path
        """
        for drive in range(ord('A'), ord('Z') + 1):
            drive_letter = chr(drive)
            drive_path = os.path.join(drive_letter + ":", os.sep)
            if os.path.exists(drive_path):
                for root, dirs, files in os.walk(drive_path):
                    for file in files:
                        if file == file_for_name:
                            # If a file is found, return its location
                            file_path = os.path.join(root, file)
                            # Printing the file location
                            print(f"File {file} found at: {file_path}")
                            return file_path
        return None

file_for_name = input("Input the name to create a PDF statement (or 'cancel' to exit): ")

# Create an instance of the FindFile class
ff = FindFile()

# Find the file and get its path
file_path = ff.find_file(file_for_name)

if file_path is None:
    print(f"{file_for_name} not found in any available drives.")
else:
    # Specify the source file path and the destination folder path
    src = file_path
    dst = os.path.join(os.path.expanduser("~"), "Desktop", "PDFs", f"{file_for_name}")

    # Move the file to the destination folder and check if it was successful or not
    try:
        shutil.move(src, dst)
        print(f"{file_for_name} was successfully moved to {dst}")
    except FileNotFoundError:
        print(f"{file_for_name} not found in {src}")
