# 1. TAREA: imprimir "Hola mundo"
print( 'Hellow World' )
# 2. imprimir "Hola Noelle!" con el nombre en una variable
name = "Noelle"
print("Hola", name)	# con una coma
print("Hola "+ name) # con un +
# 3. imprimir "Hola 42!" con un numero en una variable
name1 = 42
print("Hola", name1) # con una coma
print("Hola "+ str(name1))	# con un + - !Este debería darnos un error!
# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("Me encanta comer {} and {}".format(fave_food1, fave_food2)) # con .format()
print("Me encanta comer %s and %s" %(fave_food1, fave_food2)) # con una cadena f
# 5. Bonus Ninja
altura = 1.80
print("Hola mi nombre es %s, tengo %i y mido %f, me encanta comer %s and %s." %(name, name1, altura, fave_food1, fave_food2))