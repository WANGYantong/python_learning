def print_max(x,y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    #change arguments to integers if possible
    x = int(x)
    y = int(y)

    if x>y:
        print(x, "is maximum")
    elif x==y:
        print("both of them are equal")
    else:
        print(y, "is maximum")

print_max(3,4)
print(print_max.__doc__)
help(print_max)