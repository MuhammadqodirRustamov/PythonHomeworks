import random
s = {1, 2, 3, 4, 5, 6}
l = list(s)
index = int(random.random()*len(l))
s.remove(l[index])
print(l[index])
print(s)