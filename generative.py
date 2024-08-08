import random

for i in range(3):
    print(random.randint(30,80))


members = ['james', 'mary', 'bob']
leader = random.choice(members)
print(leader)


print('--------challenge-----')

class Dice:
    def roll(self):
        first = random.randint(1,5)
        second =random.randint(2,2)
        return first, second
    

dice = Dice()
print(dice.roll())