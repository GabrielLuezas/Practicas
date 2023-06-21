import random

print ("Hola Mundo")

if 5 > 2:
    print("5 Es mucho mejor que 2")

#Esto son variables
x= "Variable 1"
y= "Variable 2"
print(x)
print(y)

"""
Comentario
De mas
de una linea
"""

def myfunc():
  global x
  x = "Fantastico"

myfunc()


print (x)

randomnumero= random.randrange(1, 10)

print(randomnumero)

prueba="""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries,
but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

print(prueba)

for p in "Gabriel":
  print(p)

lista = ["planta", "agua", "fuego"]
print(lista)

frutas = ["manzana", "platano", "mandarina"]
i = 0
while i < len(frutas):
  print(frutas[i])
  i = i + 1