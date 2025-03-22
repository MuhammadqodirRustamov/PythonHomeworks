list = [1,2,3,4,5,6,7]
index = 4
if (len(list)>index):
    list.remove(index)
    print(list)
    print("Successfully removed.")
else: 
    print(f"Element at index {index} does not exist.")