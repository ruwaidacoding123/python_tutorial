from pathlib import Path

# Path = Path("email")
# print(Path.mkdir())

# Path = Path("env")
# print(Path.mkdir())

path = Path()
# print(path.glob('*.xls'))
for file in path.glob('*.py'):
    print(file)


path = Path()
# print(path.glob('*.xls'))
for file in path.glob('*'):
    print(file)