n1=(int(input('digite um número: ')),
              int(input('digite outro número: ')),
              int(input('digite mais um número: ')),
              int(input('digite o último número: ')))
print(f'você digitou os valores: {n1}')
print(f'O valor 9 apareceu {n1.count(9)} vazes')
if 3 in n1:
    print(f'o valor apareceu na {n1.index(3)} posição')
else:
    print('o valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ',end='')
for n in n1:
    if n%2==0:
        print(n,end=' ')