print('-='*55)
print('analisador de triângulos')
print('-='*55)
n1=float(input('primeiro seguimento; '))
n2=float(input('segundo seguimetno: '))
n3=float(input('tersero seguimento: '))
if n1>=n2+n3 and n2>=n1+n3 and n3>=n1+n2:
    print('Os seguimentos acima PODEM FORMAR triângulos! ')
else:
    print('Os seguimentos a seguir NÃO PODEM FORMAR triãngulo! ')

