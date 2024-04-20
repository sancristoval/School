n=[]
for c in range(0,5):
    m=int(input('digite um número: '))
    if c==0 or m>n[-1]:
        n.append(m)
        print('Adicionado ao final da lista...')
    else:
        v=0
        while v <len(n):
            if m <=n[v]:
                n.insert(v,m)
                print(f'Adicionado na posiçaõ {v} da lista...')
                break
            v+=1

print('-='*30)
print(f'Os valores digitados em ordem foram {n}')

