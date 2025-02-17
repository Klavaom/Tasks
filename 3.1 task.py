from os import path

def multiplication(number):
    number *= 2

    return(number)


def new_file(name):
    with open(f"{name}.txt", "w") as file:
        file.write(f'{name}')


def content_file():
    with open(f"{name}.txt", "r") as file:
        open_file = file.read()
    return(open_file)


numbers = [232, 70, 2]

for num in numbers:
    name = multiplication(num)
    new_file(name)
    content_file()


assert multiplication(232) == 464
assert multiplication(70) == 140
assert multiplication(2) == 4



print(path.exists("464.txt"))
print(path.exists("140.txt"))
print(path.exists("4.txt"))

