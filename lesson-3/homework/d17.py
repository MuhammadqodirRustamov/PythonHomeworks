d = {
    "apple": "olma",
    "banana": "banan",
    "peach": "shaftoli",
    "pear": "nok",
    "pineapple": {"one": "bir", "two":"ikki", "uch":"three"},
    "cherry": "gilos",
}
value = d["pineapple"]
inner_value = value["one"]
print(inner_value)