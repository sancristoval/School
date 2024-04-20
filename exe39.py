from datetime import date
n2=date.today().year
n=int(input('Ano de nasimento: '))
n3=n2-n
print(f'Quem naseu em {n} tem {n3} anos em {n2}')
if n==18:
    print('você tem que se alistas IMEDIATAMENTE!')
elif n<18:
    print(f'ainda faltam {n3-18} anos para o alistamento')
    print(f'seu alinstamento será em {n2+18-n3}')
elif n>18:
    print(f'você já deveria ter se alistado há {18-n3} anos.')
    print(f'seu alistamento foi em {n2+18-n3}')
