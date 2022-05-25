# Operators and assignments
# ternary and binary 
# +, -, *, /, //, %, etc., ++, --

# Assignments
# =, +=, -=, /=, *=, //=

num = 3
num = num + 1
num += 1 


# 3 things to consider in loops
# inital value
# final value
# increment

for num in range(20, 1, -2):
    print(num)

# While repeats as long as the condition is true
# syntax - 

# intial value
# while(condition):
#   ...
#   increment

number = 100
while number > 0:
    print(number)
    number //= 2


command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)