import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = (co**2) + (ca**2)
raiz = math.sqrt(hip)
print('A hipotenusa vai medir {:.2f}'.format(raiz))