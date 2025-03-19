my_list = []
count = int(input("How many words: "))
for i in range(count):
    my_list.append(input(f"{i+1}: ").strip())
res = ""
for i in my_list:
    res += i + ' '
print(res)