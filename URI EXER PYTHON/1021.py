v = float(input())

v100 = v // 100
v = v - v100*100

v50 = v // 50
v = v - v50*50

v20 = v // 20
v = v - v20*20

v10 = v // 10
v = v - v10*10

v5 = v // 5
v = v - v5*5

v2 = v // 2
v = v - v2*2

v1 = v // 1
v = v - v1*1

v0 = v //0.5
v = v - v0*0.50
v0=float('%.2f'% v0)
v=float('%.2f'% v)

v01 = v //0.25
v = v - v01*0.25
v01=float('%.2f'% v01)
v=float('%.2f'% v)

v02 = v //0.10
v = v - v02*0.10
v2=float('%.2f'% v2)
v=float('%.2f'% v)

v03 = v //0.05
v = v - v03*0.05
v03=float('%.2f'% v03)
v=float('%.2f'% v)

v04 = v*100
v = v - v04*0.01
v04=float('%.2f'% v04)
v=float('%.2f'% v)

print('NOTAS:')
print(f'{v100} nota(s) de R$ 100.00')
print(f'{v50} nota(s) de R$ 50.00')
print(f'{v20} nota(s) de R$ 20.00')
print(f'{v10} nota(s) de R$ 10.00')
print(f'{v5} nota(s) de R$ 5.00')
print(f'{v2} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{v1} moeda(s) de R$ 1.00')
print(f'{v0} moeda(s) de R$ 0.50')
print(f'{v01} moeda(s) de R$ 0.25')
print(f'{v02} moeda(s) de R$ 0.10')
print(f'{v03} moeda(s) de R$ 0.05')
print(f'{v04} moeda(s) de R$ 0.01')

