import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        # Entry widget to show calculations
        self.entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
        self.entry.grid(row=0, column=0, columnspan=4)
        
        # Buttons for numbers and operations
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]
        
        for (text, row, col) in buttons:
            if text == '=':
                button = tk.Button(self.root, text=text, width=5, height=2, command=self.calculate)
            elif text == 'C':
                button = tk.Button(self.root, text=text, width=5, height=2, command=self.clear)
            else:
                button = tk.Button(self.root, text=text, width=5, height=2, command=lambda t=text: self.button_click(t))
            
            button.grid(row=row, column=col)

    def button_click(self, text):
        current_text = self.entry.get()
        if current_text == 'Error':
            self.entry.delete(0, tk.END)
            current_text = ''
        self.entry.insert(tk.END, text)

    def clear(self):
        self.entry.delete(0, tk.END)

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, 'Error')

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
