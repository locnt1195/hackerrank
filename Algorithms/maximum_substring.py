#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def maxSubstring(s):
    # Write your code here
    max_char = max(s)
    max_char_index = [i for i, v in enumerate(s) if v == max_char]
    max_sub_str = ''
    for i in range(0, len(max_char_index)):
        print(max_sub_str, s[max_char_index[i]:])
        if s[max_char_index[i]:] > max_sub_str:
            max_sub_str = s[max_char_index[i]:]
    return max_sub_str


if __name__ == '__main__':
    pass
