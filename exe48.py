n=0
n2=0
for c in range(1,501,2):
    if c%3==0:
        n2+=1
        n+=c
print(f'A soma de todos os {n2} valores solicitados é {n}')