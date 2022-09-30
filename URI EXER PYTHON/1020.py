d = int(input())

a = d // 365
d = d - a * 365

m = d // 30
d = d - m * 30

r = d

print(f'{a} ano(s)')
print(f'{m} mes(es)')
print(f'{r} dia(s)')
