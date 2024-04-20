n1=n2=0
def cáuculo(l, c):
    m=l*c
    print(f'A área de um terreno {l}x{c} é de {m}m².')


print('controle de terrenos')
print('-'*30)
l=float(input('LARGURA (m): '))
c=float(input('COMPRIMENTO (m): '))
cáuculo(l, c)