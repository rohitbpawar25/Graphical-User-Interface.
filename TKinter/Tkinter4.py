# Tkinter Grid Layout Example with Email and Password Fields

# Step 1 Import Tkinter
from tkinter import *

# Step 2 GUI Interaction
window = Tk()

# Step 3 Adding Input
window.title("simple")
window.geometry("250x50")

label1 = Label(window, text="mail")
label2 = Label(window, text="password")

e1 = Entry(window, width=40, borderwidth=5)
e2 = Entry(window, width=40, borderwidth=5)

label1.grid(row=0, column=1)
label2.grid(row=1, column=1)

e1.grid(row=0, column=2)
e2.grid(row=1, column=2)

# Step 4 Main Loop
window.mainloop()
