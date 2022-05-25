# Ternary operators
# binary operators +, -, / *, etc 2 + 2 + 4

age = 24
if(age > 18):
    print("Adult")
else:
    print("child")

# OR
age = 12
if(age > 18):
    message = "Adult"
else:
    message = "Child"
print(message)

# OR
message = "Adult" if age > 18 else "Child"
print(message)

# message = (age > 18) ? "Adult" : "Child"


# and or not nor xor