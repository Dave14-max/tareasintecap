lista=[5, 10, 15, 20]
lista_invertida=[]
for i  in range(len(lista)-1, -1, -1):
    lista_invertida.append(lista[i])
print("lista invertida:", lista_invertida)