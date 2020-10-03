
import math
import os
import random
import re
import sys


def rotateLeft(d, arr):
    for j in range(d):
        for i in range(len(arr)):
            if(i > 0):
                arr[i-1] = arr[i]
            elif(i == 0):
                temp = arr[i]

        arr[len(arr)-1] = temp
    return arr


n, d = input().split()
n = int(n)
d = int(d)
arr = []

t = input().split(" ")
arr.append(t)

res = rotateLeft(d, arr)

print(res)
