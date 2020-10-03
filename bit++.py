n = input()
n = int(n)
statements = []
x = 0

for i in range(n):
    s = input()
    statements.append(s)

for stmt in statements:
    if(stmt == "X++" or stmt == "++X"):
        x = x + 1
    elif(stmt == "X--" or stmt == "--X"):
        x = x - 1
    else:
        pass

print(x)
