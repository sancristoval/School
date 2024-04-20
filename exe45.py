from random import choices, randint
from time import sleep
list=('PEDRA', 'PAPEL', 'TISOURA' )
n2=randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
n1=int(input('qual é a sua jogada? '))
if n1==n2:
    m='IMPATE'
elif n2==0 and n1==1:
    m='JOGADOR GANHOU!!!'
elif n2==0 and n1==2:
    m='COMPUTADOR GANHOU'
elif n2==1 and n1==0:
    m='COMPUTADOR GANHOU'
elif n2==1 and n1==2:
    m='JOGADOR GANHOU'
elif n2==2 and n1==0:
    m='JOGADOR GANHOU'
elif n2==2 and n1==1:
    m='COMPUTADOR GANHOU'
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('')
print('-='*30)
print(f'''O computador escolheu: {list[n2]}
O jogador escolheu: {list[n1]}''')
print('-='*30)
print(f'{m}')
print('')
