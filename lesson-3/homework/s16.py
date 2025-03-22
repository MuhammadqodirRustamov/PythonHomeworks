s = {1, 2, 3, 4, 5, 6}
new_s = set()
for i in s:
    if i % 2 == 0:
        new_s.add(i)
print(new_s)