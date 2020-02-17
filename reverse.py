import math

class Var:
    ASCENDENTE = 1
    DESCENDENTE = 2
    """
    use x = Var(number)
    there is method overloading where you can add,sub ect
    like :
        x = Var(1)
        y = Var(2)
        z = x + y
        print(z.value)
        #output
        3
        # wich is 1 + 2, just that
    """
    def __init__(self,value):
        self.value = value
        self.children = []
        self.grad_value = None
    def __mul__(self,other):
        if type(other) == Var:
            z = Var(self.value * other.value)
            self.children.append((other.value,z))
            other.children.append((self.value,z))
            return z
        else:
            z = Var(self.value * other)
            self.children.append((other,z))
            return z
    def __rmul__(self,other):
        return self * other
    def __add__(self,other):
        if type(other) == Var:
            z = Var(self.value + other.value)
            self.children.append((1,z))
            other.children.append((1,z))
            return z
        else:
            z = Var(self.value + other)
            self.children.append((1,z))
            return z
    def __radd__(self,other):
        return self + other
    def __pow__(self,other):
        if type(other) == Var:
            z = Var(self.value**other.value)
            self.children.append((other.value*self.value**(other.value-1),z))
            other.children.append((z.value*math.log(abs(self.value)),z))
            return z
        else:
            z = Var(self.value**other)
            self.children.append((other*self.value**(other-1),z))
            return z
    def __sub__(self,other):
        if type(other) == Var:
            z = Var(self.value - other.value)
            self.children.append((1,z))
            other.children.append((-1,z))
            return z
        else:
            z = Var(self.value - other)
            self.children.append((1,z))
            return z
    def __rsub__(self,other):
        return self - other
    def __truediv__(self,other):
        if type(other) == Var:
            z = Var(self.value / other.value)
            self.children.append((1.0/other.value,z))
            other.children.append((-self.value/(other.value**2),z))
            return z
        else:
            z = Var(self.value / other)
            self.children.append((1.0/other,z))
            return z
    def __rtruediv__(self,other):
        z = Var(other/self.value)
        self.children.append((-other/(self.value**2),z))
        return z
    def grad(self):
        if self.grad_value is None:
            self.grad_value = sum(weight*var.grad() for weight,var in self.children)
        return self.grad_value
def serialize(f,*args):
    vars = []
    for arg in args:
        vars.append(Var(arg))
    z = f(*tuple(vars))
    z.grad_value = 1.0
    values = [z.value]
    for i in range(len(args)):
        values.append(vars[i].grad())
    return tuple(values)
def change(xi,index,x):
    xi = list(xi)
    xi[index] = x
    return tuple(xi)
def ln(var):
    z = Var(math.log(var.value))
    var.children.append((1.0/var.value,z))
    return z
def newtonMethod(f,xi,index=0,err=0,verbose=False):
    """
        xi é uma tuplay que será o agumnto da função f(*xi)
        index => posição de qual variavel está sendo buscada
    """
    t = serialize(f,*xi)
    y = t[0]
    dy = t[index+1]
    i = 1
    x = xi[index]
    
    while abs(y) > err:
        if verbose : print("iteration = ",i,"=>","x=",x)
        x = x - y/dy
        xi = change(xi,index,x)
        t = serialize(f,*xi)
        y = t[0]
        dy = t[index+1]
        i = i + 1
        print(y)
        if i == 100:
            print("break at ",i)
            break
    return x
Error_delta = lambda xs,ys,a,b: sum([lost(x,ys[i],a,b) for i,x in enumerate(xs)])

def minimize(xs,ys,lr=0.1,iter=100,const=None):
    loss = lambda x,y,a,b: (a*x + b - y)**2
    Error = lambda a,b: sum([loss(x,ys[i],a,b) for i,x in enumerate(xs)])
    xi = (1,0)
    #_err = Error_delta(xs,ys,a,b)
    print("Regreção Linear...")
    g = gradient(Error,xi,lr=lr,iter=iter)
    return g
def polinomial(xs,ys,lr=0.1,iter=100,const=None):
    loss = lambda x,y,a,b,c: (a*x*x + b*x + c - y)**2
    Error = lambda a,b,c: sum([loss(x,ys[i],a,b,c) for i,x in enumerate(xs)])
    xi = (1,0,0)
    #_err = Error_delta(xs,ys,a,b)
    print("Regresão Polinomial...")
    g = gradient(Error,xi,lr=lr,iter=iter)
    return g

def gradient(f,xs,lr=0.01,iter=100,type=Var.DESCENDENTE):
    t,*rest = serialize(f,*xs)
    v = list(xs)
    for i in range(iter):
        if type == Var.DESCENDENTE:
            v = [v[j] - lr*dx for j,dx in enumerate(rest)]
        elif type == Var.ASCENDENTE:
            v = [v[j] + lr*dx for j,dx in enumerate(rest)]
        else:
            print("erro: type ("+type +") not valid")
            return
        t,*res = serialize(f,*v)
        rest = res
    return tuple(v)
from functools import reduce # caso utilizes python 3
import operator

def vero(f,xs,mi,b,sigma,lr,iter):
    VL = lambda mi,sigma : [f(x,mi,sigma) for x in xs]
    PVL = lambda mi,sigma: ln(reduce(operator.mul,VL(mi,sigma)))
    da,db = gradient(PVL,xs=(mi,sigma),lr=lr,iter=iter,type="ascendente")
    return (da,db)