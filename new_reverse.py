import math

class Var:
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
    def __repr__(self):
        return "Var(%s)"%(self.value)
x = Var(2)
y = x**x + 1
y.grad_value = 1.0
print(y)
print("Derivada = %s "%(x.grad()))
