from math import sin, cos, tan, radians
n=float(input('qual o ângulo que você deseja?' ))
seno=sin(radians(n))
cosseno=cos(radians(n))
tangemte=tan(radians(n))
print(f'O ângulo de {n}º tem o seno é {seno:.2f}')
print(f'O ângulo de {n}º tem o cosseno de {cosseno:.2f}')
print(f'O ângulo de {n}º tem a tangemte de {tangemte:.2f}')
