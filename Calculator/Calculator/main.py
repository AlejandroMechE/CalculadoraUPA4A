import tkinter as tk
from tkinter import messagebox
import math

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.trig_inverse = False  # Mode toggle for trig functions
        self.expression = ""

        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.root, font=("Arial", 20), bd=10, relief=tk.GROOVE, justify="right")
        self.entry.grid(row=0, column=0, columnspan=8, ipadx=8, ipady=8, pady=10)

        self.button_texts = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sin', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('cos', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('tan', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3), ('log', 4, 4),
            ('pi', 5, 0), ('sqrt', 5, 1), ('(', 5, 2), (')', 5, 3), ('=', 5, 4),
        ]

        self.buttons = {}

        for text, row, col in self.button_texts:
            action = lambda t=text: self.on_button_click(t)
            self.buttons[text] = tk.Button(self.root, text=text, font=("Arial", 16), width=5, height=2,
                                           command=action)
            self.buttons[text].grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Trigonometric Mode Toggle Button
        self.trig_button = tk.Button(self.root, text="Trig Mode", font=("Arial", 14), width=12, height=2, 
                                     command=self.toggle_trig_mode, bg="lightgray")
        self.trig_button.grid(row=6, column=0, columnspan=5, pady=10)

    def on_button_click(self, button):
        if button == "C":
            self.expression = ""
        elif button == "=":
            try:
                self.expression = self.expression.replace("pi", str(math.pi))
                self.expression = self.expression.replace("sqrt", "math.sqrt")
                self.expression = self.expression.replace("log", "math.log10")
                self.expression = self.expression.replace("sin", "math.sin")
                self.expression = self.expression.replace("cos", "math.cos")
                self.expression = self.expression.replace("tan", "math.tan")
                self.expression = self.expression.replace("asin", "math.asin")
                self.expression = self.expression.replace("acos", "math.acos")
                self.expression = self.expression.replace("atan", "math.atan")
                
                # Evaluate and update result
                self.expression = str(eval(self.expression))
            except Exception:
                messagebox.showerror("Error", "Expresión inválida")
                self.expression = ""
        else:
            self.expression += button

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def toggle_trig_mode(self):
        """Switch between normal and inverse trigonometric functions."""
        self.trig_inverse = not self.trig_inverse

        if self.trig_inverse:
            self.buttons["sin"].config(text="asin")
            self.buttons["cos"].config(text="acos")
            self.buttons["tan"].config(text="atan")
            self.trig_button.config(bg="lightblue")  # Change color to indicate inverse mode
        else:
            self.buttons["sin"].config(text="sin")
            self.buttons["cos"].config(text="cos")
            self.buttons["tan"].config(text="tan")
            self.trig_button.config(bg="lightgray")  # Reset color

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
