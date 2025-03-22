t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
num = 3
l = []
for i in t:
    for j in range(0, num):
        l.append(i)
new_t = tuple(l)
print(new_t)