from os import path


def new_file(number):
    number = int(number)*2
    with open(f"{number}.txt", "w") as file:
        file.write(f'{number}')
    with open(f"{number}.txt", "r") as file:
        open_file = file.read()
    return(open_file)


assert new_file(232) == "464"
assert new_file(70) == "140"
assert new_file(2) == "4"

print(path.exists("464.txt"))
print(path.exists("140.txt"))
print(path.exists("4.txt"))





