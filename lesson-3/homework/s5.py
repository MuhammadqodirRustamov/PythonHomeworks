s = {1, 2, 3, 4, 5, 6}
elem = 4
try: 
    s.remove(elem)
    print("Element exists")
except:
    print("Element not found")