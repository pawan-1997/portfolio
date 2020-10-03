u = input()

distinct = set(u)

if(len(distinct) % 2 == 0):
    print("It's a girl")
    print("CHAT WITH HER!")
else:
    print("It's a boy")
    print("IGNORE HIM!")

