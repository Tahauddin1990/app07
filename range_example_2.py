

for i in range(1,20):
    # {0:2} means 1st position from arguments and it takes 2 places
    # {1:4} means 2nd position from arguments and it takes 4 places
    # {2:4} means 3rd position from arguments and it takes 4 places
    print("Number is {0:2} and its Square is {1:4} and its Cube is {2:4}".format(i, i ** 2, i ** 3) )

for i in range(1,20):
    # {0:2} means 1st position from arguments and it takes 2 places
    # {1:<4} means 2nd position from arguments and it takes 4 places with Left Aligned
    # {2:<4} means 3rd position from arguments and it takes 4 places with Left Aligned
    print("Number is {0:2} and its Square is and is Left Aligned {1:<4} and its Cube is and is Left Aligned {2:<4}".format(i, i ** 2, i ** 3) )

for i in range(1,20):
    # {0:2} means 1st position from arguments and it takes 2 places
    # {1:>4} means 2nd position from arguments and it takes 4 places with Right Aligned
    # {2:>4} means 3rd position from arguments and it takes 4 places with Right Aligned
    print("Number is {0:2} and its Square is and is Right Aligned {1:>4} and its Cube is and is Right Aligned {2:>4}".format(i, i ** 2, i ** 3) )

