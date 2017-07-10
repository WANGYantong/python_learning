def func(a, b=5, c=10):
    print("a is {} and b is {} and c is {}".format(a, b, c))

func(3, 7)
func(25, c=24)
func(c=25, a=100)
