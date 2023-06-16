numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

def bubbleSort(array):
    for count in range(len(numbers)):
        for index in range(0, len(numbers)-1):
            if numbers[index] > numbers[index+1]:
                temp = numbers[index]
                numbers[index] = numbers[index+1]
                numbers[index+1] = temp

bubbleSort(numbers)
print(numbers)