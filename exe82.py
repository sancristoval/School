n1=[]
n2=[]
n3=[]
while True:
    n1.append(int(input('digite um número: ')))
    m=str(input('quer continuar? '))
    if m in 'Nn':
        break
for i,b in enumerate(n1):
    if b%2==0:
        n2.append(b)
    if b%2==1:
        n3.append(b)
print('-='*30)
print(f'A lista completa é {n1}')
print(f'A lista de pares é {n2}')
print(f'A lista de impares é {n3}')
