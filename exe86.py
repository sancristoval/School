n1=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for v in range(0, 3):
        n1[c][v]=int(input(f'digite um valor para [{c}, {v}]: '))
print('-='*30)
for c in range(0, 3):
    for v in range(0, 3):
        print(f'[{n1[c][v]:^15}]',end='')
    print()