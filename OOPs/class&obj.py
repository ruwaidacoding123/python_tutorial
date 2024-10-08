'''
Class creates a user-defined data structure, 
which holds its own data members and member functions, 
which can be accessed and used by creating an instance of that class. 
A class is like a blueprint for an object.
'''
#Class Objects

'''
An Object is an instance of a Class. A class is like a blueprint while 
an instance is a copy of the class with actual values
'''

#An object consists of : 

'''
State: It is represented by the attributes of an object. It also reflects the properties of an object.
'''
'''
Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
'''
'''
Identity: It gives a unique name to an object and enables one object to interact with other objects.
'''

'''
A class is a user-defined blueprint or prototype from which objects are created. 
Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, 
allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state.
 Class instances can also have methods (defined by their class) for modifying their state.

'''



class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point()
point1.x = 10
print(point1.x)
point1.draw()



