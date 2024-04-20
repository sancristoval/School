n1=0
n2=0
n=int(input('digite um número [999 para parar]: '))
while n !=999:
    n1+=1
    n2+=n
    n=int(input('digite um número [999 para parar]: '))
print(f'você digitou {n1} números e a soma entre eles foi {n2}')
