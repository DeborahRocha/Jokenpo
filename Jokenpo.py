import random
from time import sleep
nome = str(input('Qual é o seu nome? ')).upper()
print('Bem vindo ao jogo de pedra, papel e tesoura')
print('Boa sorte!')
opcao = str(input('Qual será sua escolha? '))
lista = ['pedra' , 'papel', 'tesoura']
computador = random.choice(lista)
print('O COMPUTADOR esta pensando...')
sleep(2)
print(f'A escolha do COMPUTADOR foi: {computador}')
if opcao == 'papel' and computador == 'pedra':
    print('PAPEL GANHOU DE PEDRA')
    print(f'O vencedor é {nome}')
elif opcao == 'papel' and computador == 'tesoura':
    print('TESOURA GANHOU DE PAPEL')
    print(f'O vencedor é COMPUTADOR')
elif opcao == 'papel' and computador == opcao:
    print('EMPATE')
sleep(2)
if opcao == 'tesoura' and computador == 'pedra':
    print('PEDRA GANHOU DE TESOURA')
    print('O vencedor é COMPUTADOR')
elif opcao == 'tesoura' and computador == 'papel':
    print('TESOURA GANHOU DE PAPEL')
    print(f'O vencedor é {nome}')
elif opcao == 'tesoura' and computador == opcao:
    print('EMPATE')
if opcao == 'pedra' and computador == 'tesoura':
    print('PEDRA GANHOU DE TESOURA')
    print(f'O vencedor é {nome}')
elif opcao == 'pedra' and computador == 'papel':
    print('PAPEL GANHOU DE PEDRA')
    print('O vencedor é COMPUTADOR')
elif opcao == 'pedra' and computador == opcao:
    print('EMPATE')
print(f'FIM DE JOGO {nome}')