'''# Python program to illustrate
# while loop
count = 0
while (count < 3):    
    count = count + 1
    print("Hello Geek")

print("------------------------")

# combining else with while
count = 0
while (count < 3):    
    count = count + 1
    print("Hello Geek")
else:
    print("In Else Block")

print("----------------------------")
# Single statement while block
count = 0
while (count == 0): print("Hello Geek")

print("-----------------------------")
# Single statement while block
count = 0
while (count == 0): print("Hello Geek")
'''

print("------------range-------------")


# Iterating over range 0 to n-1

n = 4
for i in range(0, n):
    print(i)

print("------------------------")

# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
     
# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
     
# Iterating over a String
print("\nString Iteration")    
s = "Geeks"
for i in s :
    print(i)
     
# Iterating over dictionary
print("\nDictionary Iteration")   
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s  %d" %(i, d[i]))
    
#Iterating over a set
print("\nSet Iteration")
set1 = {1,2,3,4,5,6}
for i in set1:
    print(i),

