import os


def print_tree(directory, level=0):
    # Get the list of files and folders in the given directory
    items = os.listdir(directory)

    # Loop through the items
    for item in items:
        # Create the full path of the item
        item_path = os.path.join(directory, item)

        # Print the item with indentation to represent the level in the tree
        print("    " * level + "|-- " + item)

        # If it's a directory, recursively print its contents
        if os.path.isdir(item_path):
            print_tree(item_path, level + 1)
