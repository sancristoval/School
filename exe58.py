from random import choice
m1=0
list=(1,2,3,4,5,6,7,8,9,10)
n=choice(list)
print('Seu seu computador...')
print('Acabei de pensar um número entre 0 e 10. \n Sera que você consegue adivivhar qual foi?')
m=int(input('qual é seu palpite? '))
while m!=n:
    if m<n:
        n1='mais'
    if m>n:
        n1='menos'
    m1+=1
    if m!=n:
        print(f'{n1} tente mais uma vezes.')
    m=int(input('qual é seu palpite? '))
    if m==n:
        print(f'acertou com {m1+1} tentativas. parabéns!')
