n=('aprender','programar','linguagem','python','curso','gratis','praticar','tabalhhar','mercado','programor','futuro')
for c in n:
    print(f'\nNa palavra {c} temos ',end='')
    for m in c:
        if m.lower() in 'aeiou':
            print(m,end=' ')
print('')