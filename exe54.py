from datetime import date
n=date.today().year
m1=int(input('quantas pessoas você quer saber se é maior de idade: '))
n2=0
n3=0
for c in range(1, {m1}):
    n1=int(input(f'em que ano a {c}° pessoa naceu? '))
    m=n-n1
    if m >= 21:
        n2+=1
    else:
        n3+=1
print(f'ao todo tivemos {n2} pessoas maiores de idade')
print(f'é tivemos {n3} pessoas maiores de idade')
