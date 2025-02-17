def Intersections (first_list, second_list):
    intersections = []
    for element in first_list:
        if element in second_list:
            intersections.append(element)
    intersections = list(set(intersections))
    return(intersections)
    

def Sort (non_sort):
    non_sort = list(non_sort)
    non_sort.sort()
    return(non_sort)


assert Intersections([1, 2, 3, 2, 0], [5, 1, 2, 7, 3, 2]) == [1, 2, 3] 
assert Intersections([1, 2, 3, 4, 2, 0], [5, 1, 2, 7, 4, 3, 2]) == [1, 2, 3, 4] 
assert Intersections([1, 7, 3, 2, 0, 6], [5, 1, 2, 7, 3, 2]) == [1, 2, 3, 7] 

assert Sort([0,1,0,1,1,0]) == [0,0,0,1,1,1] 
assert Sort([1,1,0,1,1,0]) == [0,0,1,1,1,1] 
assert Sort([0,1,0,1,1,0,0]) == [0,0,0,0,1,1,1] 