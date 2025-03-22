t = ("apple", "olma", "banana", "banan", "peach", "shaftoli")
d = dict()
for i in range(0, len(t), 2):
    d[t[i]] = t[i+1]
print(d)