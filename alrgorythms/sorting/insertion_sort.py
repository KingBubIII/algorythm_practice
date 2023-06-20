numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

# my first attempt
def insertionSort1(array):
    sorted_amt = 1
    for i in range(1,len(array)):
        temp_nums = array[:sorted_amt]
        if array[i] < temp_nums[0]:
            temp_nums.insert(0,array[i])
        elif array[i] > temp_nums[len(temp_nums)-1]:
            temp_nums.append(array[i])
        else:
            for j in range(len(temp_nums)):
                if array[i] < temp_nums[j]:
                    temp_nums.insert(j,array[i])
                    break
        array[:sorted_amt+1] = temp_nums
        sorted_amt += 1

insertionSort1(numbers)
print(numbers)