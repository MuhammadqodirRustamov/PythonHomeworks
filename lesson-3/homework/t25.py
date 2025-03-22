t = (1, 2, 2, 2, 3, 3, 4, 3, 4, 5, 6, 6, 6, 7, 8, 8, 8, 9, 9, 9)
l = []
for i in t:
    if t.count(i) == 1:
        l.append(i)
new = tuple(l)
print(new)