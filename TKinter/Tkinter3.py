# Tkinter Example with Frames and Buttons

from tkinter import *

window = Tk()
window.title("simple")
window.geometry("500x700")
window.config(bg="yellow")

frame1 = Frame(window, width=300, height=300, cursor="dot")
frame2 = Frame(window, width=300, height=300, cursor="dotbox")

button1 = Button(frame1, text="Button1", bg="blue")
button2 = Button(frame2, text="Button2", bg="green")
button3 = Button(frame1, text="Logged", bg="red")

frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)

button1.pack()
button2.pack()
button3.pack()

window.mainloop()
