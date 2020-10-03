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
        print("Adding")
    elif(stmt == "X--" or stmt == "--X"):
        x = x - 1
        print("Subtracting")
    else:
        pass

print(x)
