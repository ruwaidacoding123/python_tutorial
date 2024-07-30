# Python code to demonstrate range() vs xrange()
# on  basis of return type

# initializing a with range()
a = range(1,10000)

# initializing a with xrange()
x = range(1,10000)

# testing the type of a
print ("The return type of range() is : ")
print (type(a))

# testing the type of x
print ("The return type of xrange() is : ")
print (type(x))


print("-------------------------")

# Python code to demonstrate range() vs xrange()
# on  basis of operations usage 

# initializing a with range()
a = range(1,6)

# initializing a with xrange()
x = range(1,6)

# testing usage of slice operation on range()
# prints without error
print ("The list after slicing using range is : ")
print (a[2:5])

# testing usage of slice operation on xrange()
# raises error
print ("The list after slicing using xrange is : ")
print (x[2:5])
