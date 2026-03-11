# Igor Terplak: wkyouma, Gabriel Antony: misfasol, Kevin Henriques: kevinhag, Patrick Froes: PatrickFroes
#Grupo: RA1-3

#Função parseExpressao: faz a análise da expressão e retorna lista de tokens
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
            if token and tokens[-1] in '+-*/%^':
                raise ValueError(f"Operadores consecutivos: '{tokens[-1]}' e '{token}'")
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
    
    # Validar parênteses balanceados
    if not validar_parenteses(tokens):
        raise ValueError("Parênteses desbalanceados")
    
    # Validar sintaxe RPN
    valida_rpn(tokens)
    
    return tokens

#Função para estado de numero na maquina de estados
#retorno é o token número e a posição do próximo caractere
def estadoNumero(linhas, inicio):
    j = inicio
    pontos = 0
    while j < len(linhas) and (linhas[j].isdigit() or linhas[j] == '.'):
        if linhas[j] == '.':
            pontos += 1
        j += 1
    if pontos > 1:
        raise ValueError(f"Número inválido: {linhas[inicio:j]}")
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

#Função para salvar tokens em arquivo (função auxiliar para testes)
def salvar_tokens(tokens_lista, nome_arquivo='tokens_ultimos.txt'):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        for token in tokens_lista:
            f.write(f"{token}\n")


#Função para verificar se é um operando
def operando(token):
    if token in ("RES", "MEM"):
        return True
    try:
        float(token)
        return True
    except:
        return False

#Função para verificar se é operador 
def operador(token):
    return token in ['+', '-', '*', '/', '//', '%', '^']

#Função para validar sintaxe RPN simples
#Verifica se está no formato (operando operando operador)
def valida_rpn(tokens):
    i = 0
    for i in range(len(tokens)):
        if tokens[i] == '(':
            if i + 4 >= len(tokens):
                raise ValueError("Expressão incompleta após '('")
            if not operando(tokens[i + 1]) or not operando(tokens[i + 2]) or not operador(tokens[i + 3]) or tokens[i + 4] != ')':
                raise ValueError(f"Expressão RPN inválida: {tokens[i:i+5]}")
    

