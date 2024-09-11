import json

def buscar_palavra(palavra, arquivo_json):
    with open(arquivo_json, 'r') as f:
        dados = json.load(f)

    pilha = [dados]

    palavra_normalizada = palavra.lower()

    while pilha:
        atual = pilha.pop()

        if isinstance(atual, dict):
            pilha.extend(atual.values())
        elif isinstance(atual, list):
            pilha.extend(atual)
        elif isinstance(atual, str):
            if palavra_normalizada in atual.lower():
                return f"A palavra '{atual}' foi encontrada!"

    return f"A palavra '{palavra}' não foi encontrada."

palavra = input("Digite uma palavra para buscar no JSON: ")
resultado = buscar_palavra(palavra, 'example.json')

print(resultado)
