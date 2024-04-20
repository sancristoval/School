n1=n3=n4=n5=0
while True:
    print('-'*20)
    print('   CADASTRE UMA PESSOA')
    print('-'*20)
    n1=int(input('idade: '))
    n2=str(input('sexo: [M\F ]'))
    print('-'*20)
    b=str(input('quer continuar? [N\S]'))
    print('-'*20)
    if n1>=18:
        n3+=1
    if n2 in 'mM':
        n4+=1
    else:
        if n2 in 'fF' and n1<=20:
            n5+=1
    if b in 'nN':
        break
print(f'Total de pessoas com mais de 18 anos: {n3}')
print(f'Ao todo temos {n4} homes cadastrados')
print(f'E temos {n5} mulheres com menos de 20 anos')