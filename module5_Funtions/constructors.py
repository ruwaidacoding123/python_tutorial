class Person:
    def __init__(self, name):
        self.name = name


    def talk(self):
        print("talk")

james = Person("James Smith")
print(james.name)
james.talk()