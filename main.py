import tkinter as tk
from tkinter import ttk
import ttkboostrap as ttk
import math

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.attributes('-fullscreen', True)  # Tela cheia
        self.root.bind("<Escape>", lambda e: self.root.attributes('-fullscreen', False))  # Sair do modo tela cheia com Esc

        self.expression = ""
        
        # Estilo Moderno com suporte a modo claro e escuro
        self.style = ttk.Style()
        self.style.theme_use("superhero")  # Modo escuro por padrão

        # Alternar entre modo claro e escuro
        self.root.bind("<F1>", self.toggle_theme)
        self.create_widgets()

    def toggle_theme(self, event=None):
        current_theme = self.style.theme_use()
        new_theme = "flatly" if current_theme == "superhero" else "superhero"
        self.style.theme_use(new_theme)

    def create_widgets(self):
        # Campo de exibição
        self.display = ttk.Entry(self.root, font=("Arial", 20), justify="right")
        self.display.pack(fill="both", padx=10, pady=10, ipady=10)

        # Botões da Calculadora
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('C', '0', '=', '+'),
            ('sin', 'cos', 'tan', '√')
        ]
        
        frame = ttk.Frame(self.root)
        frame.pack()

        for row in buttons:
            row_frame = ttk.Frame(frame)
            row_frame.pack(side="top", fill="both")

            for btn_text in row:
                btn = ttk.Button(row_frame, text=btn_text, padding=10, width=5, command=lambda b=btn_text: self.on_button_click(b))
                btn.pack(side="left", expand=True, fill="both")

    def on_button_click(self, button):
        if button == "=":
            try:
                result = eval(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
                self.expression = ""
        elif button == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        elif button == "√":
            try:
                result = math.sqrt(float(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
        elif button in ["sin", "cos", "tan"]:
            try:
                angle = math.radians(float(self.expression))
                result = getattr(math, button)(angle)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.expression = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Erro")
        else:
            self.expression += button
            self.display.insert(tk.END, button)

# Iniciar a calculadora
if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    app = Calculadora(root)
    root.mainloop()
