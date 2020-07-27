from random import randint
from time import sleep
from emoji import emojize

jogar = 's'

while jogar == 's':

    Pedra = emojize('pedra :fist:',use_aliases=True)
    Papel = emojize('papel :hand:', use_aliases=True)
    Tesoura = emojize('tesoura :v:',use_aliases=True)
    itens = (Pedra, Papel,Tesoura)
    computador = randint(0,2)
    print(emojize('''Suas opções: 
    [ 0 ] PEDRA :fist:
    [ 1 ] PAPEL :hand:
    [ 2 ] TESOURA :v:''',use_aliases=True))

    jogador = int(input('Qual é a sua jogada? '))
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!')
    print('-=' * 11)
    print('Computador jogou {} '.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)

    if computador == 0: # computador jogou PEDRA
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('JOGADOR VENCE!')

        elif jogador == 2:
            print('COMPUTADOR VENCE!')

        else:
            print('JOGADA INVÁLIDA!')

    elif computador == 1: # computador jogou PAPEL
        if jogador == 0:
            print('COMPUTADOR VENCE!')
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('JOGADOR VENCE!')

        else:
            print('Jogada Inválida!')


    elif computador == 2: # computador jogou TESOURA
        if jogador == 0:
            print('JOGADOR VENCE!')
        elif jogador == 1:
            print('COMPUTADOR VENCE!')
        elif jogador == 2:
            print('EMPATE!')
        else:
            print('Jogada Inválida!')

    
    jogar = input('Deseja continuar? s/n ')
prin('Você saiu do jogo! ')
    

