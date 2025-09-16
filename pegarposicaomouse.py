import pyautogui
from time import sleep
sleep(3)
print(pyautogui.position())
pyautogui.click(x=665, y=535) #Colocar a posicao inicial do mouse aqui (use o arquivo para pegar posicao para auxiliar)
pyautogui.write("emailteste@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhateste123")
pyautogui.press("enter")
sleep(3)

#importar base de dados

import pandas
tabela = pandas.read_csv("produtos.csv")

#registrar produtos

print(tabela)

for linha in tabela.index: #para cada linha da tabela
    pyautogui.click(x=640, y=411)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))

    marca = tabela.loc[linha, "marca"]
    pyautogui.press("tab")
    pyautogui.write(str(marca))

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.press("tab")
    pyautogui.write(str(tipo))

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.press("tab")
    pyautogui.write(str(categoria))

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.press("tab")
    pyautogui.write(str(preco_unitario))

    custo = tabela.loc[linha, "custo"]
    pyautogui.press("tab")
    pyautogui.write(str(custo))

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    
    if obs != "nan":
        pyautogui.write((obs))
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)