#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

n = 8

def Uw(phi):
    w = 144
    phi[w] = -phi[w]
    return phi
