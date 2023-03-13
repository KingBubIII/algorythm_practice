def mergeSortArray(input1, input2):
    output = []

    while input1 or input2:
        arrayItem1 = input1[0] if input1 else False
        arrayItem2 = input2[0] if input2 else False

        if not input2 or arrayItem1 < arrayItem2:
            output.append(arrayItem1)
            del input1[0]
        else:
            output.append(arrayItem2)
            del input2[0]

    return output

print(mergeSortArray([0,3,4,31],[4,6,30]))