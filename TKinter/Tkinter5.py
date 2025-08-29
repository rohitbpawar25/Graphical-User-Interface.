# Tkinter Example with Labels Positioned Using Pack

# Step 1 Import Tkinter
from tkinter import *

# Step 2 GUI Interaction
window = Tk()

# Step 3 Adding Input
window.title("simple")
window.geometry("500x700")

label1 = Label(window, text="Label-1", bg="red", fg="white")
label2 = Label(window, text="Label-2", bg="blue", fg="white")
label3 = Label(window, text="Label-3", bg="green", fg="white")

label1.pack(side=TOP, fill=X, expand=False)
label2.pack(side=LEFT, fill=Y, expand=False)
label3.pack(side=RIGHT, fill=Y, expand=False)

# Step 4 Main Loop
window.mainloop()
