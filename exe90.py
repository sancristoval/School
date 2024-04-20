dados=dict()
dados['nome']=str(input('nome: '))
dados['media']=float(input(f'Média de {dados["nome"]} '))

if dados['media']>=7.0:
    n='Aprovado'
if dados['media']>=5.0 and dados['media']<7.0:
    n='Recuperação'
if dados['media']<5:
    n='Reprovado'
print('-='*30)
print(f'  - nome é igual a {dados["nome"]}')
print(f'  - média é igual a {dados["media"]}')
print(f'  - situação é igua a {n}')