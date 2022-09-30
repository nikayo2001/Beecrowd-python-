

v = int(input())
print(v)
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

print(f'{v100} nota(s) de R$ 100,00')
print(f'{v50} nota(s) de R$ 50,00')
print(f'{v20} nota(s) de R$ 20,00')
print(f'{v10} nota(s) de R$ 10,00')
print(f'{v5} nota(s) de R$ 5,00')
print(f'{v2} nota(s) de R$ 2,00')
print(f'{v1} nota(s) de R$ 1,00')