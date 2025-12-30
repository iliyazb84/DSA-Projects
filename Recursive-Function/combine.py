
# Project no 01-2 --> Composite Function!

# TODO: Create a Combination Function Using Only Recursive Functions.

def combine(num1, num2):
    if num2 == 0 or num2 == num1:
        return 1
        
    else:
        return combine(num1 - 1, num2 - 1) + combine(num1 - 1, num2)
        

print(combine(4,3))
