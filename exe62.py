print('gerador de pa')
print('-='*20)
n1=int(input('primeiro valor '))
n2=int(input('razão da pa '))
n4=n1
n3=1
mais=10
n5=0
while mais!=0:
    n5+=mais
    while n3<=n5:
        print(f'{n4} → ',end='')
        n4+=n2
        n3+=1
    print('pausa')
    mais=int(input('quantos termos você quer mostrar a mais? '))
print(f'progressâo finalizada com {n5} termos mostrados')
