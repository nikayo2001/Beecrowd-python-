import math

lista = input().split(" ")
lista2 = input().split(" ")
x,y = lista
x2,y2 = lista2
distancia = math.sqrt(((float(x) - float(x2))*(float(x) - float(x2))) + ((float(y) - float(y2)) * (float(y) - float(y2))))
print(f'{distancia:.4f}')