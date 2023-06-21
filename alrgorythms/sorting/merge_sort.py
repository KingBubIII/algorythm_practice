numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

# first try
def merge1(left, right):
    result = []

    for i in range((len(left)+len(right))):
        if left == []:
            result.extend(right)
            break
        elif right == []:
            result.extend(left)
            break
        elif left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        elif left[0] > right[0]:
            result.append(right[0])
            right.pop(0)
    
    return result

# reworked to use a while loop
def merge2(left, right):
    result = []

    while left != [] and right != []:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        elif left[0] > right[0]:
            result.append(right[0])
            right.pop(0)
    if left == []:
        result.extend(right)
    elif right == []:
        result.extend(left)

    return result

def mergeSort (array):
    if (len(array) == 1):
        return array
    
    # Split Array in into right and left
    sub_arr_len = len(array)//2
    left, right = array[:sub_arr_len], array[sub_arr_len:]

    return merge2(mergeSort(left), mergeSort(right))




answer = mergeSort(numbers)
# answer = merge([44, 99], [2, 6])
print(answer)