"""
Build file explorer GUI.
"""

import os
from tkinter import Tk, Treeview, Scrollbar, Button, Label, END

def build_tree(parent, path):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            node = parent.insert("", END, text=entry, open=False)
            build_tree(node, full_path)

def on_select(event):
    selected_item = tree.selection()[0]
    file_path = os.path.join(root_path, tree.item(selected_item, "text"))
    if os.path.isfile(file_path):
        label.config(text=f"Selected File: {file_path}")

root = Tk()
root.title("File Explorer")

root_path = "/path/to/root"
tree = Treeview(root)
tree.pack(side="left", fill="both", expand=True)

scrollbar = Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

build_tree(tree, root_path)

button = Button(root, text="Open Selected", command=lambda: os.startfile(tree.item(tree.selection()[0], "text")))
button.pack(side="bottom")

label = Label(root, text="Selected File: None")
label.pack(side="bottom")

tree.bind("<<TreeviewSelect>>", on_select)

root.mainloop()