# Tkinter Menu Bar Example with File Menu Options

# Step 1 Import Tkinter
from tkinter import *

# Step 2 GUI Interaction
window = Tk()

# Step 3 Adding Input
menu = Menu(window)

file = Menu(menu, tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save As")
file.add_separator()
file.add_command(label="Exit")

menu.add_cascade(label="File", menu=file)
window.config(menu=menu)

# Step 4 Main Loop
mainloop()
