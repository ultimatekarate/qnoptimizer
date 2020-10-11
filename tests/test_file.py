from context import of
from context import ls

import numpy as np

def test_Hessian(F,x_0):
    return F.Hessian(x_0)

def test_Gradient(F,x_0):
    return F.Gradient(x_0)

def test_NewtonStep(F,x_0):

    # Quick and dirty Newton step test.
    return -1*np.linalg.solve(F.Hessian(x_0),F.Gradient(x_0))

def test_NewtonMethod(F,x_0,iterations):
    nm = ls.LineSearch(F,x_0,iterations)
    nm.Optimize(x_0)

f = lambda x : 2*(x[0]**2) + 2*x[1]**2
F = of.ObjectiveFunction(f,2,1)

x = [1,1]
#print(test_Hessian(F,x))
#print(test_Gradient(F,x))
#print(test_NewtonStep(F,x))

guess = np.array([300, -12])
test_NewtonMethod(F,guess,10)