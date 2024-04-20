from time import sleep
from random import randint
list=[]
j=[]
print('-='*30)
print('               JOGO DA MEGA SENA')
print('-='*30)
n=int(input('quantos jogos você quer que eu sorteie? '))
t=0
while t<=n:
    c=0
    while True:
        m=randint(1, 60)
        if m not in list:
            list.append(m)
            c+=1
        if c>=6:
            break
    list.sort()
    j.append(list[:])
    list.clear()
    t+=1
print('-='*3, f'SORTEANDO {n} JOGOS','-='*3)
for i, l in enumerate(j):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print('-='*3, '< BOA SORTE! >', '-='*3)
