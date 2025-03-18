import tkinter as tk
from tkinter import messagebox
from Pila import Pilas
from infix_to_posfix import infix2posfix
from Pos2Valor import pos2Value
import math

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.trig_inverse = False  # Modo para funciones trigonométricas inversas
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
            ('pi', 5, 0), ('sqrt', 5, 1),('ln',5,2), ('(', 5, 3), (')', 5,4), 
            ('=', 6, 4),
        ]

        self.buttons = {}

        for text, row, col in self.button_texts:
            action = lambda t=text: self.on_button_click(t)
            self.buttons[text] = tk.Button(self.root, text=text, font=("Arial", 16), width=5, height=2, command=action)
            self.buttons[text].grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        self.trig_button = tk.Button(self.root, text="Inversas", font=("Arial", 14), width=12, height=2, 
                                     command=self.toggle_trig_mode, bg="lightgray")
        self.trig_button.grid(row=6, column=0, columnspan=5, pady=10)

    def on_button_click(self, button):
        if button == "C":
            self.expression = ""
        elif button == "=":
            try:
                # Convert to postfix and evaluate
                postfix_expr = infix2posfix(self.expression)  
                self.expression = str(pos2Value(postfix_expr))  
            except Exception:
                messagebox.showerror("Error", "Expresión inválida")
                self.expression = ""
        else:
            # Correct inverse trig functions in input
            if self.trig_inverse and button in ["sin", "cos", "tan","log","ln"]:
                button = "a" + button  # Change "sin" → "asin", etc.

            self.expression += button  # Append to expression

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)


    def toggle_trig_mode(self):
        self.trig_inverse = not self.trig_inverse

        if self.trig_inverse:
            self.buttons["sin"].config(text="asin")
            self.buttons["cos"].config(text="acos")
            self.buttons["tan"].config(text="atan")
            self.buttons["log"].config(text="alog")
            self.buttons["ln"].config(text="aln")
            
            self.trig_button.config(bg="lightblue")  # Indicar modo inverso
        else:
            self.buttons["sin"].config(text="sin")
            self.buttons["cos"].config(text="cos")
            self.buttons["tan"].config(text="tan")
            self.buttons["log"].config(text="log")
            self.buttons["ln"].config(text="ln")

            self.trig_button.config(bg="lightgray")  # Restaurar color


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
