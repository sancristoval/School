n1=('xero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
    'onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    n2=int(input('digite um número entre 0 e 20: '))
    if 0<=n2<=20:
        print('Tente novamente. ',end='')
        print(f'Você digitou o número {n1[n2]}')
    n3=str(input('quer continuar? [N\S]'))
    if n3 in 'Nn':
        break