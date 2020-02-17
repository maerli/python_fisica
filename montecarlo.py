#from __future__ import xrange
#monte carlo method module
#https://www.ime.usp.br/~viviane/MAP2212/integralmc.pdf
from random import random
import math
PI = math.pi

rand = lambda a,b: a + (b-a)*random()
def monte_carlo(f,a,b,N=10):
    s = 0
    i = 0
    print("waiting ...")
    while i < N:
        s = s + f(rand(a,b))
        i = i + 1
    return (b-a)*(1/N)*s
#f = lambda x: 4.0/(1 + x**2)
def f(x):
    media = 0
    desvio = 1.0
    p = (1.0/(desvio*math.sqrt(2*math.pi)))*math.exp(-(1/2.0)*((x - media)/(desvio))**2)
    return p

#integral = monte_carlo(f,-10,10,2000000)
#print(integral)
