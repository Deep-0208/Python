import tkinter as tk
from tkinter import messagebox

def clicked():
    label.config(text="Button Clicked!")

def show_input():
    print("Entry Input:", entry.get())

def get_text():
    print("Text Area Content:", text.get("1.0", tk.END).strip())

def show_alert():
    messagebox.showinfo("Alert", "This is a message box!")

root = tk.Tk()
root.title("Tkinter learning")
root.geometry("300x300")

label = tk.Label(root, text="Hello World!", font=("Arial", 14))
label.pack()

text = tk.Text(root, height=5, width=30)
text.pack()

btn4 = tk.Button(root, text="Show Text", command=get_text)
btn4.pack()

entry = tk.Entry(root)
entry.pack()

btn3 = tk.Button(root, text="Show Entry", command=show_input)
btn3.pack()

check_var = tk.IntVar()
check = tk.Checkbutton(root, text="Accept", variable=check_var, command=show_input)
check.pack()

btn = tk.Button(root, text="Click Me", command=clicked)
btn.pack()

radio_var = tk.StringVar()
tk.Radiobutton(root, text="Male", value="Male", variable=radio_var).pack()
tk.Radiobutton(root, text="Female", value="Female", variable=radio_var).pack()

listbox = tk.Listbox(root)
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.pack()

canvas = tk.Canvas(root, width=200, height=100, bg="lightblue")
canvas.pack()
canvas.create_rectangle(20, 20, 150, 70, fill="yellow")


tk.Button(root, text="Show Alert", command=show_alert).pack()

btn2 = tk.Button(root, text="Stop", command=root.destroy)
btn2.pack()
tk.Label(root, text="Place Example").place(x=0, y=100)

root.mainloop()
