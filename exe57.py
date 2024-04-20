sexo=str(input('informe seu sexo: [M/F] '))
while sexo not in 'MmFf':
    sexo=str(input(('dados invalidos tente novamente:')))
print(f'sexo {sexo} registrado com sucesso.')