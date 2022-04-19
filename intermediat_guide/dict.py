#DICTIONARY

#init1
mydict = { "name": "Johannes", "age": 26, "city": "Lohne"}
print(mydict)

#init2
mydict2 = dict(name="Anton", age=21, city="Lohne")
print(mydict2)

#access value
print(mydict["age"])
print(mydict2["age"])

#change value
mydict["age"]=27
print(mydict["age"])

#del value
del mydict["name"]
print(mydict)

#del value 2
mydict.pop("age")
print(mydict)

#del LAST value
mydict2.popitem()
print(mydict2)

mydict3 = { "name": "Johannes", "age": 26, "city": "Lohne"}

if "name" in mydict3:
    print(mydict3["name"])

try:
    print(mydict3["not_name"])
except:
    print("Error")

#loop through keys
for key in mydict3:
    print(key)

#loop through values
for value in mydict3.values():
    print(value)

#copy dict - deep copy
dict_copy = dict(mydict3)

#copy dict - shallow copy
dict_copy2 = mydict3






