nums = [1, 2, 3, 4, 5, 6, 7]
subNums = [1, 2, 3, 8]
for i in subNums:
    if i not in nums:
        print(False)
        exit()
print(True)