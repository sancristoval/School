print('gerador de pa')
print('-='*20)
n1=int(input('primeiro valor'))
n2=int(input('razão da pa'))
n4=n1
n3=1
while n3<=10:
    print(f'{n4} → ',end='')
    n4+=n2
    n3+=1
print('Fim')
