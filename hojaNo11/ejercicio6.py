lista=[1, 3, 5, 3, 9, 3, 7]
contador=0
buscar=3
for elemento in lista:
    if elemento == buscar:
        contador+=1
print("aparece", contador, "veces")