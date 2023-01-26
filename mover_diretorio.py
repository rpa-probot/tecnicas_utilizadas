import os
import shutil


# Alterando diretório de arquivo via API's (OS, Shutil)

# 1° Listar todos os arquivos presentes em um diretório definido;
# 2° Os organizar baseado na data/horário da última modificação;
# 3° Capturar o último arquivo modificado para o transferir de diretório.


def move_dir():

    caminho = f'C:\\Users\\{os.getlogin()}\\PASTA_ORIGEM'
    pasta_destino = r'C:\PASTA_DESTINO'
    lista_arquivos = os.listdir(caminho)

    lista_datas = []

    for arquivo in lista_arquivos:
        data = os.path.getmtime(f'{caminho}\\{arquivo}')
        lista_datas.append((data, arquivo))

    lista_datas.sort(reverse=True)
    ultimo_arquivo = lista_datas[0][1]
    pasta_origem = f'{caminho}\\{ultimo_arquivo}'
    shutil.move(pasta_origem, pasta_destino)

    return True
