import os
import sys
from typing import Union, List

# Define Directory class
class Directory:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.children: List[Union['Directory', 'File']] = []

    def __repr__(self) -> str:
        return f"Directory({self.name})"

    def display(self, indent: int = 0) -> None:
        print("  " * indent + self.name)
        for child in self.children:
            child.display(indent + 1)


# Define File class
class File:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"File({self.name})"

    def display(self, indent: int = 0) -> None:
        print("  " * indent + self.name)


# Function to parse the Emmet-like string and create directories and files
def organize(emmet_string: str, current_dir: Union[Directory, None] = None, i: int = 0) -> int:
    if not current_dir:
        current_dir = Directory('')  # Start without root

    dir_or_file = ""
    while i < len(emmet_string):
        ch = emmet_string[i]
        
        if ch == "^":  # Go up to the parent directory
            if "." in dir_or_file:  # It's a file
                file = File(dir_or_file)
                current_dir.children.append(file)
            else:  # It's a directory
                dir = Directory(dir_or_file)
                current_dir.children.append(dir)
            return i + 1
        
        elif ch == ">":  # Create a subdirectory or file in the current directory
            if "." in dir_or_file:  # It's a file
                file = File(dir_or_file)
                current_dir.children.append(file)
            else:  # It's a directory
                dir = Directory(dir_or_file)
                current_dir.children.append(dir)
                i = organize(emmet_string, dir, i + 1) - 1  # Recurse into the new directory
            
            dir_or_file = ""
        
        elif ch == "+":  # Create a sibling file or directory
            if "." in dir_or_file:  # It's a file
                file = File(dir_or_file)
                current_dir.children.append(file)
            else:  # It's a directory
                dir = Directory(dir_or_file)
                current_dir.children.append(dir)
            dir_or_file = ""
        
        else:  # Build the name of the directory or file
            dir_or_file += ch
        
        i += 1
    
    # Handle the final element in the string if needed
    if dir_or_file:
        if "." in dir_or_file:  # It's a file
            file = File(dir_or_file)
            current_dir.children.append(file)
        else:  # It's a directory
            dir = Directory(dir_or_file)
            current_dir.children.append(dir)

    return i


# Function to create directories and files on the filesystem
def create_filesystem_structure(directory: Directory, path: str = ".") -> None:
    # Don't create root directory, start directly
    for child in directory.children:
        if isinstance(child, Directory):
            current_path = os.path.join(path, child.name)
            os.makedirs(current_path, exist_ok=True)  # Create directory
            create_filesystem_structure(child, current_path)
        elif isinstance(child, File):
            file_path = os.path.join(path, child.name)
            with open(file_path, 'w') as f:
                pass  # Create empty file


# Main entry point: Read the Emmet-like string from the command-line arguments
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: dirgen <emmet-like structure>")
        sys.exit(1)

    emmet_structure = sys.argv[1]

    # Parse and create the directory structure
    root = Directory("")
    organize(emmet_structure, root)

    # Now create the actual directories and files
    create_filesystem_structure(root)
    root.display()
