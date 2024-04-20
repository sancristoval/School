n2=n1=0
while True:
    n=int(input('digite um valor [999 para parar]: '))
    if n==999:
        break
    n1+=n
    n2+=1
print(f'A soma dos {n2} valores foi {n1}')
