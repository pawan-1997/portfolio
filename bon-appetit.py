import math
import os
import random
import re
import sys


def bonAppetit(bill, k, b):
    # did_not_eat = bill[k]
    s = 0
    for i in range(len(bill)):
        if i != k:
            s += bill[i]

    s = s//2

    if s == b:
        print("Bon Appetit")
    else:
        print(b - s)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
