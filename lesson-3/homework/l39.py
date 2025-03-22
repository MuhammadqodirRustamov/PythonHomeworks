list = [1,2,3,4,5,6,7,8,9,10, 11, 12, 13, 14]
numbers = [1,2,3,4]
nested = []
nested.append(list[:numbers[0]])
for index in range(1, len(numbers)):
    startIndex = sum(numbers[:index])
    endIndex = startIndex+numbers[index]
    nested.append(list[startIndex:endIndex])

print(nested)