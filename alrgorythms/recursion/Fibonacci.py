def fibonacciIterative(n):
    answer = 0
    first, second = 0, 1
    for count in range(n-1):
        answer = first + second
        first = second
        second = answer
    return answer

# print(fibonacciIterative(5))

def fibonacciRecursive(n):
    if n<2:
        return n
    else:
        behind2, behind1 = fibonacciRecursive(n-2), fibonacciRecursive(n-1)
        answer = behind2 + behind1
        return answer
    
print(fibonacciRecursive(5))