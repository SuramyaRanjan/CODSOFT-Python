import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os
import os
import sys
from PIL import Image

def resource_path(relative_path):
    
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root = tk.Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.configure(bg="#75cb97")

task_list = []
task_counter = 0  

def addTask():
    global task_counter
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        task_counter += 1
        task_with_number = f"{task_counter}. {task}"
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"{task_with_number}\n")
        task_list.append(task_with_number)
        listbox.insert(END, task_with_number)

def deleteTask():
    global task_list, task_counter
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for i, task in enumerate(task_list, start=1):
                task_with_number = f"{i}. {task.split('. ', 1)[1]}"
                taskfile.write(task_with_number + "\n")
        listbox.delete(ANCHOR)
        task_counter = len(task_list)  

def openTaskFile():
    global task_list, task_counter
    try:
        with open("ToDoPy/tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task.strip():
                task_list.append(task.strip())
                listbox.insert(END, task.strip())
        task_counter = len(task_list)  
    except FileNotFoundError:
        with open('tasklist.txt', 'w') as file:
            file.close()
        print("tasklist.txt file created.")
    except Exception as e:
        print(f"An error occurred: {e}")

icon_img = Image.open("ToDoPy/task.png")
icon_img = icon_img.resize((20, 20))  
img1 = ImageTk.PhotoImage(icon_img)


title_frame = Frame(root, bg="#eeeeee")
title_frame.place(x=10, y=10)


icon_label = Label(title_frame, image=img1, bg="#32405b")
icon_label.pack(side=LEFT, padx=5, pady=5)


title_label = Label(title_frame, text="To-Do-List", font=("Arial", 14), fg="white", bg="#32405b")
title_label.pack(side=LEFT)


topbar_img = Image.open("ToDoPy/topabar.jpeg")
topbar_img = topbar_img.resize((400, 85))  
img2 = ImageTk.PhotoImage(topbar_img)


topbar_label = Label(root, image=img2)
topbar_label.place(x=0, y=50)


document_img = Image.open("ToDoPy/document.jpeg")
document_img = document_img.resize((40, 50))  
img3 = ImageTk.PhotoImage(document_img)


document_label = Label(root, image=img3)
document_label.place(x=10, y=68)


note_img = Image.open("ToDoPy/note.jpeg")
note_img = note_img.resize((40, 50))
img4 = ImageTk.PhotoImage(note_img) 


note_label = Label(root, image=img4)
note_label.place(x=330, y=68)


heading = Label(root, text="To Be Done", font="Arial 20 bold", fg="White", bg="#32405b")
heading.place(x=120, y=68)


frame = Frame(root, width=400, height=500, bg="White")
frame.place(x=0, y=180)


task = StringVar()
task_entry = Entry(frame, width=18, font="Arial 20", bg="#b9b9b9", bd=8)
task_entry.place(x=10, y=26)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold ", width=6, height=1, bg="#ffbf00", fg="#fff", bd=5, command=addTask)
button.place(x=280, y=19)


frame1 = Frame(root, bd=3, width=700, height=280, bg="black")
frame1.pack(pady=(160, 0))
frame1.place(x=10, y=270)

listbox = Listbox(frame1, font=('Arial', 12), width=40, height=16, bg="lightblue", fg="black", cursor="hand2", selectbackground="#5a95ff")
listbox.place(x=10, y=270)
listbox.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()


delete_icon_img = Image.open("ToDoPy/delete.jpeg")
delete_icon_img = delete_icon_img.resize((40, 50))
delete_icon = ImageTk.PhotoImage(delete_icon_img)


delete_button = Button(root, image=delete_icon, bd=0, command=deleteTask,bg="red")
delete_button.pack(side=BOTTOM, pady=13)

root.resizable(False, False)
root.mainloop()
