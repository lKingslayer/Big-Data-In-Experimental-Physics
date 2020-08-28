#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

n = 4

def Uw(phi):
    w = 15
    phi[w] = -phi[w]
    return phi
