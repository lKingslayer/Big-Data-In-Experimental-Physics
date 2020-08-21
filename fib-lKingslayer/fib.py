#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''This code is to calculate the nth fibonacci number'''


# input
N = int(input())


def fibonacci(num):
    '''Takes in a number, returns the corresponding fibonacci number'''
    if num < 0:
        raise ValueError("Negative arguments not implemented")
    return fib(num)[0]


def fib(num):
    '''Takes in a number, return the tuple (F(n), F(n+1))'''
    if num == 0:
        return 0, 1
    else:
        matrix_a, matrix_b = fib(num // 2)
        matrix_c = matrix_a * (matrix_b * 2 - matrix_a)
        matrix_d = matrix_a * matrix_a + matrix_b * matrix_b
        if num % 2 == 0:
            return matrix_c, matrix_d
        return matrix_d, matrix_c + matrix_d


# print the nth Fibonacci number
print(fibonacci(N))
