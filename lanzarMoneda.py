import random
print('Lanzare una moneda 1000 veces. Adivina cuantas veces caera Cara. (Presiona enter para comenzar)')
input()
lanzamientos = 0
caras = 0
while lanzamientos < 1000:
    if random.randint(0, 1) == 1:
        caras = caras + 1
    lanzamientos = lanzamientos + 1

    if lanzamientos == 900:
        print('900 lanzamientos y hubo ' + str(caras) + ' caras.')
    if lanzamientos == 100:
        print('En 100 lanzamientos, cara salio ' + str(caras) + ' veces.')
    if lanzamientos == 500:
        print('La mitad de los lanzamientos y cara salio ' + str(caras) + ' veces.')

print()
print('De 1000 lanzamientos, al final cara sali ' + str(caras) + ' veces!')
print('Â¿Estuviste cerca?')
