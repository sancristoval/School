n6=999999999999999
n5=n4=n2=0
print('-'*30)
print('    LOJA SUPER BARATÃO')
print('-'*30)
while True:
    n1=str(input('nome do produto: '))
    n2=int(input('preço: do produto: '))
    if n2<n6:
        n6=n2
        n7=n1
    if n2>=1000:
        n5+=1
    n4+=n2

    n3=str(input('quer continuar? [N\S ]'))
    if n3 in 'nN':
        break
print('------------ FIM DO PROGRAMA ----------------')
print(f'O total da compra foi de {n4}')
print(f'Temos {n5} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {n7} que custa R${n6}')
print('')
