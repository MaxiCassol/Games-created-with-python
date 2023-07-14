peso = input("Cuanto pesas?")
altura = input('Cual es tu altura en metros?')
imc = round(float(peso)/float(altura)**2,2)
print("El indice de masa corporal es: " + str(imc))
