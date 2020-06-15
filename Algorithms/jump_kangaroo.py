#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    #         0   3   4   2
    #         0   2   5   3
    #        21   6  47   3 => (47 - 21) / (6 - 3) = 26 / 3
    # S = x1 + v1.t
    # S = x2 + v2.t
    # x1 + v1.t = x2 + v2.t
    # v1.t - v2.t = x2 - x1
    # t = (x2 - x1) / (v1 - v2)
    res = ''
    diff_x = x2 - x1
    diff_v = v2 - v1
    if diff_x == 0:
        if diff_v == 0:
            res = "YES"
        else:
            res = "NO"
    else:
        if diff_v >= 0:
            res = "NO"
        else:
            if abs(diff_x) % abs(diff_v) == 0:
                res = "YES"
            else:
                res = "NO"
    return res


if __name__ == '__main__':
    x1V1X2V2 = [1, 2, 3, 4]

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result + '\n')
