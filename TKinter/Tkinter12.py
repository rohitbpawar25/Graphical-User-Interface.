# Tkinter Button Positioned Using place() Geometry Manager

# Step 1 Import Tkinter
from tkinter import *

# Step 2 GUI Interaction
window = Tk()

# Step 3 Adding Input
window.geometry("500x500")

button = Button(window, text="Button", width=12)
button.place(x=200, y=200)

# Step 4 Main Loop
mainloop()
