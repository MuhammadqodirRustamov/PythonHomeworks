d = {
    "apple": "olma",
    "banana": "banan",
    "peach": "shaftoli",
    "pear": "nok",
    "pineapple": {"one": "bir", "two":"ikki", "uch":"three"},
    "cherry": "gilos",
}
for i in d.values():
     if isinstance(i, dict):
          print(True)
          quit()
print(False)