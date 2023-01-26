import pandas as pd 


# LENDO E TRATANDO PLANILHA .XLSX

# 1° Lendo planilha salva localmente (poderia ser uma planilha online via API Google Sheets);
# 2° Declarando listas vazias que receberão os dados filtrados;
# 3° Junção de laço For e List Comprehension para percorrer e transformar cada linha da planilha em uma lista;
# 4° Procurando em cada linha pelo valor 'NaN = not a number' contido em uma posição específica na lista (correspondente a posição da coluna 8) e o adicionamos à lista previamente declarada;
# 5° Os dados filtrados serão convertidos em um Data Frame e posteriormente em uma nova planilha xslx.


df = pd.read_excel(r'C:\PASTA_ORIGEM\EXCEL.XLSX')

list_linhas = []
list_final = []
list_colunas = [df.loc[0]]

for x in range(len(df)):
    linha = [x for x in df.loc[x]]
    list_linhas.append(linha)

for y in range(len(df)):
    email = str(list_linhas[y][8])

    if email == 'nan':
        list_final.append(list_linhas[y])

df2 = pd.DataFrame(list_final, columns=list_colunas)
df2.to_excel(r'C:\PASTA_DESTINO\NOVO_EXCEL.XLSX')
