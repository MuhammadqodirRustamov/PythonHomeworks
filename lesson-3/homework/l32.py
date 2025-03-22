list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]
list2 = [1, 2, 3, 4, 5, 6, 7]
merged = list1.copy()
merged.extend(list2)
merged.sort()
print(merged)