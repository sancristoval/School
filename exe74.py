n2=12
n4=0
from random import randint
n1=(randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),)
print('Os valores sorteados foram: ',end='')
for c in n1:
    print(f'{c} ',end='')
print(f'\nO menor valor sorteado foi {min(n1)}')
print(f'O maior valor sorteado foi {max(n1)}')
