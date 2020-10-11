import numpy as np

class LineSearch:
    # Backtracking line search with quadratic AND cubic interpolation.

    # Greek letters for variable names because math reasons.
    # This particular alpha is used when checking one of the Armijo conditions.
    alpha = 10**-4
    
    # Stupid Python reserves lambda.
    lamduh = 1

    # Boolean flag because I'm writing this to work with other search methods.
    search_failed = False

    objective_function = None

    __x0 = None
    max_iterations = 10

    def __init__(self,F,initial_guess,max_iterations):
        self.__x0 = initial_guess
        self.objective_function = F
        self.max_iterations = max_iterations

    def NewtonStep(self,x_c):
        F = self.objective_function
        print(F.Hessian(x_c))
        return -1*np.linalg.solve(F.Hessian(x_c),F.Gradient(x_c))

    def Backtrack(self):
        pass

    def Optimize(self,initial_guess):
        assert self.objective_function is not None,\
            'Define an objective function.'
        assert isinstance(self.max_iterations,int)\
            and self.max_iterations > 0,\
            'Maximum number of iterations must be a positive integer.' 

        F = self.objective_function
        x_c = initial_guess
        i = 0

        while i < self.max_iterations:
            search_direction = self.NewtonStep(x_c)
            x_plus = x_c + search_direction
            f_plus = F.Evaluate(x_plus)
            print(f_plus)
            x_c = x_plus
            i += 1
        
    def SetObjectiveFunction(self,F):
        self.objective_function = F
