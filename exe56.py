nvelho=''
ivelho=0
númerof=0
idades=0
for c in range(1, 5):
    print(f'----- {c}° pessoa -----')
    nome=str(input('Nome: '))
    idade=int(input('idade: '))
    sexo=str(input('sexo [M\F]: '))
    idades+=idade
    if c == 1 and sexo in "Mm":
        ivelho=idade
        nvelho=nome

    if sexo in 'Mm' and idade>ivelho :
        ivelho=idade
        nvelho=nome

    if sexo=='f' or 'F' and idade<=20:
        númerof=+1
print(f'A média de idade do grupo de {int((idades)/4)} anos')
print(f'O homen mais velho tem {ivelho} anos e se chama {nvelho}')
print(f'Ao todo são {númerof} mulheres com menos de 20 anos')
