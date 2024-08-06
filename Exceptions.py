#handling errors in python

#exit code 0 in terminal is says there is no error in the code
#exit code 1 in terminal is says there is  error in the code program crush  

'''try:
    age = input (int('Age: '))
    print(age)

except ValueError:
    print("invalid value")
   ''' 
try:
    age = int(input('Age: '))
    income = 5000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age can not be Zero")

except ValueError:
    print("invalid value") 
