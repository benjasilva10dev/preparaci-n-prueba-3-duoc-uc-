import os 
os.system("cls")
import random

# Inicialización de contadores y acumuladores
contador_agua = 0
contador_planta = 0
contador_fuego = 0
contador_victorias = 0
contador_derrotas = 0
suma_poder = 0
poder_legendario = False 


cantidad_combate_correcta = False
while cantidad_combate_correcta == False:
    cantidad_combate = int(input("Escriba la cantidad de combates: "))
    if cantidad_combate > 0:
        cantidad_combate_correcta = True
    else:
        print("La cantidad de combates debe ser mayor a 0.")


for x in range(cantidad_combate):
    print(f"--- Combate {x+1} ---")
    
    
    nombre = input("ESCRIBA EL NOMBRE DEL ENTRENADOR: ")
    
    
    tipo_pokemon = input("Escriba la inicial del tipo (F: Fuego, A: Agua, P: Planta): ").upper()
    while tipo_pokemon not in ["F", "A", "P"]:
        print("Tipo no válido.")
        tipo_pokemon = input("Escriba la inicial (F, A o P): ").upper()

    
    poder = random.randint(1, 20)
    
    
    if tipo_pokemon == "F":
        poder += 3
        contador_fuego += 1
    elif tipo_pokemon == "A":
        poder += 2
        contador_agua += 1
    else:
        poder += 1
        contador_planta += 1

    
    suma_poder += poder

    
    if poder >= 25:
        poder_legendario = True

    
    if poder >= 18:
        estado = "Victoria"
        contador_victorias += 1
    elif poder >= 10:
        estado = "Batalla dificil"
    else:
        estado = "Derrota"
        contador_derrotas += 1

    print(f"Entrenador: {nombre} | Poder Final: {poder} | Resultado: {estado}")


print("\nESTADÍSTICAS FINALES")
print(f"Total de combates: {cantidad_combate}")
print(f"Cantidad de victorias: {contador_victorias}")
print(f"Cantidad de derrotas: {contador_derrotas}")
print(f"Cantidad de Pokémon Fuego: {contador_fuego}")
print(f"Cantidad de Pokémon Agua: {contador_agua}")
print(f"Cantidad de Pokémon Planta: {contador_planta}")
promedio = suma_poder / cantidad_combate
print(f"Promedio de poder final: {promedio}")


if poder_legendario:
    print("¡Hubo un Pokémon legendario en el torneo!")
                    
        

