#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'degreeOfArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def degreeOfArray(arr):
    # Write your code here
    values_dict = {}
    # print(arr)
    duplicated = False
    for i, v in enumerate(arr):
        if v not in values_dict:
            values_dict[v] = [i, 0, 0]
        else:
            duplicated = True
            values_dict[v][1] = i
            values_dict[v][2] += 1

    if not duplicated:
        return 1

    max_degree = 0
    min_length = len(arr)
    for k, v in values_dict.items():
        lt = v[1] - v[0]
        degree = v[2]
        if l > 0:
            if degree > max_degree or (degree == max_degree and lt < min_length):
                min_length = l + 1
                max_degree = degree

    return min_length


if __name__ == '__main__':
    pass
