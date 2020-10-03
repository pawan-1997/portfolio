a, b = input().split()
a = int(a)
b = int(b)

years = 0

for i in range(b):
    a = a*3
    b = b*2
    if(a > b):
        years = i + 1
        break

print(years)
