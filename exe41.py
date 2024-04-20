from datetime import date
n=int(input('Ano de nacimento: '))
n1=date.today().year
n2=n1-n
print(f'O atleta tem {n2} Anos. ')
if n2<=9:
    print('Classificação: MIRIM ')
elif n2>=10. <=14:
    print('Classificação: INFANTIL ')
elif n2>=15. <=19:
    print('Classificação: JUNIO ')
elif n2>=20. <=25:
    print('Classificação; SÊNIOR ')
elif n2>26:
    print('Classificação: MASTER ')
else:
    print('REQUISITOS MINIMOS NÃO ALCANSADOS')
