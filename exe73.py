n1=('Corintinas','Palmeiras','Santos','Grêmio','cruzeiro','Flamengo','Vasco','Chapecoense',
    'Atlético','Botafogo','Atletico-PR','Bhaia','São Paulo','Fluminense','Sport Recifr','EC Vitória',
    'Coritiba','Avaí','Ponte Oreta','Atlético-GO')
print('-='*15)
print(f'lista de times do Brasileirão: {n1}')
print('-='*15)
print(f'Os 5 primeiros são {n1[0:5]}')
print('-='*15)
print(f'Os 4 últimos são {n1[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(n1)}')
print('-='*15)
print(f'O chapecoense está na {n1.index("Chapecoense")+1} posição')