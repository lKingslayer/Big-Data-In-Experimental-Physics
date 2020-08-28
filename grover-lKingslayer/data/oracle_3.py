#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

n = 6

def Uw(phi):
    w = 63
    phi[w] = -phi[w]
    return phi
