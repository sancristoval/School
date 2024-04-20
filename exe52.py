n2=0
n1=int(input('digite um número: '))
for c in range(1, n1+1):
    if n1%c==0:
        print('\033[33m',end='')
        n2+=1
    else:
        print('\033[31m',end='')
    print(f'{c}',end=' ')
print(f'\n\033[mO número {n1} foi divisível {n2} vezes')
if n2==2:
    n3='É'
else:
    n3='NÃO'
print(f'E por isso ele {n3} primo!')
