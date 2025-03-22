nums = [1, 2, 3, 4, 5, 6, 7, 2, 3, 2, 3, 2]
elem = 2
for index, value in enumerate(nums):
    if value == elem:
        print(str(index))
