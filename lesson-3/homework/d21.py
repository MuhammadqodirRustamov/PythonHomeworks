d = {
    "apple": "olma",
    "banana": "banan",
    "peach": "shaftoli",
    "pear": "nok",
    "pineapple": "ananas",
    "cherry": "gilos",
}
values = sorted(list(d.values()))
sorted_dic = dict()
for i in values:
    for j in d.keys():
        if d[j] == i:
            sorted_dic[j] = i

print(sorted_dic)