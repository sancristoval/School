n=int(input('digite um número para calcularseu fatorial'))
f=n
c=1
print(f'calculando {n}! = ')
while f>0:
    print(f'{f} x ', end='')
    print(f' x ' if f>1 else ' = ',end='')
    c*=f
    f-=1
print(c)