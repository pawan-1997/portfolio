matrix = []
for i in range(5):
    m = input()
    matrix.append(m)

index_i = 1
pos_i = 0
pos_y = 0

for i in matrix:
    if("1" in i):
        pos_i = index_i
        # print(pos_i)
        # print(i.find("1"))
        pos_y = i.find("1")
        # print(pos_y)
    index_i = index_i + 1

# print(pos_i)

moves = 0


def calc_i():
    if(pos_i == 1 or pos_i == 5):
        # print("In 1 5 for x")
        return 2
    elif(pos_i == 2 or pos_i == 4):
        # print("In 2 4 for x")
        return 1
    elif(pos_i == 3):
        # print("In 3 for x")
        return 0
    else:
        # print("In else for x")
        return 0


def calc_y():
    if(pos_y == 0 or pos_y == 8):
        # print("In 0 8 for y")
        return 2
    elif(pos_y == 2 or pos_y == 6):
        # print("In 2 6 for y")
        return 1
    elif(pos_y == 4):
        # print("In 4 for y")
        return 0
    else:
        # print("In else for y")
        pass


moves_i = calc_i()
moves_j = calc_y()

# print(moves_i)
# print(moves_j)

moves = moves_i + moves_j

print(moves)

# print(matrix)
