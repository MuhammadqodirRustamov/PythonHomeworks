d1 = {
    "apple": "olma",
    "banana": "banan",
    "peach": "shaftoli",
    }
d2 = {"peach": "shaftoli",
    "pear": "nok",
    "pineapple": "ananas",
    "cherry": "gilos",
}
for i in d1.keys():
    if i in d2.keys():
        print(True)
        quit()
print(False)