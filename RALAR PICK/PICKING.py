import pyautogui
import time
import pandas as pd 

caminho = r"//depo0903/gpa$/PAC/Daniel Menezes/Python/RALAR PICK/ralar.xlsx"
ler = pd.read_excel(caminho)
tabela = pd.DataFrame(ler)
print (tabela)

y = 1
x = 0


while True:
    
    plu = tabela.iloc[x, y]
    rua = tabela.iloc[x, y + 2]
    print (plu)
    print (rua)
    time.sleep(2)
    pyautogui.doubleClick(558, 192)
    time.sleep(2)
    pyautogui.hotkey("backspace")
    time.sleep(2)
    pyautogui.write(str(rua))
    time.sleep(2)
    pyautogui.leftClick(1105, 192)
    time.sleep(2)
    pyautogui.leftClick(32, 292)
    time.sleep(2)
    pyautogui.leftClick(1117, 707)
    time.sleep(2)
    pyautogui.leftClick(77, 302)
    time.sleep(2)
    pyautogui.leftClick(679, 700)
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.leftClick(19, 149)
    x = x + 1 