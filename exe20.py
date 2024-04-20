from random import shuffle
n1=str(input('primeiro aluno:  '))
n2=str(input('segundo aluno:  '))
n3=str(input('treseiro aluno:  '))
n4=str(input('qualrto aluno:  '))
list=[n1, n2, n3, n4 ]
shuffle(list)
print(f'A orden de apresentação é {list}')