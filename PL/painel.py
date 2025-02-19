import pandas as pd
import pyautogui
import tkinter as tk
import colorsys
root = tk.Tk()
root.title("Cadastro De Equipamentos")

texto = tk.Text(root , height=10 , width= 40)
texto.pack(pady=20) 

def on_button_click():
    texto_digitado = texto.get("1.0", tk.END).strip()
    print(texto_digitado)


botao_1 = tk.Button(root, text = "Enter", command=on_button_click)
botao_1.pack(pady=20)


root.mainloop()