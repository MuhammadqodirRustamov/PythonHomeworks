d = {
    "apple": "olma",
    "banana": "banan",
    "peach": "shaftoli",
    "pear": "nok",
    "pineapple": "ananas",
    "cherry": "gilos",
}
new_d = dict()
for i in d.keys():
    new_d[d[i]] = i
print(new_d)