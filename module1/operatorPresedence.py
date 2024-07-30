# Examples of Operator Precedence

# Precedence of '+' & '*'
expr = 10 + 20 * 30
print(expr)

# Precedence of 'or' & 'and'
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")



print("------------ == and is -------")
#The Equality operator (==) is a comparison operator 
# in Python that compare values of both the operands and checks for value equality. 
# Whereas the 'is' operator is the  identity operator that checks whether both the operands refer to the same object or not (present in the same memory location).
# python3 code to 
# illustrate the 
# difference between
# == and is operator
# [] is an empty list
list1 = []
list2 = []
list3=list1

if (list1 == list2):
    print("True")
else:
    print("False")

if (list1 is list2):
    print("True")
else:
    print("False")

if (list1 is list3):
    print("True")
else:    
    print("False")

list3 = list3 + list2

if (list1 is list3):
    print("True")
else:    
    print("False")
