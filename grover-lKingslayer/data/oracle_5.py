#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

n = 7

def Uw(phi):
    w = 0
    phi[w] = -phi[w]
    return phi
