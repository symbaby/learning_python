#LIST IS MUTABLE

# DEFINING A SIMPLE FUNCTION
def runMyList():

    # INITIALIZE LISTS
    mylist = ["banana", "apple", "cherry"]
    print(mylist)

    # DIFFERENT DATATYPES
    mylist2 = [1,2,3,"test"]
    print(mylist2)

    # NEGATIVE INDEX
    item=mylist[-1]
    print(item)

    # ITERATE THROUGH LISTS
    for i in mylist:
        print(i)

    # SIMPLE IF ELSE CONDITION
    if "cherry" in mylist:
        print("found a cherry in your list!")
    else:
        print("no in my list!")

    # TIP : PRINT TRUE OR FALSE IF ITEM IS IN LIST
    print("banana" in mylist)

    # GET LENGTH OF AN LIST
    print(len(mylist))
    print(len(mylist2))

    # INSERT, APPEND, POP, REMOVE...
    mylist.append("lemon")
    mylist.insert(0, "blueberry")
    mylist.pop()
    item = mylist.pop()
    print(item + " popped")
    mylist.remove("apple")
    print("apple removed")
    print(mylist)

    # CLEARING WHOLE LIST
    mylist2.clear()
    print(mylist2)

    # SORTING LIST WITH .sort()
    mylist3= [3,1,5,10,2,4]
    mylist3.sort()
    print(mylist3)

    # SORTING LIST WITH sorted()
    mylist4 = [3, 1, 5, 10, 2, 4]
    print(mylist4)
    mylist5 = sorted(mylist4)
    print(mylist5)

    # INITIALIZING LIST WITH MULTIPLE VALUES OF THE SAME VALUE
    mylist6 = [1] * 10
    print(mylist6)

    mylist7 = [3] * 10
    print(mylist7)

    # ADDING THE VALUES OF 2 LIST IN 1 LIST
    print(mylist6 + mylist7)

    # SLICING 0-3 INDEX
    mylist10 = [1,2,3,4,5,6,7,8,9]
    a = mylist10[0:3]
    print(a)

    # SLICING EVERY 3RD VALUE
    mylist11 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = mylist11[0:8:3]
    print(b)

    # TIP : INVERTING A LIST
    mylist12 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    c = mylist12[::-1]
    print(c)

    # DEEP AND SHALLOW COPIES OF LISTS
    mylist13 = ["banana", "apple", "cherry"]
    # mylist14 = mylist13
    # mylist14 = mylist13.copy()
    mylist14 = list(mylist13)

    mylist14.append("pine")
    print(mylist13)
    print(mylist14)

    # SQUARING EACH ELEMENT OF ML15 AND WRITING IT IN ML16
    mylist15 = [0,1,2,3,4,5]
    mylist16 = [i*i for i in mylist15]

    print(mylist16)


# RUNNING THE FUNCTION FROM ABOVE
runMyList()