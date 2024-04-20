n1=float(input('primeiro seguimento: '))
n2=float(input('segundo seguimento: '))
n3=float(input('terceiro seguimento: '))
if n1<=n2+n3 and n2<=n1+n3 and n3<=n1+n2:
    m='PODEM'
else:
    m='NÃO'
if n1==n2 and n1==n3:
    m2='EQUILÁTERO'
elif n1==n2 or n1==n3 or n3==n2:
    m2='ISÓSCELES'
elif n1!=n2 and n2!=n3 and n1!=n3 and m=='podem':
    m2='ESCALENO'
else:
    m2=''
print(f'Os seguimentos acima {m} FORMAR UM TRIÂNGULO {m2}')

