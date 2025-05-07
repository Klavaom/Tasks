
def count(a):
    remake = {}
    for number in a:
        if number in remake:
            remake[number] += 1
        else:
            remake[number] = 1
    return(remake)



def main(a):
    counter = count(a)
    max_meaning = max(counter, key=counter.get)
    return(counter[max_meaning], max_meaning)



if __name__ == "__main__":
    a = [1, 1, 1, 3, 4, 5, 6, 4, 3, 2, 1, 3, 4, 1, 2, 3, 1, 2]
    main(a)



assert main([2, 2, 3, 1, 1, 2, 5,]) ==  (3, 2)
assert main([2, 3, 3, 1, 3, 2, 5,]) == (3, 3)
assert main([2, 2, 1, 1, 1, 2, 5,]) == (3, 2)






