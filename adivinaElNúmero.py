# Este es el uego de adivinar el numero.
import random 

intentosRealizados = 0

print('Hola! Como te llamas?')
miNombre = input()

numero = random.randint(1, 20)
print('Bueno, ' + miNombre + ', estoy pensando un numero entre el 1 y el 20.')

while intentosRealizados < 6:
    print('Intenta adivinar.') #tab delante del print
    estimacion = input()
    estimacion = int(estimacion)

    intentosRealizados = intentosRealizados + 1

    if estimacion < numero:
        print('Tu estimacion es muy baja.')
        
    if estimacion > numero:
        print('Tu estimacion es muy alta')
        
    if estimacion == numero:
        break
    
if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('Buen trabajo, ' + miNombre + '! Haz adivinado mi numero en ' + intentosRealizados + ' intentos!')

if estimacion != numero:
        numero = str(numero)
        print('Pues no. El numero que estaba pensando era ' + numero)
        
