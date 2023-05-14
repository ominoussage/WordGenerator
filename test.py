import random

print("Welcome to my Word Generator!")
small_consonant_list = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
small_vowel_list = ["a", "e", "i", "o", "u"]
capital_consonant_list = [c.upper() for c in small_consonant_list]
captial_vowel_list = [v.upper() for v in small_vowel_list]
vowel_list = small_vowel_list + captial_vowel_list
consonant_list = small_consonant_list + capital_consonant_list

try:
    first_letter = input("Put the first letter of your word of choice: ")
except ValueError:
    print("Please input a letter.")
try:
    word_length = int(input("Insert the number of letters for the word: "))
except ValueError:
    print("Please input a number.")

if first_letter in consonant_list:
    print(f"{first_letter}{random.choice(small_vowel_list)}{random.choice(small_consonant_list)}")

elif first_letter in vowel_list:
    print(f"{first_letter}{random.choice(small_consonant_list)}{random.choice(small_vowel_list)}")