#!/usr/bin/env python3


import sys
import math


def factorial(begin):
    ret = 1
    while (begin > 0):
        ret *= begin
        begin -= 1
    return ret


def get_identity_matrix(size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        matrix.append(row)
    for i in range(size):
        matrix[i][i] = 1
    return matrix


def error_checker():
    numbers = len(sys.argv) - 2
    int_squareroot = int(math.sqrt(numbers))
    if math.pow(int_squareroot, 2) != numbers:
        sys.stderr.write("worong number or arguments\n")
        sys.exit(84)
    return int_squareroot


def my_help():
    print("USAGE\n"
          "\t./108trigo fun a0 a1 a2....\n"
          "\n"
          "DESCRIPTION\n"
          "\tfun\tfunction to be applied,"
          ' among at least "EXP", "COS", "SIN", "COSH" and "SINH"\n'
          '\tai\tcoeficients of the matrix')
    sys.exit(0)


def check_parameters():
    try:
        possible = ["EXP", "COS", "SIN", "COSH", "SINH"]
        if len(sys.argv) == 2 and (sys.argv[1] == "--help" or sys.argv[1] == "-h"):
            my_help()
        if len(sys.argv) <= 2 or sys.argv[1] not in possible:
            sys.stderr.write("wrong Arguments\n")
            sys.exit(84)
        for i in range(2, len(sys.argv)):
            sys.argv[i] = float(sys.argv[i])
        return error_checker()
    except ValueError:
        sys.stderr.write("at least one argument is no number\n")
        sys.exit(84)


def print_matrix(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print("%.2f%c" % (tab[i][j], '\t' if (j != len(tab[i]) - 1) else '\n'), end="")