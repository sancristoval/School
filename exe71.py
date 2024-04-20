print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
n1=int(input('que valor você quer sacar? R$ '))
n2=n1
n3=50
n4=0
while True:
    if n2>=n3:
        n2-=n3
        n4+=1
    else:
        if n4>0:
            print(f'Total de {n4} cédulas de R${n3 }')
        if n3==50:
            n3=20
        elif n3==20:
            n3=10
        elif n3==10:
            n3=1
        n4=0
        if n2==0:
            break
print('='*30)
print(' volte senpre ao BANCO CEV! Tenha um bom dia!')
