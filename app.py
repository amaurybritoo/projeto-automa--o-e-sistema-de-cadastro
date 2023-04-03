import pyautogui
from time import sleep


# ABRIR A PASTA
pyautogui.doubleClick(2032,134, duration=1)

# SELECIONAR O APP
pyautogui.doubleClick(2406,192, duration=1)

# CLICAR EM CRIAR NOVO USUARIO
pyautogui.click(952,598, duration=1)

# ESCREVER NOME DE LOGIN
pyautogui.click(951,545, duration=0.01)
pyautogui.write('amaury')

# ESCREVER SENHA
pyautogui.click(964,569, duration=0.5)
pyautogui.write('amaurybrito')

# REGISTRAR NOVO USUARIO
pyautogui.click(902,596, duration=0.5)

# 1 - CLICAR E DIGITAR MEU USUARIO
pyautogui.click(1002,540, duration=0.5)
pyautogui.write('amaury')

# 2 - CLICAR E DIGITAR MINHA SENHA
pyautogui.click(964,569, duration=0.5)
pyautogui.write('amaurybrito')

# 3 - CLICAR EM 'ENTRAR'
pyautogui.doubleClick(873,597, duration=0.5)

# 4 - EXTRAIR CADA PRODUTO
with open("produtos.txt", 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        # 1 - CLICAR E DIGITAR PRODUTO
        pyautogui.click(685,529, duration=0)
        pyautogui.write(produto)

        # 1 - CLICAR E DIGITAR QUANTIDADE
        pyautogui.click(677,555, duration=0)
        pyautogui.write(quantidade)

        # 1 - CLICAR E DIGITAR PREÇO
        pyautogui.click(672,582, duration=0)
        pyautogui.write(preco)

        # 1 - CLICAR EM REGISTAR
        pyautogui.click(592,743, duration=0)
