# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

import pyautogui as py
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Tempo de delay após cada ação do Pyautogui
py.PAUSE = 0.3

# Passo a passo do projeto:
# 1) Entrar no sistema da empresa

chromedriver_path = "C:\\Users\\GUSTAVO\Desktop\\PythonCodigos\\chromedriver"
chrome_exe = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
options = webdriver.ChromeOptions()
# "detach" permite que o navegador fique aberto mesmo que o programa termine
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
driver.maximize_window()
time.sleep(3)

# 2) Fazer login

py.click(x=748, y=409)
py.write("delimagusta55@gmail.com")
py.click(x=744, y=507)
py.write("123455667")
py.press("tab")
py.press("enter")

# 3) Importar a base de dados de produtos

tabela = pd.read_csv("produtos.csv")
print(tabela)


# 4) Cadastrar 1 produto

for linha in tabela.index:
    py.click(x=704, y=296)
    codigo = tabela.loc[linha, "codigo"]
    py.write(str(codigo))

    py.click(x=709, y=388)
    marca = tabela.loc[linha, "marca"]
    py.write(str(marca))

    py.click(x=717, y=494)
    tipo = tabela.loc[linha, "tipo"]
    py.write(str(tipo))

    py.click(x=703, y=583)
    categoria = tabela.loc[linha, "categoria"]
    py.write(str(categoria))

    py.click(x=705, y=687)
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    py.write(str(preco_unitario))

    py.click(x=697, y=785)
    custo = tabela.loc[linha, "custo"]
    py.write(str(custo))

    py.click(x=710, y=883)
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        py.write(str(obs))
    py.press("tab")
    py.press("enter")

    py.scroll(5000)

driver.quit

# 5) Repetir o cadastro para todos os produtos
