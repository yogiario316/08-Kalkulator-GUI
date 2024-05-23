import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Sederhana by Yogi Ario")
        self.root.geometry("400x600")

        self.current_input = ""

        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.display_label = self.create_display_label()

        self.digit_buttons = {}
        self.operator_buttons = {}
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

        # Bind keys to the corresponding functions
        self.bind_keys()

    def create_display_frame(self):
        frame = tk.Frame(self.root, height=100, bg='lightgrey')
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_label(self):
        label = tk.Label(self.display_frame, text="", anchor=tk.E, bg="white", fg="black", padx=24, font=("Arial", 24))
        label.pack(expand=True, fill='both')
        return label

    def create_digit_buttons(self):
        digits = {
            1: (3, 0), 2: (3, 1), 3: (3, 2),
            4: (2, 0), 5: (2, 1), 6: (2, 2),
            7: (1, 0), 8: (1, 1), 9: (1, 2),
            0: (4, 1), ".": (4, 0)
        }

        for digit, grid_value in digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg="white", fg="black", font=("Arial", 18), borderwidth=0, command=lambda x=digit: self.append_to_input(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
            self.digit_buttons[digit] = button

    def create_operator_buttons(self):
        operators = {
            "/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"
        }

        i = 0
        for operator, symbol in operators.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="lightgrey", fg="black", font=("Arial", 18), borderwidth=0, command=lambda x=operator: self.append_to_input(x))
            button.grid(row=i, column=3, sticky=tk.NSEW)
            self.operator_buttons[operator] = button
            i += 1

    def create_special_buttons(self):
        clear_button = tk.Button(self.buttons_frame, text="C", bg="lightgrey", fg="black", font=("Arial", 18), borderwidth=0, command=self.clear_input)
        clear_button.grid(row=0, column=0, sticky=tk.NSEW)

        equals_button = tk.Button(self.buttons_frame, text="=", bg="lightgrey", fg="black", font=("Arial", 18), borderwidth=0, command=self.evaluate_input)
        equals_button.grid(row=4, column=2, columnspan=2, sticky=tk.NSEW)

    def append_to_input(self, value):
        self.current_input += str(value)
        self.update_display_label()

    def clear_input(self):
        self.current_input = ""
        self.update_display_label()

    def evaluate_input(self):
        try:
            self.current_input = str(eval(self.current_input))
            self.update_display_label()
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            self.clear_input()

    def update_display_label(self):
        self.display_label.config(text=self.current_input[:10])

    def bind_keys(self):
        self.root.bind('<Return>', lambda event: self.evaluate_input())
        self.root.bind('<KP_Enter>', lambda event: self.evaluate_input())
        for key in '0123456789':
            self.root.bind(key, lambda event, digit=key: self.append_to_input(digit))
            self.root.bind(f'KP_{key}', lambda event, digit=key: self.append_to_input(digit))
        for key, symbol in {'+': '+', '-': '-', '*': '*', '/': '/'}.items():
            self.root.bind(key, lambda event, operator=symbol: self.append_to_input(operator))
            self.root.bind(f'KP_{key}', lambda event, operator=symbol: self.append_to_input(operator))
        self.root.bind('.', lambda event: self.append_to_input('.'))
        self.root.bind('KP_Decimal', lambda event: self.append_to_input('.'))
        self.root.bind('<BackSpace>', lambda event: self.delete_last_character())

    def delete_last_character(self):
        self.current_input = self.current_input[:-1]
        self.update_display_label()

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)

    for i in range(5):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()
