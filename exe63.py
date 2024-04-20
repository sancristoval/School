print('-'*20)
print('sequência de fibonacci')
print('-'*20)
n=int(input('quantos termos você quer mostrar? '))
t1=0
t2=1
print('~'*20)
print(f'{t1} → {t2}',end='')
c=3
while c <= n:
    t3=t1+t2
    print(f' → {t3}',end='')
    t1=t2
    t2=t3
    c+=1
print(' → Fim')