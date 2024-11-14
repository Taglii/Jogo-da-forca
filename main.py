#entrada da palavra da forca
#palavra da forca dentro de um vetor
#while com a os tracejados baseado no numero de letras
#entrada de letra
#verificação se existe a letra na palavra digitada inicialmente.
#se sim a letra entra no local exato da letra e a letra aparece em letras digitadas
#se nao a letras so entra em letras digitadas e jogador perder 1 de vida.



palavra_escolida = []
letra_jogada = []
vida_jogador = 6
ganhou = False

palavra = input('Informe a palavra: ')
for i in range(10):
    print("")

palavra_escolida = palavra


while True:
    for letra in palavra_escolida:
        if letra.lower() in letra_jogada:
            print(letra, end = ' ')
        else:
            print('_', end = ' ')
    print('')
    print('voce tem {} chances'.format(vida_jogador))
    print('Letras jogadas: ', letra_jogada)
    
    tentativa = input('Escolha uma letra: ')
    if tentativa in letra_jogada:
        print('Você ja jogou essa letra')
        continue
    letra_jogada.append(tentativa.lower())
    
    if tentativa.lower() not in palavra_escolida.lower():
        vida_jogador -= 1

    ganhou = True
    for letra in palavra_escolida:
         if letra.lower() not in letra_jogada:
            ganhou = False
    if vida_jogador == 0 or ganhou:
        break
    
    
    
if ganhou:
        print("acertou a palavra a palavra era: {} ".format(palavra_escolida))
else:
        print("vixi, voce errou a palavra era: {}".format(palavra_escolida))
