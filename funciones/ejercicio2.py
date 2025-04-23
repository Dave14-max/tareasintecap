#Crea una función suma_lista(lista) que reciba una lista de números y devuelva la suma total.
#def suma_lista(lista):
#    a=int(input("ingrese el valor: "))
#    b=int(input("ingrese el valor: "))
#    c=int(input("ingrese el valor: "))
#    print(f"la suma total es: {a+b+c}")
#suma_lista(1)  

def suma_lista(lista):
    return sum(lista)
result = suma_lista([1, 2, 3])
print("el resultado es: ", result)