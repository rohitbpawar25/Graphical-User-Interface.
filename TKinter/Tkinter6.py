# Simple Tkinter Login Button Example

# Step 1 Import Tkinter
from tkinter import *

# Step 2 GUI Interaction
window = Tk()

# Step 3 Adding Input
window.title("simple")
window.geometry("500x500")

def Log_entry():
    print("Loged In")  # Corrected "Loged" to "Logged"

button = Button(window, text="LOGIN", command=Log_entry, width=12, bg="red", fg="white",
                font=("bold", 12), activebackground="black", activeforeground="white")
button.pack()

# Step 4 Main Loop
mainloop()
