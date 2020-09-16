print('*'*30)
print('Bem vindo ao jogo da Forca')
print('*'*30)

palavra_secreta = 'banana'
letras_acertadas = ['_', '_', '_', '_', '_', '_']

acertou = False
enforcou = False
erros = 0

print(letras_acertadas)

while (not enforcou and not acertou):
    chute = input('Qual letra? ')

    if(chute in palavra_secreta):
        posicao = 0
        
        for posicao, letra in enumerate(palavra_secreta):
            if (chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra
            
            posicao += 1
                
    else:
        erros += 1
    
    enforcou = erros == 6
    acertou = '_' not in letras_acertadas
    print(letras_acertadas)

if(acertou):
    print('você ganhou!')
else:
    print('você perdeu!')
print('Fim do jogo!')

