n=[]
while True:
    c=int(input('digite um valor: '))
    if c not in n:
        n.append(c)
        print('Valor adisionado com SUCESSO...')
    else:
        print('valor duplicado! não vou adicionar...')
    n1=str(input('quer continuar? [N\S] '))
    if n1 in 'Nn':
        break
print(f'Você digitou os valores {sorted(n)}')