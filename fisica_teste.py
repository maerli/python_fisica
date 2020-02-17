#fisica_teste
from fisica import trajetoria,radiansToDegree
from math import sqrt,asin,tan,cos
from reverse import serialize
h = 5.1
g = 9.8
v = 20
theta = asin(sqrt(2*g*h)/v)
print("theta = {:.3}".format(radiansToDegree(theta)))
y = lambda x : tan(theta)*x - g *(x**2)/(2*(v**2)*cos(theta)**2)
def S(x):
	_,dy = serialize(y,x)
	return sqrt(1 + dy**2)
comprimento = trajetoria(S,0,17,100000)
print("{:.3}".format(comprimento))