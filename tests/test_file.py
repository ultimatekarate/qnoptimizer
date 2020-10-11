from context import of

def test_Hessian(x_0):
    f = lambda x : 2*(x[0]**2) + 2*x[1]**3
    F = of.ObjectiveFunction(f,2,1)

    return F.Hessian(x_0)



print(test_Hessian([0,1]))