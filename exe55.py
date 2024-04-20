maior=0
menor=0
for c in range(1, 6):
    n=float(input(f'peso da {c}° pessoa: '))
    if c==1:
        maior=n
        menor=n
    else:
        if n>maior:
            maior=n

        if n<menor:
            menor=n
print(f'o maior peso lido foi de {maior}kg')
print(f'O menor peso lido foi de {menor}kg')