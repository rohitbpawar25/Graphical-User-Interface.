# ------------------------------
# Simple GUI Calculator using Tkinter
# ------------------------------
# This program creates a basic calculator GUI using Python's Tkinter module.
# It performs addition, subtraction, multiplication, and division on two numbers.
# ------------------------------

from tkinter import *

# Create main application window
window = Tk()
window.geometry("500x500")
window.title("Simple Calculator")  # Optional: Set window title

# Entry widget to display numbers and results
e = Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

# Function to handle number button clicks
def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

# Number Buttons (0–9)
b1 = Button(window, text="1", width=12, command=lambda: click(1))
b1.place(x=10, y=60)

b2 = Button(window, text="2", width=12, command=lambda: click(2))
b2.place(x=80, y=60)

b3 = Button(window, text="3", width=12, command=lambda: click(3))
b3.place(x=170, y=60)

b4 = Button(window, text="4", width=12, command=lambda: click(4))
b4.place(x=10, y=120)

b5 = Button(window, text="5", width=12, command=lambda: click(5))
b5.place(x=80, y=120)

b6 = Button(window, text="6", width=12, command=lambda: click(6))
b6.place(x=170, y=120)

b7 = Button(window, text="7", width=12, command=lambda: click(7))
b7.place(x=10, y=180)

b8 = Button(window, text="8", width=12, command=lambda: click(8))
b8.place(x=80, y=180)

b9 = Button(window, text="9", width=12, command=lambda: click(9))
b9.place(x=170, y=180)

b0 = Button(window, text="0", width=12, command=lambda: click(0))
b0.place(x=10, y=240)

# Function for Addition
def Add():
    n1 = e.get()
    global math
    math = "Addition"
    global i 
    i = int(n1)
    e.delete(0, END)

b_plus = Button(window, text="+", width=12, command=Add)
b_plus.place(x=80, y=240)

# Function for Subtraction
def Sub():
    n1 = e.get()
    global math
    math = "Subtraction"
    global i 
    i = int(n1)
    e.delete(0, END)

b_minus = Button(window, text="-", width=12, command=Sub)
b_minus.place(x=170, y=240)

# Function for Multiplication
def Mul():
    n1 = e.get()
    global math
    math = "Multiplication"
    global i 
    i = int(n1)
    e.delete(0, END)

b_mul = Button(window, text="*", width=12, command=Mul)
b_mul.place(x=10, y=300)

# Function for Division
def Div():
    n1 = e.get()
    global math
    math = "Division"
    global i 
    i = int(n1)
    e.delete(0, END)

b_div = Button(window, text="/", width=12, command=Div)
b_div.place(x=80, y=300)

# Function for Equal (=)
def Equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "Addition":
        e.insert(0, i + int(n2))
    elif math == "Subtraction":
        e.insert(0, i - int(n2))
    elif math == "Multiplication":
        e.insert(0, i * int(n2))
    elif math == "Division":
        if int(n2) != 0:
            e.insert(0, i / int(n2))
        else:
            e.insert(0, "Error")

b_eq = Button(window, text="=", width=12, command=Equal)
b_eq.place(x=170, y=300)

# Function to Clear Entry Box
def clear():
    e.delete(0, END)

b_clear = Button(window, text="Clear", width=12, command=clear)
b_clear.place(x=10, y=350)

# Start GUI loop
mainloop()


'''
# ------------------------------
# Simple GUI Calculator using Tkinter (Compact Version)
# ------------------------------

from tkinter import *

# Setup main window
window = Tk()
window.geometry("500x500")
window.title("Simple Calculator")

# Entry widget
e = Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

# Handle number clicks
def click(num):
    e.insert(END, str(num))

# Math operation handlers
def operate(op):
    global i, math
    i = int(e.get())
    math = op
    e.delete(0, END)

def equal():
    n2 = int(e.get())
    e.delete(0, END)
    try:
        result = {
            "add": i + n2,
            "sub": i - n2,
            "mul": i * n2,
            "div": i / n2 if n2 != 0 else "Error"
        }[math]
        e.insert(0, result)
    except:
        e.insert(0, "Error")

def clear():
    e.delete(0, END)

# Button config: (text, x, y, command)
buttons = [
    ("1", 10, 60), ("2", 80, 60), ("3", 170, 60),
    ("4", 10, 120), ("5", 80, 120), ("6", 170, 120),
    ("7", 10, 180), ("8", 80, 180), ("9", 170, 180),
    ("0", 10, 240),
    ("+", 80, 240, lambda: operate("add")),
    ("-", 170, 240, lambda: operate("sub")),
    ("*", 10, 300, lambda: operate("mul")),
    ("/", 80, 300, lambda: operate("div")),
    ("=", 170, 300, equal),
    ("Clear", 10, 350, clear)
]

# Create buttons dynamically
for btn in buttons:
    text, x, y = btn[0], btn[1], btn[2]
    cmd = btn[3] if len(btn) == 4 else lambda t=text: click(t)
    Button(window, text=text, width=12, command=cmd).place(x=x, y=y)

# Start GUI
mainloop()




'''