n2='s'
n4=0
n3=0
while n2 not in'nN':
    n1=int(input('digite um número: '))
    n3+=1
    n4+=n1
    if n3==1:
        m1=m2=n1
    else:
        if n1>m1:
            m1=n1
        if n1<m2:
            m2=n1
    n2=str(input('quer continuar? [N\S]'))
print(f'você digitou {n3} números e a média foi {int(n4/n3)} O maior valor foi {m1} e o menor foi {m2}')
