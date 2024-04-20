from random import randint
from time import sleep
from operator import itemgetter
dados={'jogador1':randint(1, 6),
           'jogador2':randint(1, 6),
           'jogador3':randint(1, 6),
           'jogador4':randint(1, 6)}
r=list()
print('Valores sorteados:')
for c, v in dados.items():
    print(f'{c} tirou {v} no dado.')
    sleep(1)
r=sorted(dados.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('    == RANKING DO JOGADOR ==')
for i, b in enumerate(r):
    print(f'{i+1}° lugar: {b[0]} com {b[1]}.')

