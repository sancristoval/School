q=0
nome=[]
peso=[]
while True:
    
    q+=1
    nome.append(str(input('nome: ')))
    peso.append(int(input('peso: ')))
    n=str(input('quer continuar? [N\S] '))
    if n not in 'sS':
        break
print(f'Ao todo, Você cadastrou {q} pessoas. ')
print(f'O maior peso foi de {max(peso)}kg.peso de ')