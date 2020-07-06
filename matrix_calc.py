#!/usr/bin/env python3

import math
import sys


def add_matrizen(mat1, mat2):
    tmp = []
    for i in range(len(mat1)):
        c = []
        for j in range(len(mat1[0])):
            c.append(mat1[i][j] + mat2[i][j])
        tmp.append(c)
    return tmp


def mult_matritzen(matrix_1, matrix_2):
    ret = []
    for i in range(len(matrix_1)):
        mult = []
        for j in range(len(matrix_1)):
            a = 0
            for k in range(len(matrix_1)):
                a += matrix_1[i][k] * matrix_2[k][j]
            mult.append(a)
        ret.append(mult)
    return ret


def pow_matrix(mat, n):
    tmp = mat
    for i in range(n - 1):
        tmp = mult_matritzen(tmp, mat)
    return tmp


def div_matrix(mat, k):
    for i in range(len(mat)):
        for j in range(len(mat)):
            mat[i][j] /= k
    return mat


def sub_matritzen(mat1, mat2):
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat2[i][j] = mat1[i][j] - mat2[i][j]
    return mat2
