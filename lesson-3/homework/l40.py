nums = [1,3,3,2,3,4,5,6,7,6,7]
new_list = []
for i in nums:
    if nums.count(i) == 1:
        new_list.append(i)
print(new_list)