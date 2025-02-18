import csv, random

name = "board_id.csv"
length_sort = []
length = []

def randomaise(first, end):
    num = random.randrange(first, end)
    return(num)

def new_file(name):
    count = 0
    with open(name, "w", newline='') as csvfile:
        writen = csv.writer(csvfile)
        writen.writerow(["Board_id"," Length"]) 
        for i in range(1000):
            num = randomaise(1, 6000)
            writen.writerow([count, num]) 
            count += 1

def read(name):
    with open(name, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            length_sort.append(int(row[" Length"]))
            length.append(int(row[" Length"]))
        length_sort.sort()

def max():
    max=length_sort[999]
    index = 0
    for i in range(999):      
        index += 1
        if length[index] == max:
            id = index
    print(id, max) 
    return(id, max)

def low():
    low=length_sort[0]
    index = 0
    for i in range(999):
        index += 1
        if length[index] == low:
            id = index

    print(id, low)
    return(id, low)

def midlle():
    summ = 0
    index = 0
    for i in length_sort:
        summ += length_sort[index]
        index += 1
    midlle = summ / 1000
    print(midlle)
    return(midlle)

new_file(name)
read(name)



assert max() 
assert low() 
assert midlle() 

