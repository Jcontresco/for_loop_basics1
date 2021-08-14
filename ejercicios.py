n = 5
m = 6

def imprime_matriz(num_filas, num_cols):
    for i in range( 0, num_filas):
        print("*" * num_cols)

imprime_matriz(n,m)

def numeros_primos(inicio, fin):
    contador = inicio
    numeros_primos = 0
    while (contador <= fin):
        divisibles = 0
        i = 1
        while (i <= contador):
            if (contador % i == 0):
                divisibles +=1
            i+=1
        if divisibles == 2:
            numeros_primos +=1
        contador +=1
    print("Entre {} y {} hay {} numeros primos".format(inicio, fin, numeros_primos))
       
numeros_primos(1,20)       





