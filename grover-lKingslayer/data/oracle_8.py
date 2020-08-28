#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

n = 10

def Uw(phi):
    w = 128
    phi[w] = -phi[w]
    return phi
