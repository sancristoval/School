n1=float(input('valor da casa: R$'))
n2=float(input('salario do comprador: R$'))
n3=int(input('quantos anos de finansiamento? '))
n4=n1/(n3*12)
n5=n2*30/100
print(f'para pagar sua casa de {n1} em {n3} anos',end='')
print(f'a prestação será de R${n4:.2f}')
if n5 <=n4:
    print('emprestimo consedido')
else:
    print('emprestimo negado')

