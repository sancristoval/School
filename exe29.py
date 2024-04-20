
n=float(input('qual a velocidade do carro? '))
if n>=81:
    print('\033[31mMULTADO! você excedeu o limite de velocidade que é de 80km/h')
    print(f'Você deve pagar uma multa de R${(n-80)*7}!\033[m]')
print('\033[32mtenha um bom dia! diriga com segurança\033[m')
