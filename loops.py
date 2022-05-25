# loops are programming constructs used when computing expressions that 
# repeats.

# while loop, for loop, do while.
# for loop
# print numbers from 1 to 50

# syntax - (for variable in iterable:
#               ....
#            )

from operator import truediv


for number in range(50):
    print(number)

print(type(range))

message = "looking back"
for char in message:
    print(char.upper())


for number in range(5):
    print((number + 1)* "*" )

    # Hello number 1 *
    # Hello number 2 **

# range(start, end, step)
# Addition of strings joins them together
# multiplication of string with integer duplicates
# the string to the number of the integer

print("who " * 3)


# for/else

age = int(input("Enter the age: "))

success = True if age > 18 else False
for num in range(4):
    print("Attempt")
    if(success):
        print("successful")
        break
else:
    print("Attempted four times and failed")


# Nested loop
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# (0,0)
# (0,1)
# (0,2)
# (1,0)
