import json

def inserir_json(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

def extrair_texto(dados):
   
    textos = []
    
    if isinstance(dados, dict):
        for valor in dados.values():
            textos.append(extrair_texto(valor))
    elif isinstance(dados, list):
        for item in dados:
            textos.append(extrair_texto(item))
    elif isinstance(dados, str):
        textos.append(dados)
    
 
    return ' '.join(textos)

def pesquisar_palavra(texto, palavra):
    ocorrencias = []
    texto_normalizado = texto.lower()
    palavra_normalizada = palavra.lower()
    
    indice = texto_normalizado.find(palavra_normalizada)
    
    while indice != -1:
        ocorrencias.append((palavra, indice))
        indice = texto_normalizado.find(palavra_normalizada, indice + 1)

    return ocorrencias


caminho_arquivo = r'C:\Users\Pichau\Documents\NASSAU\5periodo\Cienc_de_Dados\git\5ADS-CIENC-DADOS\Gabriel\db.json'  
palavra_procurada = input("Insira a palavra a ser procurada: ")   


dados_json = inserir_json(caminho_arquivo)


texto = extrair_texto(dados_json)


resultados = pesquisar_palavra(texto, palavra_procurada)


print(f"A palavra '{palavra_procurada}' foi encontrada {len(resultados)} vezes:")
for palavra, indice in resultados:
    print(f"- '{palavra}' encontrada no índice {indice}") 
