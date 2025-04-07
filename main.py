import tkinter as tk
import customtkinter as ctk
import math



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("black")


class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Moderna")
        self.root.geometry("360x540")
        self.root.resizable(False, False)
        self.expression = ""

        self.display = ctk.CTkEntry(self.root, font=("Arial", 24), justify="right", height=60)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="nsew")

        # Layout em grid com sombra simulada
        botoes = [
            ["%", "CE", "C", "⌫"],
            ["1/x", "x²", "³√x", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["±", "0", ",", "="],
        ]

        for i, linha in enumerate(botoes):
            for j, texto in enumerate(linha):
                # Botão "0" ocupa duas colunas
                colspan = 2 if texto == "0" else 1
                width = 170 if texto == "0" else 80

                btn = ctk.CTkButton(
                    self.root,
                    text=texto,
                    width=width,
                    height=60,
                    corner_radius=10,
                    font=("Arial", 18),
                    command=lambda b=texto: self.on_button_click(b)
                )
                btn.grid(row=i + 1, column=j if texto != "0" else 1, columnspan=colspan, padx=4, pady=4, sticky="nsew")

        # Ajuste das colunas para preencher a tela
        for col in range(4):
            self.root.grid_columnconfigure(col, weight=1)
        for row in range(7):
            self.root.grid_rowconfigure(row, weight=1)

    def on_button_click(self, button):
        try:
            if button == "C":
                self.expression = ""
                self.display.delete(0, tk.END)
            elif button == "⌫":
                self.expression = self.expression[:-1]
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.expression)
            elif button == "=":
                expression = self.expression.replace("÷", "/").replace("×", "*").replace(",", ".")
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result).replace(".", ","))
                self.expression = str(result).replace(".", ",")
            elif button == "±":
                if self.expression:
                    if self.expression.startswith("-"):
                        self.expression = self.expression[1:]
                    else:
                        self.expression = "-" + self.expression
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, self.expression)
            elif button == "1/x":
                result = 1 / float(self.expression.replace(",", "."))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result).replace(".", ","))
                self.expression = str(result).replace(".", ",")
            elif button == "x²":
                result = math.pow(float(self.expression.replace(",", ".")), 2)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result).replace(".", ","))
                self.expression = str(result).replace(".", ",")
            elif button == "³√x":
                result = float(self.expression.replace(",", ".")) ** (1/3)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result).replace(".", ","))
                self.expression = str(result).replace(".", ",")
            elif button == "%":
                result = float(self.expression.replace(",", ".")) / 100
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result).replace(".", ","))
                self.expression = str(result).replace(".", ",")
            elif button == "CE":
                self.display.delete(0, tk.END)
                self.expression = ""
            elif button == ",":
                if "," not in self.expression:
                    self.expression += ","
                    self.display.insert(tk.END, ",")
            else:
                self.expression += button
                self.display.insert(tk.END, button)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Erro")
            self.expression = ""


# Executar app
if __name__ == "__main__":
    root = ctk.CTk()
    app = Calculadora(root)
    root.mainloop()
