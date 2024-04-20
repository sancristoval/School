dados=dict()
dado=list()
i=n1=0
while True:
    dados['nome']=str(input('Nome: '))
    n1+=1
    s=str(input('Sexo: '))
    if s not in 'FfMm':
        while True:
            if s not in 'FfMm':
                print('ERRO! por favor, digite apenas M ou F.')
                s=str(input('Sexo: '))
                if s in 'FfMm':
                    break
    dados['sexo']=s

    dados['idade']=int(input('Idade: '))
    i+=dados['idade']
    dado.append(dados.copy())
    n=str(input('quer continuar? [N/S]: '))
    if n not in 'SsNn':
        while True:
            if n not in 'SsNn':
                print('ERRO! Responda apenas S ou N.')
                n=str(input('quer continuar? [N/S]: '))
                if n in 'SsNn':
                    break
    if n in 'Nn':
        break
print(f'A) Ao todo temos {n1} pessoas cadastradras.')
print(f'B) A média de idade é de {i/n1:.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for x in dado:
    if x['sexo'] in 'Ff':
        print(f'{x["nome"]} ', end='')
print('')
print(f'D) Lista das pessoas que estão acima da média:')
for x in dado:
    if x['idade']>=i/n:
        print('   ',end='')
        for f, d in x.items():
            print(f'{f} = {d}: ', end='')
        print()
print('-='*30)
print('<< ENCERRADO >>')