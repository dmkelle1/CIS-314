import random

tuple = ("A","B","C","D","E","F","G","H","I","J")
list = ["J","I","H","G","F","E","D","C","B","A"]

print(tuple)
print(list)

print(tuple[2])
print(list[2])

print(random.sample(tuple, len(tuple)))
print(random.sample(list, len(list)))

tupleMore = tuple + ("K",)
listMore = list + ["Z",]

print(tupleMore)
print(listMore)

#removing an element in a touple alone is not possible
#there are ways to get around this by adding the touple to a list
#but if its a tuple alone then its not possible

listMore.remove(listMore[0])
print(listMore)