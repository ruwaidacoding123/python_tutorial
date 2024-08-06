'''
Python Functions is a block of related statements designed to perform a computational, logical, or evaluative task. The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again. 

Functions can be both built-in or user-defined. It helps the program to be concise, non-repetitive, and organized.

Syntax: 

def function_name(parameters):
	"""docstring"""
	statement(s)
	return expression

Creating a Function
We can create a Python function using the def keyword.

Calling a Function
After creating a function we can call it by using the name of the function followed by parenthesis containing parameters of that particular function.

'''
#Example: Python Creating Function


# A simple Python function
def fun():
	print("Welcome to python journey")

# Driver code to call a function
fun()


print('passing Argument')
'''
Arguments of a Function
Arguments are the values passed inside the parenthesis of the function. A function can have any number of arguments separated by a comma.

Example: Python Function with arguments
In this example, we will create a simple function to check whether the number passed as an argument to the function is even or odd.
'''
# A simple Python function to check
# whether x is even or odd
def evenOdd(x):
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")


# Driver code to call the function
evenOdd(2)
evenOdd(3)

print('---------Arguigemen---------')

'''
Types of Arguments
Python supports various types of arguments that can be passed at the time of the function call. Let’s discuss each type in detail.

Default arguments
A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument. The following example illustrates Default arguments. 
'''

# Python program to demonstrate
# default arguments
def myFun(x, y=50):
	print("x: ", x)
	print("y: ", y)

# Driver code (We call myFun() with only
# argument)
myFun(10)

