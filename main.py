import tkinter as tk
import customtkinter as ctk
import math
import darkdetect
import os
import sys

# Configuração visual
ctk.set_appearance_mode(darkdetect.theme().lower())

# Cores personalizadas
OPERATOR_COLOR = "#FF6F00"
NUMBER_COLOR = "#2C2C2C"

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("360x540")
        self.root.resizable(False, False)
        self.expressao = ""

        # Display da calculadora
        self.display = ctk.CTkEntry(
            self.root,
            placeholder_text="0",
            placeholder_text_color="#AAAAAA",
            font=("Arial", 24),
            justify="right",
            height=60
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="nsew")

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
                cor = OPERATOR_COLOR if texto in ["÷", "×", "-", "+"] else NUMBER_COLOR
                botao = ctk.CTkButton(
                    self.root,
                    text=texto,
                    font=("Arial", 24),
                    fg_color=cor,
                    text_color="#FFFFFF",
                    hover_color="#FF8800",
                    corner_radius=15,
                    border_width=2,
                    border_color="#000000",
                    command=lambda b=texto: self.ao_clicar(b)
                )
                botao.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")

        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)

    def atualizar_display(self, texto):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, texto)

    def calcular(self, operacao):
        try:
            valor = float(self.expressao.replace(",", "."))
            if operacao == "1/x":
                return 1 / valor
            elif operacao == "x²":
                return valor ** 2
            elif operacao == "³√x":
                return valor ** (1/3)
            elif operacao == "%":
                return valor / 100
        except:
            return "Erro"

    def ao_clicar(self, tecla):
        try:
            if tecla in ["C", "CE"]:
                self.expressao = ""
                self.atualizar_display("")
            elif tecla == "⌫":
                self.expressao = self.expressao[:-1]
                self.atualizar_display(self.expressao)
            elif tecla == "=":
                expressao_formatada = self.expressao.replace("÷", "/").replace("×", "*").replace(",", ".")
                resultado = eval(expressao_formatada)
                resultado_str = str(resultado).replace(".", ",")
                self.expressao = resultado_str
                self.atualizar_display(resultado_str)
            elif tecla in ["1/x", "x²", "³√x", "%"]:
                resultado = self.calcular(tecla)
                resultado_str = str(resultado).replace(".", ",") if resultado != "Erro" else "Erro"
                self.expressao = resultado_str if resultado != "Erro" else ""
                self.atualizar_display(resultado_str)
            elif tecla == "±":
                if self.expressao:
                    if self.expressao.startswith("-"):
                        self.expressao = self.expressao[1:]
                    else:
                        self.expressao = "-" + self.expressao
                    self.atualizar_display(self.expressao)
            elif tecla == ",":
                if "," not in self.expressao:
                    self.expressao += ","
                    self.display.insert(tk.END, ",")
            else:
                self.expressao += tecla
                self.display.insert(tk.END, tecla)
        except:
            self.atualizar_display("Erro")
            self.expressao = ""

if __name__ == "__main__":
    root = ctk.CTk()
    app = Calculadora(root)
    root.mainloop()
