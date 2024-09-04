import numpy as np
import timeit

#1)	Define the following metrics and perform the following operations
#    i)	Write a Python program using Python Lists
def func1():
    matrix_a = [[3.7827,3.3454,3.2341],[2.2122,3.5678,3.9087],[1.1234,2.8934,5.9087]]
    matrix_b = [[3.1234,3.0987,3.1234],[2.1111,3.2222,3.3333],[1.0987,1.3456,5.1234]]
    matrix_c = [[3.1243,3.0989,3.1256],[2.6721,3.6785,3.9017],[1.1254,2.8956,5.9187]]

print("1. i")
print(timeit.timeit(func1, number=1000))

#    ii)	Write a Python program and NumPy
def func2():
    np_matrix_a = np.matrix([[3.7827,3.3454,3.2341],[2.2122,3.5678,3.9087],[1.1234,2.8934,5.9087]])
    np_matrix_b = np.matrix([[3.1234,3.0987,3.1234],[2.1111,3.2222,3.3333],[1.0987,1.3456,5.1234]])
    np_matrix_c = np.matrix([[3.1243,3.0989,3.1256],[2.6721,3.6785,3.9017],[1.1254,2.8956,5.9187]])
print("1. ii")
print(timeit.timeit(func2, number=1000))

# 2)	Write a Python Program and perform the following operations ?

# I.	Create a List {1225, 4986, 6789, 7890, 2345, 6783, 0987, 1234, 8765, 3456}
print("2. I")
def funci():
    list1 = (1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456)

print(timeit.timeit(funci, number=1000))

# II.	Iterate using a for loop
print("2. II")
def funcii():
    list1 = (1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456)

    for i in list1:
        return i

print(timeit.timeit(funcii, number=1000))

# III.	Iterate using for loop and range
print("2. III")
def funciii():
    list1 = (1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456)

    for i in range(0,9):
        return i

print(timeit.timeit(funciii, number=1000))

# IV.	List Comprehension
print("2. IV")
def funciv():
    list1 = (1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456)
    return [i for i in list1]

print(timeit.timeit(funciv, number=1000))

# V.	Enumerate
print("2. V")
def funcv():
    list1 = (1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456)
    enum1 = enumerate(list1)
    for i in enum1:
        return i

print(timeit.timeit(funcv, number=1000))

# VI.	Iter function and next function
print("2. VI")
def funcvi():
    list1 = (1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456)
    iter1 = iter(list1)
    for i in range(0,9):
        return(next(iter1))

print(timeit.timeit(funcvi, number=1000))

# VII.	Map function
print("2. VII")
def funcvii():
    list1 = (1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456)
    def print_test(x):
        return x

    map_test = map(print_test, list1)
    return(list(map_test))

print(timeit.timeit(funcvii, number=1000))

# VIII.	Using zip
print("2. VIII")
def funcviii():
    list1 = (1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456)
    zipped = zip(list1,[0,1,2,3,4,5,6,7,8,9])

    return(set(zipped))

print(timeit.timeit(funcviii, number=1000))

# IX.	Using NumPy Module
print("2. IX")
def funcix():
    arr = np.array([1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456])
    return(arr)

print(timeit.timeit(funcix, number=1000))

test_list = ["a","b", "c", "d", "e"]

def allperms(my_list):
    
    if not (my_list):
        return []
    
    if len(my_list) ==1:
        return[my_list]
    
    total = []
    for i in range(len(my_list)):
        temp = my_list[i]
        leftover = my_list[:i] + my_list[i+1:]

        for each in allperms(leftover):
            total.append([temp]+each)
    return total
print("3. Permutations")
print(timeit.timeit(lambda: allperms(test_list), number=1000))

def allcomb(my_list):
    total = [[]]
    for i in my_list:
        for j in total.copy():
            comb = j + [i]
            if comb != []:
                total.append(comb)
    total.pop(0)
    return total
print("3. Combinations")
print(timeit.timeit(lambda: allcomb(test_list), number=1000))

import itertools

def iter_perms(my_list):
    perm = list(itertools.permutations(test_list))
    return perm

print("4. Permutations")
print(timeit.timeit(lambda: iter_perms(test_list), number=1000))

def iter_comb(my_list, r):
    total = []
    for each in range(1,r+1):
        combo = list(itertools.combinations(test_list, each))
        total.append(combo)
    return total

print("4. Combinations")
print(timeit.timeit(lambda: iter_comb(test_list, 5), number=1000))