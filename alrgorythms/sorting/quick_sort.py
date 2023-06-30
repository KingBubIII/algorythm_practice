numbers = [0, 99, 6, 2, 1, 5, 63, 87, 283, 4, 44]

# first attempt
# may need to fix to exclude array slices
def quickSort(array):
    pivot_index = len(array)-1
    left_index = -1
    right_index = 0
    
    if len(array)==0:
        return []
    elif len(array)==1:
        return array
    else:
        while right_index != pivot_index:
            if array[right_index] < array[pivot_index]:
                left_index+=1
                temp = array[left_index]
                array[left_index] = array[right_index]
                array[right_index] = temp
            right_index+=1
        
        left_index+=1
        temp = array[left_index]
        array[left_index] = array[right_index]
        array[right_index] = temp

        return quickSort(array[:left_index]) + [array[left_index]] + quickSort(array[left_index+1:])

# Select first and last index as 2nd and 3rd parameters
result = quickSort(numbers)
print(result)

numbers = [0, 99, 6, 2, 1, 5, 63, 87, 283, 4, 44]

def quickSort2(array, left, right):
    pivot_index = right
    curr_change = left-1
    checking = left
    
    if len(array[left:right+1])==0:
        return []
    elif len(array[left:right+1])==1:
        return array[left:right+1]
    else:
        while array[checking] != array[pivot_index]:
            if array[checking] < array[pivot_index]:
                curr_change+=1
                temp = array[curr_change]
                array[curr_change] = array[checking]
                array[checking] = temp
            checking+=1
        
        curr_change+=1
        temp = array[curr_change]
        array[curr_change] = array[checking]
        pivot_index = curr_change
        array[checking] = temp

        array = quickSort2(array,left,pivot_index-1) + [array[pivot_index]] + quickSort2(array, pivot_index+1, checking)
        return array

# Select first and last index as 2nd and 3rd parameters
result = quickSort2(numbers,0, len(numbers)-1)
print(result)