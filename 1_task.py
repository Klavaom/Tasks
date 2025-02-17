
def Endswith(string, ending):
    ending = list(ending)
    string = list(string)
    len_ending = len(ending)
    len_string = len(string)
    b = 0
   
    for i in range(len_ending):
        if string[len_string-1] == ending[len_ending-1]:
            None
        else:
            b += 1
        len_ending -= 1
        len_string -= 1

    return b == 0


def Vowels(string): 
    vowels_letter = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y'}
    len_string = len(string)
    for i in range(len_string):
        if string[len_string-1] in vowels_letter:
            string.pop(len_string-1)
        else:
            None
        len_string -= 1 
     
    return (''.join(string))


def Arithmetic_mean(nums):
    nums = list(nums)
    count_num = len(nums)
    divider = len(nums)
    sum_num = 0

    for i in range(count_num):
        sum_num += nums[count_num - 1]
        count_num -= 1
    return sum_num/divider


def Individuality(non_sort):
    return list(set(non_sort))


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
    



assert Endswith('abc', 'bc') == True
assert Endswith('abc', 'cd') == False
assert Endswith('asd', 'sd') == True

assert Vowels("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"
assert Vowels("You can never be overdressed or overeducated") == " cn nvr b vrdrssd r vrdctd" 
assert Vowels("The best dreams happen when you're awake") == "Th bst drms hppn whn 'r wk"

assert Arithmetic_mean([1, 2, 3]) 
assert Arithmetic_mean([2, 2, 2]) 
assert Arithmetic_mean([4, 2, 3, 6]) 

assert Individuality([1, 1, 2, 3, 3, 4, "a"])  
assert Individuality([1, 1, 1, 2, 3, "a", 4, "a"])  
assert Individuality([1, 2, 2, 3, 5, "b", 4, "d"]) 

assert Intersections([1, 2, 3, 2, 0], [5, 1, 2, 7, 3, 2]) == [1, 2, 3] 
assert Intersections([1, 2, 3, 4, 2, 0], [5, 1, 2, 7, 4, 3, 2]) == [1, 2, 3, 4] 
assert Intersections([1, 7, 3, 2, 0, 6], [5, 1, 2, 7, 3, 2]) == [1, 2, 3, 7] 

assert Sort([0,1,0,1,1,0]) == [0,0,0,1,1,1] 
assert Sort([1,1,0,1,1,0]) == [0,0,1,1,1,1] 
assert Sort([0,1,0,1,1,0,0]) == [0,0,0,0,1,1,1] 