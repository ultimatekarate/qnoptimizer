class qnoptimizer:
    # This will be the main class of the package.

    model_hessian = None
    
    # These things are needed to determine when to stop the iterative 
    # procedure.
    iteration_information = {
        'function_value':[],
        'gradient_norm':[],
        'step_sizes':[]
    }

    def __init__(self):
        pass

    def StoppingCriteria(self):
        # Is the norm of the gradient small enough?
        # Has the step size been sufficiently small?
        # Have we hit the maximum number of iterations? 
        pass

    def Optimize(self):
        # The workhorse function.
        # At each iteration it will try to 
        # 1) Take the Newton step 
        # 2) If Newton step does not meet Armijo condition, 
        # try backtracking line search.
        # 3) If that fails, solve the trust region subproblem.
        pass

    def BFGSUpdate(self):
        # I'm putting this function here for now. 
        pass