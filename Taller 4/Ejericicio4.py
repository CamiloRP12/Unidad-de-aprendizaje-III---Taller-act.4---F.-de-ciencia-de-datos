#Crea un programa en Python que permita adivinar un número. La aplicación genera un
#número aleatorio del 1 al 100. A continuación, va pidiendo números y va respondiendo si
#el número a adivinar es mayor o menor que el introducido, así como el número de intentos
#que quedan, se contarán con 10 intentos para adivinar el número). El programa termina
#cuando se acierta el número y debe indicar en que intento fue acertado, si se llega al límite
#de intentos, el programa debe mostrar que se había generado.

#Lo primero será importar la librería de random para poder generar números al azar
import random
#Adicional se usará randint para que el número al azar este entre dos límites y sea un entero, y de paso para generar un número
#diferente para cada intento
numero_de_la_loteria=random.randint(1,100)

intentos_restantes=10

print("\nBuen día, beinvenido a la loteria, donde hallar el número ganador puede volverlo millonario!")
print("Cuenta con 10 intentos para adivinar el número ganador, el cual estará entre el 1 y el 100")

#Acá se creará el bucle con el cual se le darán los intentos al usuario. La variable indica que intentos_restantes debe ser
#mayor a 0, el bucle se acabará.
while intentos_restantes>0:
    #Al igual que en los otros ejercicios, se usará try-except para evitar que el progama se detenga abruptamente
    #si es que el usuario brinda información que no coincida con lo estipulado en el juego
    try:
        #Int se usará para que la entrada dada por el usuario se convierta en número entero
        intento=int(input(f"\nPor favor introduzca el número que desea jugar(Intentos restantes:{intentos_restantes}): "))

        #Se colocará una primera condición donde se restará un intentoasí el usuario use un número menor a 1 o mayor a 100
        if intento<1 or intento>100:
            print("Por favor tenga presente que el rango de número es de 1 a 100")
            continue
        intentos_restantes-=1
        
        #Se colocará una segunda condición donde tambien se restará un intento, dando una respuesta diferente dependiendo
        #de si el usuario acierta o no al número ganador. Der ganar o gastar los intentos el break interrumpirá el bucle
        if intento==numero_de_la_loteria:
            print(f"\n¡¡¡Felicidades!!! Es usted uno de nuestros afortunados ganadores!!! Adivinar el número solo\
 le tomo {10-intentos_restantes} intentos")
            break

        elif intento<numero_de_la_loteria:
            print("\nEl número elegido no es el correcto, pero le daré una pista, el número ganador es mayor al que\
 usted eligió")
        else:
            print("\nEl número elegido no es el correcto, pero le daré una pista, el número correcto es menor al que\
 usted eligió")
    except ValueError:
        print("\nRecuerda que debes ingresar un número válido!")

#Una vez agotados los 10 intentos, el bucle se denetrá e imprimirá este mensaje
if intentos_restantes==0:
    print(f"\nLo sentimos, has utilizado todos tus intentos. El número ganador era {numero_de_la_loteria}!")