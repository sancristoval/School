n=float(input('qual é a distansia da sua viagem? '))
if n <=200:
    print(f'E o preço da sua passagem será de R${n*0.50}')
else:
    print(f'E o preso da sua passagem será de R${n*0.45}')