for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

print("------------challenge---------------")

print(" frist way")
numbers = [5, 2, 5, 2, 3]

for x_count in numbers:
    print('x' * x_count)

print(" second way ")
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
        print(output)
