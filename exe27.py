n=str(input('digite seu nome completo: ')).upper().strip()
n1=n.split()
print(f'seu primeiro nome é {n1[0]}')
print(f'seu ultimo nome é {n1[len(n1)-1]}')
