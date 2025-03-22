t = (1, 2, 3, 4, 5, 6, 7, 8, 9)
l = list(set(t))
l.remove(max(l))
print(max(l))