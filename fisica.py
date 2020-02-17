from math import sqrt,asin,tan,cos,pi
from montecarlo import monte_carlo
from reverse import serialize
angulo_raso = 180
def Torricelli(v0=None,vf=None,a=None,h=None):
    if vf == None : 
        return sqrt(v0**2 + 2*a*h)
    elif v0 == None:
        return sqrt(2*a*h - vf**2)
    elif a == None:
        return (vf**2 - v0**2)/(2*h)
    elif h == None:
        return (vf**2 - v0**2)/(2*a)
def radiansToDegree(radians):
    return radians*(angulo_raso/pi)
def degreeToRadians(angle):
    return pi*(angulo_raso/angle)
def equacaoHorariaVertical(x,a,b,c):
    return a*x**2 + b*x + c
    
def trajetoria(f,a,b,N):
    return monte_carlo(f,a,b,N)
#calculando trajetoria
