# Tkinter Message Widget with Dynamic Text from Entry

# Step 1 Import Tkinter
from tkinter import *

# Step 2 GUI Interaction
window = Tk()

# Step 3 Adding Input

'''
window.geometry("500x500")
message = Message(window,text = "Python")
message.pack()
'''

'''
var = StringVar()
message = Message(window,textvariable=var,relief=RAISED)
var.set("Welcome")
message.pack()
'''

var = StringVar()
ent_var = StringVar()

def insert():
    result = ent_var.get()
    var.set(result)

message = Message(window, textvariable=var, relief=RAISED, padx=50, pady=50)
entry = Entry(window, textvariable=ent_var)
button = Button(window, text="ok", command=insert)
message.pack()
entry.pack()
button.pack()

# Step 4 Main Loop
mainloop()
