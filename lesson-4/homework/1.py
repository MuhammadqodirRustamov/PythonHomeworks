list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

new_list = []

for i in list1:
    if i not in list2:
        new_list.append(i)
for i in list2:
    if i not in list1:
        new_list.append(i)
print(new_list)