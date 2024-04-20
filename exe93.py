
dados=dict()
partidas=list()
dados['nome']=str(input('nome do jogador: '))
n=int(input(f'quantas partidas {dados["nome"]} jogo: '))
dados['partidas']=n
for c in range(0, n):
    partidas.append(int(input(f'quantos gols na partida {c} ')))
dados['gols']=partidas
dados['total']=sum(partidas)
print('-='*30)
print(f'{dados}')
print('-='*30)
for v, b in dados.items():
    print(f'O campo {v} tem o valor {b}')
print('-='*30)
print(f'O jogador {dados["nome"]} jogou {n} partifdas.')
for c, v in enumerate(dados['gols']):
    print(f'   =>Na partida {c}, fez {v} gols.')
print(f'Foi um total de {dados["total"]}')