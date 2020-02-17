import math
#automatic diferentiation
class ad:
  """ Classe para automatic diferentiation"""
  @staticmethod
  def cos(d):
    return D(math.cos(d.x),-math.sin(d.y))
  @staticmethod
  def sin(d):
    return D(math.sin(d.x),math.cos(d.y))
  @staticmethod
  def exp(d):
    return D(math.exp(d.x),math.exp(d.x)*d.y)

class D:
  def __init__(self,x,y=1):
    """passe como parâmetro x e y"""
    self.x = x
    self.y = y
  def __add__(self,d):
    if type(d) == D:
      return D(self.x + d.x,self.y + d.y)
    else:
      return D(self.x + d,self.y)
  def __radd__(self,d):
    return D(self.x,self.y) + d
  def __sub__(self,d):
    return self + (-d)
  def __rsub__(self,d):
    return D(d - self.x,self.y)
  def __neg__(self):
    return D(-self.x,-self.y)
  def __repr__(self):
    return "(%f , %f)"%(self.x,self.y)
  def __mul__(self,d):
    if type(d) == D:
      return D(self.x * d.x,self.y*d.x + self.x*d.y)
    else:
      return D(self.x*d,d*self.y)
  def __rmul__(self,d):
    return D(self.x,self.y)*d
  def __truediv__(self,d):
    return D(self.x/d.x,(self.y*d.x - self.xd.y)/(d.x**2))
  def __pow__(self,n):
    return D(self.x**n,n*self.x**(n-1))
#metódo de newton em uma dimensão
def _g(i,j):
    return 1 if i == j else 0
def serialize(f,*args):
    values = []
    enum = enumerate(args)
    for i,arg in enum:
        g = f(*tuple([D(x,_g(i,j)) for j,x in enumerate(args)]))
        if i == 0: values.append(g.x)
        values.append(g.y)
    return tuple(values)
def change(xi,index,x):
    xi = list(xi)
    xi[index] = x
    return tuple(xi)
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
        if i == 500: break
    return x
def minimize(xs,ys,err=0):
    lost = lambda x,y,a,b : (a*x + b  - y)**2

    Error = lambda a,b : sum([lost(x,ys[i],a,b) for i,x in enumerate(xs)])
    a,b = 0,0
    #_err = Error(a,b)
    print("Minimizing")
    i = 1
    while i < 10:
        a = newtonMethod(Error,(a,b),index=0,err=err)
        b = newtonMethod(Error,(a,b),index=1,err=err)
        i = i + 1
    return(a,b)
 