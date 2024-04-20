n1=int(input('digite um número inteiro'))
print('''escolhauma das bases para conversão:
[ 1 ] conserter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
n2=int(input('sua opção: '))
if n2==1:
    print(f'{n1} convertido para BINÁRIO é igual {bin(n1)[2:]}')
elif n2==2:
    print(f'{n1} cnvertido para OCTAL é igaul a {oct(n1)[2:]}')
elif n2==3:
    print(f'{n1} convertido para HEXADECIMAL é igual a {hex(n1)[2:]}')
else:
    print(' opção invalida! tente novamente')
