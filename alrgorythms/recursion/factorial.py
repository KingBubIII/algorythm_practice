def findFactorialRecursive(number):
    if number > 1:
        answer = findFactorialRecursive(number-1)
    else:
        answer = number
    answer = answer * number
    return answer

def findFactorialIterative(number):
    answer = number
    while number != 1:
        number -= 1
        answer = answer * number
    return answer

# print(findFactorialIterative(5))
print(findFactorialRecursive(5))