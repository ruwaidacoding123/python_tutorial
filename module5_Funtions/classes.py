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