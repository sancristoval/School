n1=str(input('digite a expressão: '))
n2=[]
for c in n1:
    if c=='(':
        n2.append('(')
    elif c ==')':
        if len(n2)>0:
            n2.pop()
        else:
            n2.append(')')
            break
if len(n2)==0:
    print('Sua expressão está Válida!')
else:
    print('Sua expressaõ não está Valida! ')
