while True:
    n=int(input('quer ver a tabuada de qual valor? '))
    if n>=0:
        print('-'*20)
        for c in range(1,11):
            print(f'{n} x {c} = {(n)*c}')
        print('-'*20)
    if n<=-1:
        break
print('PROGAMA TABUADA ENCERRADO. Volte senpre!')
