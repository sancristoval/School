n1=0
n=[]
while True:
    n.append(int(input('digite um número: ')))
    n1+=1
    if 5 in n:
        m1='O valor 5 fas parte da lista!'
    else:
        m1=''
    m=str(input('quer continuar? [N\S] '))
    if m not in 'Ss':
        break
n.sort(reverse=True)
print(f'Você digitou {n1} elementos.')
print(f'Os números em ordem crescente são {n}')
print(m1)
