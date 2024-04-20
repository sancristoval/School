n=str(input('digite uma frase: ')).upper().strip()
print(f'a letra A aparesel {n.count("A")} vezes na frase ')
print(f'A primeira letra A aparesel na posição {n.find("A")+1}')
print(f'A ultima letra A aparecel na posição {n.rfind("A")+1}')
