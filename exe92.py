from datetime import datetime
dados=dict()
dados['nome']=str(input('nome: '))
n=int(input('Ano de Nacimento: '))
dados['nacimento']=datetime.now().year-n
dados['carteira']=int(input('Carteira de Trabalho (0 não tem): '))
if dados['carteira'] !=0:
    dados['contratação']=int(input('Ano de Contratação: '))
    dados['salario']=int(input('Salário: '))
dados['aposentadoria']=dados['nacimento']+((dados['contratação']+35)-datetime.now().year)
print('-='*30)
for c, v in dados.items():
    print(f'   -{c} tem o valor {v}')
'''print(f'   - nome tem o valor {dados["nome"]}')
print(f'   -idade tem o valor {dados["nacimento"]}')
print(f'   - ctps tem o valor {dados["carteira"]}')
if dados['carteira']!=0:
    print(f'   - contratação tem o valor {dados["contratação"]}')
    print(f'   - saçário tem o valor {dados["salario"]}')
    print(f'   - aposentadoria tem o valor {dados["aposentadoria"]}')'''