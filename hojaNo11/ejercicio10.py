lista=[4, 5, 4, 7, 5, 8, 4]
lista_sin_duplicados=[]
for n in lista:
    if n not in lista_sin_duplicados:
        lista_sin_duplicados.append(n)
print("lista limpia:", lista_sin_duplicados)