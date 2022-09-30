# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item.
#  A seguir, calcule e mostre o valor da conta a pagar.



# Entrada
# O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade
#  de um item conforme tabela acima.

# Saída
# O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, 
# com 2 casas após o ponto decimal.

list = input().split()

c, q = list

c = float(c)
q = float(q)
t = 0

if c == 1:
  t = q * 4.00

if c == 2:
  t = q * 4.50

if c == 3:
  t = q * 5.00

if c == 4:
  t = q * 2.00

if c == 5:
  t = q * 1.50

print(f'Total: R$ {t:.2f}')