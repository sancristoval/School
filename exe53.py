n1=str(input('digite uma frase; ')).strip().upper()
n2=n1.split()
n3=''.join(n2)
n4=n3[::-1]
print(f'o inverso de {n3} é {n4}')
if n3==n4:
    print('TEMOS um palindromo!')
else:
    print('A frase digitada não é um pallindromo')