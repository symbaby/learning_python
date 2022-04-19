# SET DOES NOT ALLOW DUPLICATES
# IS UNORDERED AND MUTABLE

myset = {1, 2, 3, 4, 5, 1}
print(myset)

myset1 = set("Hello")
print(myset1)

#init empty set like this
myset2 = set()
print(type(myset2))

#add elements to set
myset2.add(1)
myset2.add(2)
myset2.add(2)
print(myset2)

#delete the element
myset2.discard(2)
print(myset2)

#delete element and return it
print(myset2.pop())

#clear whole set
myset.clear()
print(myset)

#loop through
for i in myset1:
    print(i)

if "e" in myset1:
    print("e in myset1")
else:
    print("e not in myset1")

#union of 2 sets
numSet1 = {1, 2, 3, 4, 5}
numSet2 = {4, 5, 6, 7, 8}
unionSet = numSet1.union(numSet2)#need new set for union of 2 sets <----- REWATCH!!!!
print(unionSet)

#intersect of 2 sets
intersectSet = numSet1.intersection(numSet2)
print(intersectSet)

#returns difference of the first set      <------- REWATCH!!!!!
differenceSet = numSet1.difference(numSet2)
print(differenceSet)

differenceSet = numSet2.difference(numSet1)
print(differenceSet)

#symmetric difference Method returns difference of BOTH sets <------- REWATCH!!!!
symDifferenceSet = numSet1.symmetric_difference(numSet2)
print(symDifferenceSet)

#update the first set with the second set
#numSet1.update(numSet2)
#print(numSet1)

#first set gets updated with intersect values of set 1 and set 2
#numSet1.intersection_update(numSet2)
#print(numSet1)

#removes value from first set found in the second set
#numSet1.difference_update(numSet2)
#print(numSet1)

#updates the first set with the difference values of BOTH sides
numSet1.symmetric_difference_update(numSet2)
print(numSet1)

numSet3 = {4, 5}
numSet4 = {4, 5, 6, 7, 8}
numSet5 = {100}

#is set SUBSET of other set
print(numSet3.issubset(numSet4))

#is set SUPERSET of other set
print(numSet4.issuperset(numSet3))

#checks is sets are different in all values
print(numSet5.isdisjoint(numSet4))
print(numSet3.isdisjoint(numSet4))


numSet6 = {4, 5, 6, 7, 8}

#deep copy of set
numSet7 = set(numSet6)
print(numSet7)

# UNMUTABLE SET with frozenset() <------ REWATCH!!!!!
# we cant change the set
numSet8 = frozenset({1, 2, 3, 4})
print(numSet8)









