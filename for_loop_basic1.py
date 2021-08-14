#Básico : imprime todos los enteros del 0 al 150.

'''
for x in range(0, 151,):
    print(x)
'''

#Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000    

'''
for y in range(5, 1001, 5):
    print(y)
'''

#Contar, Dojo Way - imprime enteros del 1 al 100. Si es divisible por 5, imprima "Coding" en su lugar. Si es divisible por 10, imprima "Coding Dojo".

''' 
for z in range(0, 101):
    if z % 10 == 0:
        print('Coding Dojo')
        continue 
    elif z % 5 == 0 :
        print('Coding')
    else:
        print(z)
'''

#¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.

'''
#num = 500000
num = int(input("Please, enter a number:"))
total = 0

for i in range(0, num + 1):

    if i % 2 != 0:
        total += i
    
print("Suma de los valores impares en el rango 1 a {} is {}".format(num,total))
'''

#Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
'''
num = 2018
for i in range(0,num+1,--4):
    print(" ", num-i)
'''

#Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)

'''
lowNum = 2 #int(input("Ingrese el numero menor:"))
highNum = 9 #int(input("Ingrese el numero mayor:"))
mult = 3 #int(input("Ingrese el multiplo que desea condicionar:"))

for n in range(lowNum, highNum+1):

    if n % mult == 0:
        print(n)
'''

#BONUS: ¿Cómo se puede detectar si un número es primo? ¿Cómo retornar una lista con los primos entre el 1 y el 1000?

# OP 1
'''
lowNum = 1
highNum = 1000

while lowNum <=highNum:
    contador = 1
    x = 0
    while contador <= lowNum:
        if lowNum % contador == 0:
            x=x+1
        contador = contador + 1

    if x == 2:
        print(lowNum)

    lowNum = lowNum + 1    
'''
#OP 2
'''
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
       
numeros_primos(1,1000)
'''
#FIM
