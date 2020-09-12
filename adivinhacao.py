print ('*'*30)
print ('*     Jogo de adivinhação    *')
print ('*'*30)

numero_de_tentativas =  3
rodada = 1


for rodada in range (1, numero_de_tentativas + 1):

    print('Tentativa {} de {}'.format(rodada, numero_de_tentativas))

    chute = int(input('Qual seu palpite? '))
    numero_secreto = 42
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print('Você acertou!')
        break
    elif (maior):
        print('Quase, seu palpite foi maior!')
    elif (menor):
        print('Quase, seu palpite foi menor!')

print('Jogo encerrado!')

    

