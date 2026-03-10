# Igor Terplak: wkyouma, Gabriel Antony: misfasol, Kevin Henriques: kevinhag, Patrick Froes: PatrickFroes
#Grupo: X


import json

#Função parseExpressao: faz a análise da expressão e validação da sintaxe, retorna lista de tokens se expressão válida
def parseExpressao(linhas):
    tokens = []
    i = 0
    
    while i < len(linhas):
        # Ignora espaços
        if linhas[i].isspace():
            i += 1
            continue
        
        # Parênteses
        if linhas[i] in '()':
            token, i = estadoParenteses(linhas, i)
            tokens.append(token)
            continue
        
        # Números
        if linhas[i].isdigit() or (linhas[i] == '.' and i + 1 < len(linhas) and linhas[i + 1].isdigit()):
            token, i = estadoNumero(linhas, i)
            tokens.append(token)
            continue
        
        # Operadores
        if linhas[i] in '+-*/%^':
            token, i = estadoOperador(linhas, i)
            tokens.append(token)
            continue
        
        # Identificadores (letras maiúsculas)
        if linhas[i].isalpha():
            j = i
            while j < len(linhas) and linhas[j].isalpha():
                j += 1
            token = linhas[i:j]
            if not token.isupper():
                raise ValueError(f"Identificador deve ser maiúsculo: {token}")
            tokens.append(token)
            i = j
            continue
        
        raise ValueError(f"Caractere inválido: '{linhas[i]}'")
    
    if not validar_parenteses(tokens):
        raise ValueError("Parênteses desbalanceados")
    
    return tokens

#Função para estado de numero na maquina de estados
#retorno é o token número e a posição do próximo caractere
def estadoNumero(linhas, inicio):
    j = inicio
    while j < len(linhas) and (linhas[j].isdigit() or linhas[j] == '.'):
        j += 1
    return linhas[inicio:j], j

#Função para estado de operador na maquina de estados
#retorno é o token operador e a posição do próximo caractere
def estadoOperador(linhas, inicio):
    if linhas[inicio:inicio+2] == '//':
        return '//', inicio + 2
    else:
        return linhas[inicio], inicio + 1

#Função para estado de parênteses na maquina de estados
#retorno é o token parêntese e a posição do próximo caractere
def estadoParenteses(linhas, inicio):
    return linhas[inicio], inicio + 1

#Função para validar se os parênteses estão balanceados
def validar_parenteses(tokens):
    cont = 0
    for token in tokens:
        if token == '(':
            cont += 1
        elif token == ')':
            cont -= 1
            if cont < 0:
                return False
    return cont == 0

#Função para salvar tokens em arquivo JSON
def salvar_tokens(tokens_lista, nome_arquivo='tokens_ultimos.txt'):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(tokens_lista, f, indent=2, ensure_ascii=False)



