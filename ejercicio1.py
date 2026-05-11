suma = 0
menu_valido = True

import os 
os.system("cls")

while menu_valido:
    print("------------MENÚ---------")
    print("1. Contar del 1 al N")
    print("2.  Mostrar números pares")
    print("3. Tabla de multiplicar")
    print("4. salir ")
    print("5. suma")

    try:
        eleccion = int(input("escoja su elección"))
        while eleccion not in [1,2,3,4,5]:
            eleccion = int(input("escoja su elección"))
        
        if eleccion == 1:
            n = int(input("escriba el numero"))
            for x in range (1,n + 1):
                print(x)
        
        elif eleccion == 2:
            n = int(input("escriba el numero"))
            for x in range (1,n,2):
                print(x+1)
        
        elif eleccion == 3:
            n = int(input("escriba el numero"))
            for x in range (1,11):
                print(F"{n} X {x} = {n * x}")
        
        elif eleccion == 4:
            print("programa finalizado")
            break

        else:
            n = int(input("escriba el numero"))
            for x in range (n + 1):
                suma += x
            print(f" la suma es {suma}")
        
    except:
        print("datos invalidos")
    
    
    
    
    
    
