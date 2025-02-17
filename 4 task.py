import csv, random

name = "board_id.csv"
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
            length.append(int(row[" Length"]))
        length.sort()

def max():
    max=length[999]
    with open(name, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row[" Length"] == str(max):
                id = row["Board_id"]
                
    print(id, max) 
    return(id, max)

def low():
    low=length[0]
    with open(name, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row[" Length"] == str(low):
                id = row["Board_id"]
    print(id, low)
    return(id, low)

def midlle():
    summ = 0
    index = 0
    for i in length:
        summ += length[index]
        index += 1
    midlle = summ / 1000
    print(midlle)
    return(midlle)
new_file(name)
read(name)






assert max() 
assert low() 
assert midlle() 

