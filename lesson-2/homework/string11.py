my_str = input("Enter a string: ")
nums = "0123456789"
contains = False
for char in my_str:
    if char in nums:
        contains = True
        break 
print(contains)