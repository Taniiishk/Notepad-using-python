
import tkinter as tk
from tkinter import Menu, mainloop
from tkinter.filedialog import asksaveasfilename, askopenfilename
import webbrowser

# Function to create a new file
def new_file():
    text_edit.delete("1.0", tk.END)
    root.title("New File - NOTEPAD")

# Function to save the current file
def saving_file():
    file_location = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("text files","*.txt"),["All files","*"]])
    if not file_location:
        return
    with open(file_location,"w") as file_output:
        text=text_edit.get("1.0",tk.END)
        file_output.write(text)
    root.titel(f"My Own Notepad - {file_location}")
    
# Function to open an existing file
def opning_file():
    file_location = askopenfilename(
        filetypes=[("text files","*.txt"),("All files","*.*")])
    if not file_location:
        return
        text_edit.delete(1.0,tk.END)
    with open(file_location,"r") as file_input:
        text = file_input.read()
        text_edit.insert(tk.END, text)
    root.title(f"MY OWN NOTEPAD - {file_location}")
    
# Function to cut text
def cut():
    text_edit.event_generate("<<Cut>>")
    
# Function to copy text
def copy():
    text_edit.event_generate("<<Copy>>")
    
# Function to paste text
def paste():
    text_edit.event_generate("<<Paste>>")
    
# Function to select all text
def select_all():
    text_edit.tag_add("sel", "1.0", "end")
    
# Function to open a help link in the web browser
def open_help():
    webbrowser.open("https://github.com/Taniiishk/Notepad-using-python")
    
# Function to show the "About" information by loading content from a text file
def show_about():
    about_file = "about.txt"
    with open(about_file, "r") as file_input:
        text = file_input.read()
        text_edit.delete("1.0", tk.END)
        text_edit.insert(tk.END, text)
    root.title(f"About - NOTEPAD")
    
# Initialize the main window        
root=tk.Tk()
root.title("NOTEPAD")
root.geometry("1920x1080")

# Create a menu bar
menubar=Menu(root)
root.option_add('*Menu*Font', 'Arial 10')

# Add File menu
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=file)
file.add_command(label='New file',command=new_file)
file.add_command(label='open',command=opning_file)
file.add_command(label='Save',command=saving_file)
file.add_separator()
file.add_command(label='Exit',command=root.destroy)

# Add Edit menu
edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=edit)
edit.add_command(label='Cut',command=cut)
edit.add_command(label='Copy',command=copy)
edit.add_command(label='Paste',command=paste)
edit.add_command(label='Slect All',command=select_all)

# Add Help menu
help=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=help)
help.add_command(label='Help',command=open_help)
help.add_separator()
help.add_command(label='About',command=show_about)

# Configure the grid layout to expand the text editor
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create a Text widget and set the font
text_edit = tk.Text(root, font=("Helvetica", 14))
text_edit.grid(row=0, column=0, sticky="nsew")

# Set the menu bar
root.config(menu=menubar)
mainloop()
