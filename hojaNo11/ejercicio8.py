numeros=[11, 22, 33, 44]
buscar=33
encontrado=False
for n in numeros:
    if n == buscar:
        encontrado=True
        break
if encontrado:
    print("si está en la lista")
else:
    print("no se encontró")
