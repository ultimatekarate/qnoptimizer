class LineSearch:
    # Backtracking line search with quadratic AND cubic interpolation.


    # Greek letters for variable names because math reasons.
    # This particular alpha is used when checking one of the Armijo conditions.
    alpha = 10**-4
    
    # Stupid Python reserves lambda.
    lamduh = 1

    # Boolean flag because I'm writing this to work with other search methods.
    search_failed = False

    max_iterations = 10

    def __init__(self):
        pass

    def NewtonStep(self):
        pass

    def Backtrack(self):
        pass

