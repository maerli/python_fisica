from reverse import serialize,minimize,Var,gradient,vero,ln,polinomial
import math
import matplotlib.pyplot as plt
import numpy as np
from random import random

f = lambda t : (9.8 * t*t +  random()/100)/2
xs = [x/20.0 for x in range(20)]
ys = [f(x) for x in xs]

a,b,c= polinomial(xs,ys,lr = 0.01,iter=4000)

print("{} {} {}".format(a*2,b,c))
"""
import inspect
print(inspect.getsourcelines(f)[0][0])
"""
#print(Var.__doc__)

"""
g = lambda x: x*x - 6*x + 16
x = (7,)
a = gradient(g,x,lr=0.01,iter=5000,type=Var.DESCENDENTE)
print(a)
"""
"""
f = lambda t: 4 + t - g \frac{gt^2}{2}
xf = newtonMethod(f,xs=(1,),index=0,err=0.01)
print(xf)
"""
"""
f = lambda x,a,b : 1.0/(1 + Var(math.e)**(-1*x*(a-b)))
s = (1,3)
a,b = vero(f,xs,1,2,0.01,1000)
ys = [f(x,a,b).value for x in xs]
plt.plot(xs,ys)
plt.show()
print(a,b)"""