pessoas=[]
while True:
    n1=str(input('Nome: '))
    n2=int(input('Nota 1: '))
    n3=int(input('Nota 2: '))
    n4=(n2+n3)/2
    pessoas.append([n1, [n2, n3], n4])
    n=str(input('quer continuar? '))
    if n not in 'sS':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÈDIA":>8}')
print('-'*20)
for c, v in enumerate(pessoas):
    print(f'{c:<4}{v[0]:<10}{v[2]:>8.1f}')
while True:
    print('-'*35)
    o=int(input('Mostrar notas de qual Aluno? (999 interronpe): '))
    if o ==999:
        print('FINALIZADO... ')
        break
    if o<=len(pessoas)-1:
        print(f'Notas de {pessoas[o][0]} são {pessoas[o][0]}')
print('<<< VOLTE SENPRE ')