# 🗂️ DirGen: Directory and File Generator Magic! 🪄

Welcome to **DirGen**, the script that transforms your dreams of directory structures into reality! ✨ 

## ✨ What Is DirGen?

DirGen lets you create a whole forest of directories and files using a simple syntax! No more manual folder creation—just sit back, relax, and let DirGen do the heavy lifting. 🏋️‍♂️

## 📜 How to Use It

1. **Command Structure**:
   Use the following syntax to create your directory structure (Don't forget quotation mark):
   ```
   dirgen "<structure>"
   ```
   For example:
   ```bash
   dirgen "app>__init__.py+main.py+utils.py+config>settings.py^tests>__init__.py+test_main.py^requirements.txt"
   ```

2. **What Each Symbol Means**:
   - `>`: Create a new directory or file.
   - `+`: Create a sibling directory or file.
   - `^`: Move back to the parent directory.

3. **Example**:
   Running the command above will create:
   ```
   app
   ├── __init__.py
   ├── config
   │   └── settings.py
   ├── main.py
   ├── requirements.txt
   ├── tests
   │   ├── __init__.py
   │   └── test_main.py
   └── utils.py
   ```

## ⚠️ Warnings

- Make sure your structure is well-formed. A missing symbol can lead to unexpected results. Think of it like a treasure map: one wrong turn and you might end up in the Bermuda Triangle! 🏴‍☠️

## 🤔 Questions or Bugs?

If you encounter any bugs, just pretend they don’t exist and they’ll go away! (Just kidding, please report them 😅)

Happy generating! 🌟