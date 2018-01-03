#Implementing fuzzy connectives and tranferefunctions

import numpy as np

#Fuzzy logic connectives

def fuzzyNot(u):
    return 1.0 - u

def fuzzyAnd(u, v):
    if u < v:
        return u
    else:
        return v

def fuzzyOr(u, v):
    if u > v:
        return u
    else:
        return v

def fuzzyImplication(u, v):
    value = 1.0 - u + v
    if value < 1.0:
        return value
    else:
        return 1.0

def fuzzyEquivalence(u, v):
    return 1.0 - abs(u - v)


#Transefere functions

def sigmoid(x, zeroOffset):
    x -= zeroOffset
    return 1.0 / (1.0 + np.exp(- x))

def piecewiseLinear(x, low, high):
    if x < low:
        return 0.0
    elif x > high:
        return 1.0
    else:
        m = 1.0 / (high - low)
        return m * (x - low)
    

