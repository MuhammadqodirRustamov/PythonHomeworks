d = {
    "apple": "olma",
    "banana": "banan",
    "peach": "shaftoli",
    "pear": "nok",
    "pineapple": "ananas",
    "cherry": "gilos",
}
min_length = 4
new_dic = dict()
for i in d.keys():
    if len(d[i]) > min_length:
        new_dic[i] = d[i]
print(new_dic)