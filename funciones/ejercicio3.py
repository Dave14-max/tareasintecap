#cuenta regresiva
def cuenta_regresiva(n):
    if n <0:
        print("despegue")
    else:
        print(n)
        cuenta_regresiva(n-1)
cuenta_regresiva(5)