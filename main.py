#!/usr/bin/env python3


import sys
import math
from calc import *
from additional import *


def main():
    root = check_parameters()
    ar = []
    new = []
    i = 2
    while (i < len(sys.argv)):
        for j in range(root):
            new.append(sys.argv[i])
            i += 1
        ar.append(new)
        new = []
    get_calc(ar, root)
