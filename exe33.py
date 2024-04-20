n=int(input('primeiro valor: '))
n1=int(input('segundo valor: '))
n2=int(input('terseiro valor: '))
menor=n
if n1<n2 and n1<n:
    menor=n1
if n2<n and n2<n1:
    menor=n2
else:
    menor=(f'todos os valores são iguais a {n} ')
maior=n
if n1>n and n1>n2:
    maior=n1
if n2>n and n2>n1:
    maior=n2
else:
    maior=(f'todos os valores são iguais a {n} ')
print(f' O menor valor é {menor}')
print(f' O maior valor é {maior}')
