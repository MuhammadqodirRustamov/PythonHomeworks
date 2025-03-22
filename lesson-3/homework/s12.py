s = {1, 2, 3, 4, 5, 6}
elem = 7
if elem in s:
    print("element already exists")
else: 
    s.add(elem)
    print(s)