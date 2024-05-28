import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os

# Initialize the main window
root = tk.Tk()
root.title("MyCalculator")
root.geometry("400x450+400+100")
root.configure(bg="dark grey")

# Create a frame to hold all the widgets and center it
frame = Frame(root, bg="dark grey")
frame.pack(expand=True)

# Global variables
textin = StringVar()
operator = ""

# Function to handle button clicks and key presses
def clickbut(number):
    global operator
    operator = operator + str(number)
    textin.set(operator)

# Function to handle the equal button click and Enter key press
def equalbut(event=None):
    global operator
    try:
        result = str(eval(operator))
        textin.set(result)
        operator = ''
    except:
        textin.set("Error")
        operator = ''

# Function to clear the entry field and handle Escape key press
def clrbut(event=None):
    global operator
    operator = ''
    textin.set('')

# Bind keyboard input to corresponding functions
root.bind('0', lambda event: clickbut(0))
root.bind('1', lambda event: clickbut(1))
root.bind('2', lambda event: clickbut(2))
root.bind('3', lambda event: clickbut(3))
root.bind('4', lambda event: clickbut(4))
root.bind('5', lambda event: clickbut(5))
root.bind('6', lambda event: clickbut(6))
root.bind('7', lambda event: clickbut(7))
root.bind('8', lambda event: clickbut(8))
root.bind('9', lambda event: clickbut(9))
root.bind('<Return>', equalbut)  # Enter key
root.bind('<Escape>', clrbut)   # Escape key
root.bind('+', lambda event: clickbut('+'))
root.bind('-', lambda event: clickbut('-'))
root.bind('*', lambda event: clickbut('*'))
root.bind('/', lambda event: clickbut('/'))

# Entry widget for displaying the input and output
metext = Entry(frame, font=("Arial", 12, "bold"), textvariable=textin, width=25, bd=10, insertwidth=2, bg="#e8b5ce")
metext.grid(columnspan=4, pady=10)

# Button creation and placement
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

buttons = []

# Create buttons dynamically
for i, text in enumerate(button_texts):
    if text == 'C':
        button = Button(frame, padx=16, pady=16, bd=8, fg="black", font=("Arial", 12, "bold"),
                        text=text, bg="#c2b5e8", command=clrbut)
    elif text == '=':
        button = Button(frame, padx=16, pady=16, bd=8, fg="black", font=("Arial", 12, "bold"),
                        text=text, bg="#c2b5e8", command=equalbut)
    else:
        button = Button(frame, padx=16, pady=16, bd=8, fg="black", font=("Arial", 12, "bold"),
                        text=text, bg="#c2b5e8", command=lambda t=text: clickbut(t))
    
    buttons.append(button)
    button.grid(row=i//4+1, column=i%4, padx=5, pady=5)

root.resizable(False, False)
root.mainloop()
