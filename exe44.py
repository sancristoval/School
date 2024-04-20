n1=float(input('preço do produto? '))
print('''qual forma de pagamento
[ 1 ] á vista dinhero/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
n2=int(input('qual é a opção: '))
if n2==1:
    print(f'Sua compra de {n1} vai custar R${n1-(n1*10/100):.2f} no final.')
elif n2==2:
    print(f'Sua compra de {n1} vai custar R${n1-(n1*5/100):.2f} no final.')
elif n2==3:
    print(f'Sua compra de {n1} vai custar R${n1:.2f} no final.')
elif n2==4:
    n3=int(input('quantas vezes no cartão? '))
    print(f'Sua parcelada em {n3}x de R${(n1+(n1*20/100))/n3:.2f} COM JUROS')
    print(f'Sua compra de {n1} vai custar R${n1+(n1*20/100)} no final.')