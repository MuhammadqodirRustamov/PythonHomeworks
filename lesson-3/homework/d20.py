d = {
    "banana": "banan",
    "peach": "shaftoli",
    "pear": "nok",
    "apple": "olma",
    "pineapple": "ananas",
    "cherry": "gilos",
}
keys = sorted(d.keys())
sorted_dic = dict()
for i in keys:
    sorted_dic[i] = d[i]
print(sorted_dic)