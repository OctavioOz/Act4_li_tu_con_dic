arcoiris=("Azul", "Verde", "Rojo", "amarillo")
print(arcoiris)
print("--Longitud arcoiris--")
print(len(arcoiris))

print("")

animales=("Pantera", 20, "estatura", 1.7)
print(animales)
print("Elementos tuplas")
print(animales[2])

print("")

rateros = ("Juan", "Ana", "Pedro")
y = list(rateros)
y[0] = "polainas"
x = tuple(y)

print(x)

print("")

print("Agregando elementos")
Nanimal=("Boby", "Chetos")
y = list(Nanimal)
print(y)
y.append("tontolin")
otradupla = tuple(y)

print(otradupla)

print("Uso de for en tuplas")
for elcolor in arcoiris:
    print(elcolor)