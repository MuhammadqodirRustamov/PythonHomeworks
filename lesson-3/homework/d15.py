d = {
    "apple": "olma",
    "banana": "banan",
    "peach": "shaftoli",
    "pear": "nok",
    "pineapple": "ananas",
    "cherry": "gilos",
}

keys = ["apple", "banana", "peach"]
values = ["olma", "banan", "shaftoli"]

d = dict()

for i in range(0, len(keys)):
    d[keys[i]] = values[i]
print(d)