#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import numpy as np
from oracle import Uw
from oracle import n

# A hadamard gate for one qubit
H = np.array([[1, 1], [1, -1]] / np.sqrt(2))


# TODO: In this function, you can generate a hadamard gate capable of
# processing n qubit system
# HINT: you can use functions of numpy library
def genHn(n):
    """Realization of hadamard door"""
    Hn = H.copy()
    for _ in range(n - 1):
        Hn = np.kron(Hn, H.copy())
    return Hn


Hn = genHn(n)

# complex number is not necessary here
x = np.zeros((2 ** n), dtype=np.float64)
x[0] = 1
s = Hn.dot(x)


# TODO: Implement Us
def Us(phi):
    """Realization of Us"""
    u_s = 2 * np.outer(s, s) - np.eye(s.ndim)
    phi = u_s.dot(phi)
    return phi


# TODO: calculate T and fullfil the computation process
T = 0

T = int(np.pi * np.sqrt(2 ** n) / 4)

phi = s

for _ in range(T):
    phi = Uw(phi)
    phi = Us(phi)

phi = np.abs(phi)

# TODO: print the argmax of abs of one array
print(np.argmax(phi))
