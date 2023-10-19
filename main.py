# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# Looping through dictionaries:
# student_dict_formatted = {name:score for (name, score) in student_dict.items()}
# print(student_dict_formatted)

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# It creates a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
# print(phonetic_dict)

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
#  It creates a list of the phonetic code words from a word that the user inputs.
print(output_list)



