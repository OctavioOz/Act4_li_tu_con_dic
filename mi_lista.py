#Ejemplos de uso de listas
misnovias=["Agripina", "Anastacia", "Maria"]
misNumeros=["666", "77", "10"]
#Mostrando mis novias
print(misnovias)
#Mostrando mis numeros
print(misNumeros)
print("--accediendo a los elementos de la lista--")
print(misnovias[-2])
if "Ana" in misnovias:
    print("Si,'Ana' esta en la lista de mis novias")
else:
    print("Chale no eres mi novia")
    print("Numeros de novias")
    Nnovias=len(misnovias)
    print(f"Numero de novias = {Nnovias}")
    posicion=0
    print("Ciclo for en listas")
    for medianaranja in misnovias:
        print(posicion," ", medianaranja)
        posicion=posicion+1