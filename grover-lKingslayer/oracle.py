#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

n = 5

def Uw(phi):
    w = 2
    phi[w] = -phi[w]
    return phi
