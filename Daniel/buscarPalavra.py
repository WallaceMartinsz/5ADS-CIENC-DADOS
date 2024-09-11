import json

# Função para verificar se a palavra existe em um arquivo JSON
def verificar_palavra_json(caminho_arquivo_json, palavra):
    try:
        # Abrir e carregar o arquivo JSON
        with open(caminho_arquivo_json, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        
        # Função recursiva para procurar a palavra em todos os valores do JSON
        def buscar_palavra(dados, palavra):
            if isinstance(dados, dict):
                for chave, valor in dados.items():
                    if buscar_palavra(valor, palavra):
                        return True
            elif isinstance(dados, list):
                for item in dados:
                    if buscar_palavra(item, palavra):
                        return True
            elif isinstance(dados, str):
                if palavra.lower() in dados.lower():
                    return True
            return False

        # Verifica se a palavra está no JSON
        if buscar_palavra(dados, palavra):
            print(f"A palavra '{palavra}' foi encontrada no arquivo JSON.")
        else:
            print(f"A palavra '{palavra}' não foi encontrada no arquivo JSON.")
    
    except FileNotFoundError:
        print("Arquivo JSON não encontrado.")
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")

# Exemplo de uso:
# Upload do arquivo JSON
from google.colab import files
uploaded = files.upload()

# Nome do arquivo (modifique para o nome correto do seu arquivo JSON)
nome_arquivo = list(uploaded.keys())[0]

# Solicita que o usuário digite a palavra a ser procurada
palavra_a_procurar = input("Digite a palavra que deseja procurar: ")

# Verificar a palavra no arquivo JSON
verificar_palavra_json(nome_arquivo, palavra_a_procurar)
