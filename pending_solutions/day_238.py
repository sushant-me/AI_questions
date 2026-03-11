"""
Create GUI using Tkinter.
"""

import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Clicked", "Button was clicked!")

root = tk.Tk()
root.title("Tkinter GUI")
root.geometry("300x200")

label = tk.Label(root, text="Hello, Tkinter!", font=("Helvetica", 16))
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

root.mainloop()