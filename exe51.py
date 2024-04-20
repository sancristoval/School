print('='*30)
print('       10 termos de uma pa')
print('='*30)
n1=int(input('primeiro valor: '))
n2=int(input('razão: '))
for c in range(n1, n1+10*n2, n2):
    print(c, end=' → ')
print('ACABOU')