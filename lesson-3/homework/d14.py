d = {
    "apple": "olma",
    "banana": "banan",
    "peach": "olma",
    "pear": "nok",
    "pineapple": "ananas",
    "cherry": "olma",
}
value = "olma"
l = []
for i in d.keys():
    if d[i] == value:
        l.append(i)
print(l)