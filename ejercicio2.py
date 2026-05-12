import os
os.system("cls")
acumulador_deposito = 0
acumulador_total = 0
while True:
    print("========= BANCO FINANCIERO =========")
    print("1. Mostrar cuotas de ahorro")
    print("2. Simular depósito acumulado")
    print("3. Tabla de crédito")
    print("4. Contar clientes atendidos")
    print("5. Salir")
    
        
    try:
            opcion_cliente = int(input("escriba la opcion a elegir del menú"))
            while opcion_cliente not in [1,2,3,4,5]:
                print("opcion no valida")
                opcion_cliente = int(input("escriba la opcion a elegir del menú"))
            
            
            if  opcion_cliente == 1:
                ahorro_mensual = 0
                cantidad_meses = 0
                while ahorro_mensual <= 0:
                    ahorro_mensual = int(input("Ingrese ahorro mensual: "))
                for x in range (cantidad_meses + 1):
                    ahorro_mensual = int(input("Ingrese ahorro mensual: ")) 
                print(F"mes {cantidad_meses + 1} : {ahorro_mensual}")
                
            
            elif opcion_cliente == 2:
                deposito = int(input("Ingrese depósito: "))
                cantidad_meses_deposito = int(input("escriba cantidad de meses"))
                for i in range (cantidad_meses_deposito + 1):
                    deposito = int(input("Ingrese depósito: "))
                    print(F"mes {i+1} : {deposito} ")
                    acumulador_deposito += 1
                    acumulador_total += deposito
                print(f"total acumulado : {acumulador_deposito}")
                print(F"cantidad de depósitos : {acumulador_deposito}")
        
        
            elif opcion_cliente == 3:
                monto_credito = int(input("Ingrese monto del crédito: "))
                for z in range (1,12 +1):
                    print(F"{z} X {monto_credito} = {z * monto_credito}")
                
            elif opcion_cliente == 4:
                cantidad_clientes = int(input("Ingrese cantidad de clientes: "))
                for y in range (cantidad_clientes):
                    print(F"Cliente atendido N°{y + 1}")
        
        
            else:
                print("Gracias por utilizar el sistema financiero")
                break
    except:
        print("Datos invalidos")        
                    
            
                
            
        
