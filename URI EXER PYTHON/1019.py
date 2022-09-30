s = int(input())

h = s // 60**2
s = s - h * 60**2

m =  s // 60
s = s -m*60

ss = s

print(f'{h}:{m}:{ss}')

