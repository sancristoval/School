import random
n1=str(*input('qual o nome do primeiro aluno? '))
n2=str(input('qual o nome do segundo aluno? '))
n3=str(input('qual o nome do terseiro aluno? '))
n4=str(input('qual o nome do qualrto aluno? '))
list=[n1, n2, n3, n4]
iscolia=random.choices(list)
print(f'o aluno sorteado foi: {iscolia}  ')
