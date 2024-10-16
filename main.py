import math

c_o = int(input('Digite o valor do cateto oposto: '))
c_a = int(input('Digite o valor do cateto adjacente: '))

h1 = c_o * c_o
h2 = c_a * c_a
h3 = h1 + h2
h4 = math.sqrt(h3)

print(f'O valor da hipotenusa e de {h4}')
