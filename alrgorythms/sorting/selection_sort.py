numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

def selectionSort(array):
    for i in range(len(array)):
        smallest_index = i
        for j in range(len(array[i::])):
            if array[i+j] < array[smallest_index]:
                smallest_index = i+j
        temp = array[i]
        array[i] = array[smallest_index]
        array[smallest_index] = temp
    
selectionSort(numbers)
print(numbers)