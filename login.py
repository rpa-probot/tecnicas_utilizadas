import pyautogui as p
import os


# LOGIN EM SISTEMA DEALER VIA LOCALIZAÇÃO DE IMAGENS

# 1° Encerrando possíveis processos anteriores em aberto;
# 2° Lendo arquivo .txt com nome do usuário e senha do Dealer;
# 3° Inicializando o programa e aguardando o input para começar o processo de login;
# 4° Utilizamos redundâncias na localização das imagens (screenshots) que serão clicadas e/ou preenchidas para minimizar potenciais erros críticos.


def login_sys():

    os.system("taskkill /im xxx.exe")

    credenciais = open('C:\\CAMINHO_ARQUIVO_CREDENCIAIS.txt', 'r')
    chaves = credenciais.readlines()
    credenciais.close()

    usuario = chaves[0][:-1]
    senha = chaves[1]

    os.startfile("C:\\CAMINHO_EXECUTAVEL.exe")
    p.sleep(1)

    ipt_usuario = p.locateCenterOnScreen('C:\\CAMINHO_IMAGEM\\ipt_usuario.png',confidence = 0.95)
    while ipt_usuario == None:
        ipt_senha = p.locateCenterOnScreen('C:\\CAMINHO_IMAGEM\\ipt_senha.png', confidence = 0.95)
    if ipt_usuario != None:
        p.click(ipt_usuario)
        p.typewrite(usuario, interval=.10)
    p.sleep(1)

    ipt_senha = p.locateCenterOnScreen('C:\\CAMINHO_IMAGEM\\ipt_senha.png', confidence = 0.95)
    while ipt_senha == None:
        ipt_senha = p.locateCenterOnScreen('C:\\CAMINHO_IMAGEM\\ipt_senha.png', confidence = 0.95)
    if ipt_senha != None:
        p.click(ipt_senha)
        p.typewrite(senha, interval=.10)
    p.sleep(1)

    btn_login = p.locateCenterOnScreen('C:\\CAMINHO_IMAGEM\\btn_login.png', confidence = 0.95)
    while btn_login != None:
        btn_login = p.locateCenterOnScreen('C:\\CAMINHO_IMAGEM\\btn_login.png', confidence = 0.95)
    if btn_login != None:
        p.click(btn_login)

    return True
