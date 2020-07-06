#!/usr/bin/env python3

from matrix_calc import *
from additional import *
import sys
import math


def get_calc(matrix, size):
    func = sys.argv[1]
    out = []
    if (func == "EXP"):
        out = calc_exp(matrix, size)
    if (func == "COS"):
        out = calc_cos(matrix, size)
    if (func == "SIN"):
        out = calc_sin(matrix, size)
    if (func == "COSH"):
        out = calc_cosh(matrix, size)
    if (func == "SINH"):
        out = calc_sinh(matrix, size)
    print_matrix(out)


def calc_exp(matrix, size):
    ret = get_identity_matrix(size)
    for i in range(1, 80): #if there are problems --> end of loop smaller
        pow_v = pow_matrix(matrix, i)
        div_v = div_matrix(pow_v, factorial(i))
        ret = add_matrizen(ret, div_v)
    return ret


def calc_cos(matrix, size):
    try:
        ret = get_identity_matrix(size)
        for i in range (1, 80): #if there are problems --> end of loop smaller
            pow_v = pow_matrix(matrix, 2 * i)
            div_v = div_matrix(pow_v, factorial(2 * i))
            if i % 2 == 0:
                ret = add_matrizen(ret, div_v)
            else:
                ret = sub_matritzen(ret, div_v)
        return ret
    except ValueError:
        exit(84)


def calc_cosh(matrix, size):
    ret = get_identity_matrix(size)
    for i in range (1, 80): #if there are problems --> end of loop smaller
        pow_v = pow_matrix(matrix, i * 2)
        div_v = div_matrix(pow_v, factorial(i * 2))
        ret = add_matrizen(ret, div_v)
    return ret


def calc_sin(matrix, size):
    ret = matrix
    for i in range(1, 40):  # if there are problems --> end of loop smaller
        pow_v = pow_matrix(matrix, 2 * i + 1)
        div_v = div_matrix(pow_v, factorial(2 * i + 1))
        if i % 2 == 0:
            ret = add_matrizen(ret, div_v)
        else:
            ret = sub_matritzen(ret, div_v)
    return ret


def calc_sinh(matrix, size):
    ret = matrix
    for i in range (1, 80): #if there are problems --> end of loop smaller
        pow_v = pow_matrix(matrix, i * 2 + 1)
        div_v = div_matrix(pow_v, factorial(2 * i + 1))
        ret = add_matrizen(ret, div_v)
    return ret

