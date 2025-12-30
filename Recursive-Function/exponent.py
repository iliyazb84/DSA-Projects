

# Project no 01-1 --> Recursive Function!

# TODO: Create a Recursive Function that Raises the First Input to the Power of the Second.
def Exponent(base, exponent):
    if exponent > 0:

        # Code Trace: --> E.x(2,4): 2 * (2, 4) --> 2 * (2, 3) --> 2 * (2, 2) --> 2 * (2, 1) --> 2 * 1
        #                     16          8               4             2               1         1

        return base * Exponent(base, exponent - 1)
    else:
        return 1
    
print(f"Result: {Exponent(2, 8)}")
