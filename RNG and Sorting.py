import random
import secrets
from collections import Counter
import timeit

randomList1 = []
randomList2 = []
x = 0
for x in range(100):
    randomList1.append(random.randrange(1,17))

print(randomList1)

for x in range(100):
    randomList2.append(secrets.choice(range(1,17)))

print(randomList2)
# printed two 100 element lists with random numbers between 1-16. 
# The first one using random, and the second one using secrets

ranNumCount1 = Counter(randomList1)
print(ranNumCount1)
ranNumCount2 = Counter(randomList2)
print(ranNumCount2)
# I imported a counter module to count how many time a uniqe sumber appeared in the list
# Both rng methods seem to be very similar with unique numbers, secrets is just a little bit better but could just
# be up to chance

ranBigList1 = []
ranBigList2 = []

for x in range(100):
    ranBigList1.append(random.randrange(0,65535))

print(ranBigList1)

for x in range(100):
    ranBigList2.append(secrets.choice(range(0,65535)))

print(ranBigList2)

ranBigCount1 = Counter(ranBigList1)
print(ranBigCount1)
ranBigCount2 = Counter(ranBigList2)
print(ranBigCount1)
#since the range of numbers is so big, almost always every number in the list would be unique


sortList = []
for x in range(100):
    sortList.append(random.randrange(1, 17))
print(sortList)
sortListCopy1 = sortList.copy()
sortListCopy2 = sortList.copy()

def bubbleSort(arr):
    start = timeit.default_timer()
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    end = timeit.default_timer()
    time = end - start
    print("Bubble sort took %.9f seconds" % time)
    return arr
print(bubbleSort(sortListCopy1))
def pythonSort(arr):
    start = timeit.default_timer()
    arr.sort()
    end = timeit.default_timer()
    time = end - start
    print("Pythons built in sort took %.9f seconds" % time)
    return arr
print(pythonSort(sortListCopy2))
# the .sort() was much faster than using bubble sort

sortListBig = []
for x in range(100):
    sortListBig.append(random.randrange(0, 65535))
print(sortListBig)
sortListBigCopy1 = sortListBig.copy()
sortListBigCopy2 = sortListBig.copy()
print(bubbleSort(sortListBigCopy1))
print(pythonSort(sortListBigCopy2))

sortListBigMore = []
for x in range(500):
    sortListBigMore.append(random.randrange(0, 65535))
print(sortListBigMore)
sortListBigMoreCopy1 = sortListBigMore.copy()
sortListBigMoreCopy2 = sortListBigMore.copy()
print(bubbleSort(sortListBigMoreCopy1))
print(pythonSort(sortListBigMoreCopy2))

# in both cases, the .sort() method was much faster than bubble sort, as the number of elements increased,
# the sorting took longer in both methods but much more in bubble. When all thats increased is the size of
# whats in the elements, then the time doesnt change much.