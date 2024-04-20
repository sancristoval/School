n2=0
n1=0
for c in range(1, 7):
    n=int(input(f'digite {c} número: '))
    n2+=1
    if n % 2==0:
        n1+=n
print(f'vocẽ informou {n2} números e a soma foi {n1}')