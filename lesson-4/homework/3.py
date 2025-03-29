txt = "abcabcdabcdeabcdefabcdefg"

new_txt = []
do_not_underscore = {'a', 'e', 'i', 'o', 'u'}
last_underscore = -1

for index, char in enumerate(txt):
    new_txt.append(char)
    if index == len(txt)-1:
        break
    if char in do_not_underscore:
        continue
    if index - last_underscore > 2:
        new_txt.append("_")
        do_not_underscore.add(char)
        last_underscore = index
print("".join(new_txt))