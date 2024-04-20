print('-'*40)
print('      listagem de preços')
print('-'*40)
n=('lapis',1.75,
'borracha',2,
'caderno',15.90,
'estojo',25.00,
'transferidor',420,
'compasso',9.99,
'mochila',120.32,
'caneta',22.30,
'livro',34.90)
for c in range(0, len(n)):
    if c % 2==0:
        print(f'{n[c]:.<30}',end='')
    elif c % 1==0:
        print(f'R${n[c]:>7.2f}')
