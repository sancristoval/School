m=m1=0
n=[]
for c in range(0,5):
    n.append(int(input(f'digite um valor a posição {c}: ')))

    if c==0:
        m=m1=n[0]
    else:
        if n[c]>m:
            m=n[c]
            m3=c
        if n[c]<m1:
            m1=n[c]


print('=-'*30)
print(f'Você ditou os valores {n}')
print(f'O maior valor digitado foi {m} na posição  {c}')
print(f'O menor valor digitado foi: {m1}')
