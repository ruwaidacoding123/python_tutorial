student = {
    "name" : "Abdi Ali",
    "Age" : 15,
    "Phone" : 123456,
    "is_varified" : True

}

print(student["name"])

#get value
print(student.get("birthDate"))
print(student.get("birthDate", "jan 1 2009"))


print("----------challenge------------")
number = (input("Phone: "))

digit_mapping = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}

output = ""

for ch in digit_mapping:
    output += digit_mapping.get(ch, "!") + " "
print(output)
