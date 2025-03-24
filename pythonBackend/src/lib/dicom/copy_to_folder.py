import shutil
import os


def copy_folder_contents(source_folder, destination_folder):
    # Check if the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(
            destination_folder
        )  # Create the destination folder if it does not exist

    # Walk through the source folder and copy all files and subdirectories
    for item in os.listdir(source_folder):
        source_path = os.path.join(source_folder, item)
        destination_path = os.path.join(destination_folder, item)

        if os.path.isdir(source_path):
            # If it's a directory, copy the directory recursively
            shutil.copytree(source_path, destination_path)
        else:
            # If it's a file, copy the file
            shutil.copy2(source_path, destination_path)
