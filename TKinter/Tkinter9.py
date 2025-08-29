# Tkinter Canvas Example with Lines and Rectangle

# Step 1 Import Tkinter
from tkinter import *

# Step 2 GUI Interaction
window = Tk()

# Step 3 Adding Input
C = Canvas(window, width=500, height=500)
C.pack()

C.create_line(0, 0, 500, 500, width=5, fill="green", dash=(3, 3))
C.create_line(0, 500, 500, 0, width=5, fill="blue", dash=(3, 3))
C.create_rectangle(150, 125, 450, 375, fill="red", outline="yellow", width=5)

# Step 4 Main Loop
mainloop()
