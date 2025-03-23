txt = "abcabcdabcdeabcdefabcdefg"

new_txt = ""
vowels = "aeuio"
underscored = []
last_underscore = -1

for index, char in enumerate(txt):
    new_txt += char
    if index == len(txt)-1:
        break
    if char in vowels:
        continue
    if char in underscored:
        continue
    if index - last_underscore > 2:
        new_txt += "_"
        underscored.append(char)
        last_underscore = index
print(new_txt)