class Person:
    def __init__(self, name):
        self.name = name


    def talk(self):
        print(f"hi, I am {self.name}")

james = Person("James Smith")
print(james.name)
james.talk()