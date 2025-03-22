d = {
    "apple": "olma",
    "banana": "banan",
    "peach": "shaftoli",
    "pear": "nok",
    "pineapple": "ananas",
    "cherry": "gilos",
}
key = "apple"
val = d.get(key)
if (val == None):
    print("key not found")
else:
    print(val)