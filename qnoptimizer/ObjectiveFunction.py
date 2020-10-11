import numpy as np

# This file contains the definition for the ObjectiveFunction class. 
# 

def ValidDim(n):
    assert n > 0, 'Not greater than 0.'
    assert isinstance(n,int), 'Not an integer.'

    return True

class ObjectiveFunction:
    # This seems like a small enough step size.
    _step_size = 10**-3

    def __init__(self,f,n,m):
        self.SetFunction(f)
        self.SetInputDim(n)
        self.SetOutputDim(m)

    def SetFunction(self,f):
        # Include error handling here.
        self.__Function = f
    
    def SetInputDim(self,n):
        if ValidDim(n):
            self.__input_dim = n

    def SetOutputDim(self,m):
        if ValidDim(m):
            self.__output_dim = m

    def SetStepSize(self,h):
        if h > 0:
            self._step_size = h
        else:
            print('Step size must be a positive number.')

    def partial_derivative(self, x, var_i):
        # Yes, this is inefficient but it makes it clear what is happening.
        x_plus = x.copy()
        x_minus = x.copy()

        # include an out of bounds exception here.
        if self.__input_dim == 1:
            x_plus += self._step_size
            x_minus -= self._step_size
        else:
            x_plus[var_i]  += self._step_size
            x_minus[var_i] -= self._step_size

        numer = self.__Function(x_plus) - self.__Function(x_minus)
        
        denom = 2*self._step_size
        return(numer/denom)
    
    def Evaluate(self,x):
        return self.__Function(x)

    def Gradient(self,x):
        return np.array([self.partial_derivative(x,i)\
             for i in range(self.__input_dim)])

    def Hessian(self,x):
        # Computes a first order central difference approximation 
        # of the Hessian.        
        g = lambda x,i : self.partial_derivative(x,i)
        eye = np.identity(self.__input_dim)
        h = self._step_size
        
        half_hess = lambda i,j : (g(x + h*eye[j],i)-g(x - h*eye[j],i))

        # Check out this sick list comprehension.
        H = [
                [ (half_hess(i,j) + half_hess(j,i))/(4*h)\
                     for i in range (self.__input_dim)] 
                for j in range(self.__input_dim)
            ]

        # Make it a numpy array because WE ARE GOING FAST.
        return np.array(H)