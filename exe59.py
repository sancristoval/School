from time import sleep
n3=0
n1=int(input('primeiro valor: '))
n2=int(input('seguendo valor: '))
while n3 != 5:
    print('''        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
    n3=int(input('>>>>> qual é a sua opção? '))
    if n3==5:
        break
    if n3==4:
        n1=int(input('primeiro valor: '))
        n2=int(input('seguendo valor: '))
    if n3==1:
        print(f'a soma entre {n1} + {n2} é {n1+n2}')
    if n3==2:
        print(f'O resultado de {n1} x {n2} é {n1*n2}')
    if n3==3:
        maior=n1
        if n2>n1:
            maior=n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    else:
        print('opção invalida. tente novamente')
    print('=-='*10)
    sleep(1)
print('finalizando...')
sleep(2)
print('fim do progama! Volti sempre!')
print('')

