import Main

expressao1 = "(3 4 +)"
expressao2 = "(10 5 /)"
expressao3 = "(2 3 4 + 5 *)"
expressao4 = "((1.5 2.0 *) (3.0 4.0 *) /)"
expressao5 = "(3.14 2.0 +)"

Saida = []

for i, expressao in enumerate([expressao1, expressao2, expressao3, expressao4, expressao5], 1):
        try:
                tokens = Main.parseExpressao(expressao)
                print(f"Teste {i}")
                print(f"Expressão: {expressao}")
                print(f"Tokens: {tokens}\n")
                Saida.append((expressao, tokens))

        except ValueError as e:
                print(f"Teste {i}")
                print(f"Expressão: {expressao}")
                print(f"Erro: {e}\n")
                Saida.append((expressao, str(e)))

