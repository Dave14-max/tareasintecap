def cuenta_ascendente(n, int=1):
    if  int > n:
        return
    print(int)
    cuenta_ascendente(n, int + 1)
        
cuenta_ascendente(4)