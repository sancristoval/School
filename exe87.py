soma=terseiro=linha=0
n1=[[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for c in range(0, 3):
    for v in range(0, 3):
        n1[c][v]=int(input(f'digite um valor para [{c}, {v}]: '))
        if n1[c][v]%2==0:
            soma+=n1[c][v]
        if v==2:
            terseiro+=n1[c][v]
print('-='*30)
for c in range(0, 3):
    for v in range(0, 3):
        print(f'[{n1[c][v]:^15}]',end='')
    print()
print('-='*30)
print(f'A soma dos pares é {soma}')
print(f'A soma dos valores da terseira coluna é {terseiro}.')
for v in range(0, 3):
    if v ==0:
        linha=n1[1][v]
    elif n1[1][v]>linha:
        linha=n1[1][v]
print(f'O maior valor da segunda linha é {linha}.')
