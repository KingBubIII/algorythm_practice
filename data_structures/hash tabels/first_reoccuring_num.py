def first_reoccurance2(mylist):
    mydict = {}

    for item in mylist:
        try:
            temp = mydict[item]
            return item
        except KeyError as e:
            mydict[item] = None
            
    return None


arr = [2,5,1,2,3,5,1,2,4]
arr2 = [2,1,1,2,3,5,1,2,4]
arr3 = [2,3,4,5]
arr4 = [2,5,5,2,3,5,1,2,4]

print(first_reoccurance2(arr))
print(first_reoccurance2(arr2))
print(first_reoccurance2(arr3))
print(first_reoccurance2(arr4))
print(first_reoccurance2([1,2]))