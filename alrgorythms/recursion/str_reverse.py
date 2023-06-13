def reverseString(my_str):
    if len(my_str) == 1:
        reversed = my_str
    else:
        temp = reverseString(my_str[1::])
        reversed = temp + my_str[0]
    return reversed
    

print(reverseString('yoyo mastery'))
# print(reverseString('yo'))
# should return: 'yretsam oyoy'