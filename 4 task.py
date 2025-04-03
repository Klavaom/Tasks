import csv, random

name_file = "board_id.csv"

def new_file(name):
    count = 1
    with open(name, "w", newline='') as file:
        writen = csv.writer(file)
        writen.writerow(["Board_id","Length"]) 
        for i in range(1000):
            writen.writerow([count, random.randrange(1, 6000)]) 
            count += 1

    
def content_file(name):
    length = []
    with open(name, "r",) as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            length.append(int(row["Length"]))
            length.sort()
        return length
    
    
def max_find(length):
    return length[-1]
    

def avg_length(length):
    id = 0 
    summary = 0 
    for i in range(999):
        summary += length[id]
        id += 1
        average_length = summary / 1000 
    return average_length
    

def low_find(length):
    return length[0]


def main():
    new_file(name)
    length = content_file(name)
    max_lenght = max_find(length)
    average_length = avg_length(length)
    low_lenght = low_find(length)
    print(f"Наибольшее {max_lenght}, среднее {average_length}, наименьшее {low_lenght}")

if __name__ == '__main__':
    name = "board_id.csv"
    main()