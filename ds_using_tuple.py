zoo=("python", "elephant", "penguin")
print("Number of animals in the zoo is {}".format(len(zoo)))

new_zoo=("monkey", "camel", zoo)
print("Number of cages in the new zoo is {}".format(len(new_zoo)))
print("All animals in new zoo are {}".format(new_zoo))
print("Animals brought from old zoo is {}".format(new_zoo[2]))
print("Last animals brought from old zoo is {}".format(new_zoo[2][2]))
print("Number of animals in the new zoo is {}".format(len(new_zoo)\
                                                      -1 + len(new_zoo[2])))