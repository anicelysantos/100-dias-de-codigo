#import random

#TUPLAS SÃO IMUTÁVEIS
#  
#lanche = 'hamburguer','suco', 'pizza', 'pudim','batata-frita'
#
#for cont in range (0, len(lanche)):
#    print(f'Eu vou comer {lanche[cont]}')
#
#for c in lanche:
 #   print ('Eu vou comer {}'.format(c))
#print('Comi pra caramba!')

#for pos, comida in enumerate(lanche):
#   print (f'Eu vou comer {comida} na posição {pos}')
#print('Comi pra caramba!')

#for cont in range (0, len(lanche)):
#   print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#print(sorted(lanche)) //Tupla em ordem alfabética
#
#a = 1, 5, 4
#b = 5, 8, 1, 2
#c = a + b
#
#print(c.index(8))

#pessoa = ('Gustavo', 39, 'M', 99.88)
#print(pessoa)

#-------------------------------------------------------
#1. Crie um programa que tenha uma tupla totalmente preenchida
#com uma contagem por extenso de zero até vinte. Seu programa
#deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

#-------RESPOSTA------
#extenso = 'zero', 'um', 'dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte'

#while True:
#    pergunta = int(input('Qual o numero que você quer de 0 a 20? '))
#    if 0 <= pergunta <= 20:
#        for procura in range(0,20):
#            if procura == pergunta:
#                print(f'O numero que você escolheu por extenso é {extenso[pergunta]}')
#        break
#    else:
#        print('tente novamente. ', end="")
       
#2. Crie uma tupla preenchida com os 20 primeiros colocados na tabela
#do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
#A) Apenas os 5 primeiros colocados;
#B) Os últimos 4 colocados da tabela;
#C) Uma lista com os times em ordem alfabética;
#D) Em que posição na tabela está o time da chapecoense;

#-------RESPOSTA------

#futebol = 'internacional', 'atletico - mg', 'são paulo', 'vasco', 'flamengo','santos','fluminense','ceará','fortaleza','atlético-go','grêmio','athletico-pr','sport','corinthians','bahia','botafogo','goiás','coritiba','bragantino'

#print(f'Os 5 primeiros colocados são: {futebol[0:5]}')
#print(f'Os últimos 4 colocados da tabela são{futebol[15:20]}')
#print(sorted(futebol))

#for c in futebol:
#    if c == 'chapecoense':
#        print ('achei!')
#    else:
#        print('Não achei!')
#        break
#ou
#print(f'o Santos está na {futebol.index("santos")+1}ª posição')



#3. Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e
#o maior valor que estão na tupla;

#-------RESPOSTA------
#a = random.randrange(999)
#b = random.randrange(999)
#c = random.randrange(999)
#d = random.randrange(999)
#e = random.randrange(999)

#aleatorio = a , b, c, d, e

#print(f'A sequencia é {aleatorio}')
#ordem = (sorted(aleatorio))
#print(f'O maior valor é {ordem[4]}')
#print(f'O menor valor é {ordem[0]}')


#4. Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
#em uma tupla. No final mostre:
#A) Quantas vezes apareceu o valor 9;
#B) Em que posição foi digitado o primeiro valor 3;
#c) Quais foram os números pares;

#-------RESPOSTA------

#a = int(input('Digite um valor (de 0 a 10): '))
#b = int(input('Digite um valor (de 0 a 10): '))
#c = int(input('Digite um valor (de 0 a 10): '))
#d = int(input('Digite um valor (de 0 a 10): '))

#valores = a , b, c, d

#nove = 0
#for c in valores:
#    if (c == 9):
#        nove+=1
#print (f'Aparece {nove}x numero 9')

#for pos, c in enumerate(valores):
#    if (c == 3):
#        print (f'O valor 3 aparece a primeira vez na posição {pos}')
#        break

#for c in valores:
#    if ((c%2)==0):
#        print(f'{c} ', end="")

    
#5. Crie um programa que tenha uma tupla única com nomes de produtos e seus
#respectivos preços na sequencia. No final, mostre uma listagem de preços,
#organizando os dados em forma tabular;

#-------RESPOSTA------

#alimentos = 'picolé', 1.00 ,'pipoca', 0.55,'pirulito', 0.25

#print('-' * 37)
#print(f'{"LISTAGEM DA BARRACA":^37}')
#print('-' * 37)

#for pos in range (0, len(alimentos)):
#    if pos % 2 == 0:
#        print(f'{alimentos[pos]:.<30} ', end="")
#    else:
#        print(f'R${alimentos[pos]:.2f}')

#6. Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


#palavras = 'banana', 'maça', 'pera', 'acerola', 'manga', 'pitanga'

#for p in palavras:
#    print(f'\nNa palavra {p.upper()} temos ', end='')
#    for letra in p:  
#        if letra in 'aeiou':
#            print(letra, end=' ')




