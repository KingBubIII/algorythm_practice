# O(n^2)
def first_reoccurance2(mylist):
    pos_sum = None
    for count, item in enumerate(mylist):
        test = mylist[count+1:]
        for count2, item2 in enumerate(test):
            if item == item2:
                if pos_sum is None or count2 < pos_sum:
                    pos_sum = count2 + 1
    if pos_sum is None:
        return pos_sum
    else:
        return mylist[pos_sum]

arr = [2,5,1,2,3,5,1,2,4]
arr2 = [2,1,1,2,3,5,1,2,4]
arr3 = [2,3,4,5]
arr4 = [2,5,5,2,3,5,1,2,4]

print(first_reoccurance2(arr))
print(first_reoccurance2(arr2))
print(first_reoccurance2(arr3))
print(first_reoccurance2(arr4))
print(first_reoccurance2([1,2]))