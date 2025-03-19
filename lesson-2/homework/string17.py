my_str = input("Enter a string: ")
vowels = "aeiou"
res = ""
for i in my_str:
    if i in vowels:
        res += "*"
    else:
        res+= i
print(res)  