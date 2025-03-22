nums = [1, 2, 3, 4, 5, 6, 7, 8]
length = len(nums)
if length % 2 == 0:
    print(f"{nums[round(length/2)-1]}, {nums[round(length/2)]}")
else:
    print(str(nums[round(length/2)-1]))