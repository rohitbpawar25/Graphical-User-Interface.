# Tkinter Checkbutton Example with Multiple Independent Selections

# Step 1 Import Tkinter
from tkinter import *

# Step 2 GUI Interaction
window = Tk()

# Step 3 Adding Input
window.geometry("500x500")

check_box_1 = IntVar()
check_box_2 = IntVar()
check_box_3 = IntVar()

chk_btn_1 = Checkbutton(window, text="Apple", variable=check_box_1, onvalue=1, offvalue=0, height=2, width=10)
chk_btn_2 = Checkbutton(window, text="Mango", variable=check_box_2, onvalue=1, offvalue=0, height=2, width=10)
chk_btn_3 = Checkbutton(window, text="Plum",  variable=check_box_3, onvalue=1, offvalue=0, height=2, width=10)

chk_btn_1.pack()
chk_btn_2.pack()
chk_btn_3.pack()

# Step 4 Main Loop
mainloop()
