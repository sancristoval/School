n1=float(input('qual é o peso? (kg)'))
n2=float(input('qual é sua Altura? (m)'))
n3=n1/(n2**2)
print(f'O IMC dessa pessoa é de {n3:.2f}')
if n3<=18.5:
    n4='abaixo do peso'
elif n3>18.5:
    n4='ideal'
elif n3>25:
    n4='soprepeso'
elif n3>30:
    n4='obesidade'
elif n3>40:
    n4='obesidade mórbida'
print(f'você está na faixa de {n4}')