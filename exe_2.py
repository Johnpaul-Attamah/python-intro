# (Q2) Write a program to calculate the root of a Quadratic Equation. Go to the editor
#             Test Data : 1 5 7
#             Expected Output :
#             Root are imaginary;
#             No solution.


    # root1 = (-b + math.sqrt(math.pow(b,2) - 4 * a * c))/2 * a
    # root2 = (-b - math.sqrt(math.pow(b,2) - 4 * a * c))/2 * a
    

    # print("a quadratic equation is given as ax^2 + bx +c = 0")
    # print("Enter the values for a, b, and c to calculate the roots.")
    # get the value of a, b, c
    #     a = int(input("Enter the value of a"))
    #     convert to integers
    #     equal roots, imaginary roots and real roots
    #     if math.pow(b,2) < 4*a*c root is imaginary
    #     else root1 = ;
    #     root2 = ;
    #     print(root1, root2);
        

import math
from re import A


# print(math.pow(base,power))


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

if(math.pow(b,2) < 4 * a * c):
    print("Roots are Immagiinary")
else:
    root1 = (-(b) + math.sqrt(math.pow(b,2) - 4 * a * c))/ (2 * a)
    root2 = (-(b) - math.sqrt(math.pow(b,2) - 4 * a * c))/ (2 * a)
    print(root1, root2)


