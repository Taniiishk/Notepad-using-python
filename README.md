# Notepad Application

## Overview
This is an implementation of a Notepad application with a basic editor in Python using Tkinter. This application supports the most basic file operations-these include creating a new file, opening an existing file, saving the current file, and has an edit menu functionality that includes cutting, copying, pasting, and selecting all along with a help menu in which an online link to help is attached and also includes an about section that displays the text contents inside the text file.

## Features
 - **Create a new file **
 - **Open a file **
 - **Save the current file **
 - **Cut, copy, and paste text **
 - **Select all text **
 - **Link in the Help menu to an online resource **
 - **About which it displays information about a text file **

## Setup
1. Verify that you have Python installed on your computer.
2. If Tkinter has not yet been installed, download it. Tkinter is included with Python standard distribution but is an optional in some installations so it may not be present.

## Running
1. Save the `notepad.py` script in your desired directory.
2. In the same directory, create an `about.txt` file with whatever information you want to show.
3. Open a terminal or command prompt.
4. Navigate over to the folder where you copied the script.
5. Run the script using the following command: `python notepad.py`

## Usage
  - **File Menu:**
  - **New file:** Clears the text editor to start a new file.
  - **Open:** Opens a file dialog to select and open a text file.
  - **Save:** Saves the content that is being edited in the text editor to a file.
  - **Exit:** This is the exit application button.
  - **Edit Menu:**
  - **Cut:** Removes the selected text.
  - **Copy:** Copies the selected text.
  - **Paste:** Pastes in the clipboard.
  - **Select All:** Selects all of the text in the text editor.
  - **Help Menu:**
  - Help: A web link to an online help source.
  - About: Opens the `about.txt` file and its contents in the text editor.

## Requirements
- The `tkinter` library
- The `webbrowser` library

## License
Open source and free.


