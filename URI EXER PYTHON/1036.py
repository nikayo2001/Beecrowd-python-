

list = input().split()

a, b, c = list

a = float(a)
b = float(b)
c = float(c)

delta = (b**2) - 4 * a * c

if a == 0 and delta < 0:
  print("Impossivel calcular")
else:
  x1 = (-b + delta**(1 / 2)) / (2 * a)
  x2 = (-b - delta**(1 / 2)) / (2 * a)

print(f'R1 = {x1:.5f}\nR2 = {x2:.5f}')
