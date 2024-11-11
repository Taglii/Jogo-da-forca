#entrada da palavra da forca
#palavra da forca dentro de um vetor
#while com a os tracejados baseado no numero de letras
#entrada de letra
#verificação se existe a letra na palavra digitada inicialmente.
#se sim a letra entra no local exato da letra e a letra aparece em letras digitadas
#se nao a letras so entra em letras digitadas e jogador perder 1 de vida.



palavra_escolida = []
letra_jogada = []
vida_jogador = 7
ganhou = False
erros = 0

palavra = input('Informe a palavra: ')
palavra_escolida = palavra

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


while True:
    for letra in palavra_escolida:
        if letra.lower() in letra_jogada:
            print(letra, end = ' ')
        else:
            print('_', end = ' ')
    print('')
    print('voce tem {} chances'. format(vida_jogador))
    
    tentativa = input('Escolha uma letra: ')
    letra_jogada.append(tentativa.lower())
    
    if tentativa.lower() not in palavra_escolida.lower():
        erros +=1
        vida_jogador -=1
        desenha_forca(erros)

    ganhou = True
    for letra in palavra_escolida:
         if letra.lower() not in letra_jogada:
            ganhou = False
    if vida_jogador == 0 or ganhou:
        break
    
    
    
if ganhou:
        print("acertou a palavra a palavra era: {} ".format(palavra_escolida))
else:
        print("vixi, voce errou, a palavra era: {}".format(palavra_escolida))
