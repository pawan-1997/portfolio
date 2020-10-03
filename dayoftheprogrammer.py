#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.


def dayOfProgrammer(year):
    leap = False

    if year > 1918:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            leap = True
    else:
        if year % 4 == 0:
            leap = True

    if leap:
        return (f'12.09.{year}')
    elif year == 1918:
        return (f'26.09.{year}')
    else:
        return (f'13.09.{year}')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
