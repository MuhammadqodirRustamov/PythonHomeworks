import re


def split_words(_txt):
    words_lowercased = [str(word).lower() for (word) in re.findall(r'\b\w+\b', _txt)]
    return words_lowercased


def count_words(_words):
    words_set = set(_words)
    words_dic = dict()
    for word in words_set:
        amount = list(_words).count(word)
        words_dic[word] = amount
    words_dic = dict(sorted(words_dic.items(), key=lambda item: item[1], reverse=True))
    return words_dic


def get_words():
    _words = []
    try:
        with open("sample.txt") as file:
            while True:
                line = file.readline()
                _words.extend(split_words(line))
                if not line:
                    break
    except FileNotFoundError:
        with open("sample.txt", mode="w+") as file:
            new_content = input("File not found. Enter new content for the file: ")
            file.write(new_content)
            words.extend(split_words(new_content))
    finally:
        return _words


words = get_words()
words_counted = count_words(words)

print(f"Total words: {len(words_counted.items())}")
top_count = int(input("How many top words to show: "))
print(f"Top {top_count} most common words:")
if top_count >= len(list(words_counted.items())):
    for i in words_counted.items():
        print(f"{i[0]} - {i[1]} times")
else:
    for i in range(top_count):
        print(f"{list(words_counted.items())[i][0]} - {list(words_counted.items())[i][1]} times")

with open("word_count_report.txt", mode="w") as file:
    content = "Word Count Report\n"
    content += "Total words: "
    content += str(len(list(words_counted.values())))
    content += "\nTop "
    content += str(top_count)
    content += " words:"
    for index in range(top_count):
        i = list(words_counted.items())[index]
        content += f"\n{i[0]} - {i[1]}"
    file.write(content)
