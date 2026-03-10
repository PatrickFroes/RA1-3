import Main

expressao1 = "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"
expressao2 = "A + B * C - D / E"
expressao3 = "X1 + Y2 - Z3 * ( W4 / V 5 )"
expressao4 = "5.5 * 2.0 + ( 3.1 - 1.2 )"
expressao5 = "A + ( B - C ) * D / E ^ F"

Saida = []

for i, expressao in enumerate([expressao1, expressao2, expressao3, expressao4, expressao5], 1):
        tokens = Main.parseExpressao(expressao)
        print(f"Teste {i}")
        print(f"Expressão: {expressao}")
        print(f"Tokens: {tokens}\n")
        Saida.append((expressao, tokens))

Main.salvar_tokens(Saida)
