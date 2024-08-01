names = ['Ruweida', 'Muzamil']
print(names)

#index
print(names[1])
print(names[-1])
#indicates columns
print(names[1:]) #[2:4]


print("--------large number-----------")
numbers =[3, 4, 24, 6, 7]
max = numbers[0]

for number in numbers:
 if number > max:
  max = number
print(max)