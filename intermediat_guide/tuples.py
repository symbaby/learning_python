# TUPLE IS IMMUTABLE
import sys
import timeit

test = ("test1", 2, "ers3")
print(test)

item = test[2]
print(item)

item1 = test[-1]
print(item1)

# test[0] ="kein test"

for i in test:
    print(i)

if "test1" in test:
    print("Johannes is bad in python")
else:
    print("Johannes is good in python")

test1 = ("a","b","c","d")

print(len(test1))

print(test1.count("a"))

test2 = list(test1)
print(test1)#tuple
print(test2)#list

test4 = (1,2,3,4,5,6,7,8,9)
a = test4[0:8:2]
print(a)

test5 = "lohne", 2, "sylter str"
stadt, zahl, strasse = test5;#<------!!!!!!! REWATCH
print(stadt)
print(zahl)
print(strasse)


test6 = 1, 2, 3, 4, 5, 6
zahl1, *zahlen, zahl6 = test6;#<------!!!!!!! REWATCH
print(zahl1)
print(zahlen)
print(zahl6)

my_list = [1,2,3,"hello", True]
my_tuple = (1,2,3,"hello",True)

#TUPLES ARE EFFICIENT!! <----------!!!!!!! REWATCH
#import sys
#LISTS NEED MORE MEMORY THEN TUPLES
print(sys.getsizeof(my_list))#120 byte
print(sys.getsizeof(my_tuple))#80byte

#import timeit
#LISTS ARE SLOWER THEN TUPLES
print(timeit.timeit(stmt="[1,2,3,4,5,6]", number=100000))
print(timeit.timeit(stmt="(1,2,3,4,5,6)", number=100000))
















