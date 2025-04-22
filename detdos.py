n=int(input("ingrese la cantidad de clientes: ")) #programa echo en clase :)
p=n
lista=[]
promedio=0
uno,dos,tres,cuatro,cinco=0,0,0,0,0
suma=0
while n!=0:
    nota=int(input("ingrese la calificacion: "))
    lista.append(nota)
    suma=suma+nota
    n=n-1
    if nota==1:
        uno+=1
    elif nota==2:
        dos+=1
    elif nota==3:
        tres+=1
    elif nota==4:
        cuatro+=1
    elif nota==5:
        cinco+=1
print(f"\nmalo: {uno} \nregular: {dos} \nbueno: {tres} \nmuy bueno: {cuatro} \nexcelente: {cinco}")
prom=suma/p
print(f"el promedio es: {prom}")

for i in lista: 
    if i <prom:
        promedio=promedio+1
print((prom*100)/suma,"% esta debajo del promedio")