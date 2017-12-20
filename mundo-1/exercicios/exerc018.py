import math
a = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))
print('O ângulo de {:.1f} tem o SENO de {:.1f}'.format(a, sen))
print('O ângulo de {:.1f} tem o COSSENO de {:.1f}'.format(a, cos))
print('O ângulo de {:.1f} tem a TANGENTE de {:.1f}'.format(a, tg))