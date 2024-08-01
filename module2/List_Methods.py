numbers = [4, 7, 6, 8, 9]
numbers.remove(9)
#if you want to remove all lists use
#numbers.clear()
print(numbers)

#some methods are
#.pop()
#.index(4)
#.count() is used to count how numbers are same in the list
#.sort() is used to arrange the lists
#.reverse() is verse verse of sort



print("---------remove duplicates-----------")
num = [2, 2, 4, 6, 6, 9]
unique = []
for list in num:
    if num not in unique:
        unique.append(num)
print(unique)

