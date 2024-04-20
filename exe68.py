list=(1,10)
n3=0
from random import choice
print('=-'*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*15)
while True:
    n4=choice(list)
    n1=int(input('diga um valor: '))
    n2=str(input('par ou impar? [P\I]'))
    if (n1+n4)%2==0:
        n5='par'
    else:
        n5='impar'
    print('-'*30)
    print(f'Você jogou {n1} e o computador {n4}. total de {n1+n4} DEU {n5}')
    print('-'*30)
    if n2 in 'iI' and n5=='impar' or n2 in 'pP' and n5=='par':
        n6='VENCEU'
    else:
        break
        n6='PERDEU!'
    print(f'Você {n6}')
    print('=-'*15)
    n3+=1
print(f'GAME OVER você venceu {n3} vezes.')
print('')
print('')
