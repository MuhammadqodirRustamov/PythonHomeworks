sentence = input("Enter a sentence: ")
res = ""
for i in sentence.split():
    res += i[0].upper()
print(res)