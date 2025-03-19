my_str = input("Enter a string: ")
vowels = "aeiou"
vowel_count = sum(1 for char in my_str if char.lower() in vowels)
print(f"Vowels: {vowel_count}  Consonants: {len(my_str)-vowel_count}")