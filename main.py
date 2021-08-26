import funcoes

funcoes.cabecalho()
funcoes.escolha_da_palavra()
nome_palavra = funcoes.palavra_do_arquivo().upper()

palavra = funcoes.palavra_utilizada()

# o caractere '_' será subsituído pela letra digitada pelo jogador à medida que ele acertar
letras = list('_' * len(palavra))

# Implemento de lógica da letra digitada pelo jogador sendo armazenada numa lista
# de forma que a variável "letras" possa ser comparada com a variável "letras_armazenada"
letras_armazenada = list()
for p in palavra:
    letras_armazenada.append(p)

escolhas = list()  # criada apenas para inicializar a visualização das letras escolhidas pelo jogador
escolha_da_dificuldade = str(input("Informe 'F' para Facil ou 'D' para Dificil: ").upper())
if escolha_da_dificuldade == 'F':
    qtde_chances = 10
if escolha_da_dificuldade == 'D':
    qtde_chances = 6  # valor arbitrário e pode ser modificado

while True:
    if letras_armazenada == letras:
        print(f'A palavra é {nome_palavra}!!! VOCÊ ACERTOU! PARABÉNS!!!')
        break
    print(f'A palavra é: {" ".join(letras)}', end=' ')
    escolha_letra = str(input('Digite uma letra: ').strip().upper())
    print()
    if escolha_letra not in letras and escolha_letra in palavra:
        for indice, letra_palavra in enumerate(palavra):
            if escolha_letra == letra_palavra:
                letras[indice] = letra_palavra
    else:
        qtde_chances -= 1
        if qtde_chances != 0:
            print(f'Errou! Você possui mais {qtde_chances} chances.')
        else:
            print(f'Que pena!!! Você perdeu! A palavra é {nome_palavra}!')
            break

    if qtde_chances == 3 and escolha_letra not in palavra:
        print(funcoes.dica())

    if escolha_letra not in escolhas:
        escolhas.append(escolha_letra)

    print('.' * 55)
    print(f'Letras já usadas: {", ".join(escolhas)}')
    print('-' * 55)
