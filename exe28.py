from time import sleep
from random import randint
n=randint(0, 5)
print('-=-'*23)
print('vou pensar em um número entre 0 e 5. tente adivinnhar...') 
print('-=-'*23)
n1=int(input('em que número eu pensei? '))
print('PROCESSANDO...')
sleep(4)
if n == n1:
    print('PARABENS!')
else:
    print(f'ERROU! eu pensei no número {n}')
