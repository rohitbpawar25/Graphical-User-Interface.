# Tkinter Messagebox Example: Error and Ask Question Dialogs

# Step 1 Import Tkinter
from tkinter import *
import tkinter.messagebox

# Step 2 GUI Interaction
window = Tk()

# Step 3 Adding Input
tkinter.messagebox.showerror("Info", "Running Out Time")
question = tkinter.messagebox.askokcancel("Weather", "Will it Rain")

if question == True:
    print("Take an Umbrella")
else:
    print("Okay")

# Step 4 Main Loop
mainloop()
