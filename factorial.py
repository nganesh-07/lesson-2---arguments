def factorial(x):
    '''Repetitive function used to find the factorial of an integer.'''
    if x == 1 or x == 0:
        return 1
    else:
        return x*factorial(x-1)


print(factorial.__doc__)
print("Factorial of 0:", factorial(0))
print("Factorial of 1:", factorial(1))
print("Factorial of 5:", factorial(5))
print("Factorial of 10:", factorial(10))