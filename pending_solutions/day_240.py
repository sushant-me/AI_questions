from tkinter import Tk, Label, Entry, Button

def login():
    username = username_entry.get()
    password = password_entry.get()
    # Perform login validation here
    print(f"Logging in with username: {username}, password: {password}")

# Create the main window
root = Tk()
root.title("Login Form")

# Create username label and entry
username_label = Label(root, text="Username:")
username_label.pack()
username_entry = Entry(root)
username_entry.pack()

# Create password label and entry
password_label = Label(root, text="Password:")
password_label.pack()
password_entry = Entry(root, show="*")
password_entry.pack()

# Create login button
login_button = Button(root, text="Login", command=login)
login_button.pack()

# Run the application
root.mainloop()