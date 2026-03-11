from tkinter import Tk, Button, Entry

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = Entry(master, width=25, justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            command = lambda x=button: self.on_button_click(x)
            Button(master, text=button, width=5, command=command).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, 'end')
                self.display.insert(0, str(result))
            except Exception as e:
                self.display.delete(0, 'end')
                self.display.insert(0, 'Error')
        else:
            self.display.insert('end', char)

if __name__ == '__main__':
    root = Tk()
    app = Calculator(root)
    root.mainloop()