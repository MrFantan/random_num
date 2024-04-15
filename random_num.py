import random

print('Número Random')
print('-------------')
print('Número inicial es: 1')

# Solicitar numero final
inicio = 1
final = int(input('último número: '))


numero_aleatorio = random.randint(inicio, final)

print("Número aleatorio entre", inicio, "y", final, "es: ", numero_aleatorio)
