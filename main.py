import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# It creates a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
# print(phonetic_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
        #  It creates a list of the phonetic code words from a word that the user inputs.
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()  # This is the best way to call the input again instead of a while loop.
    else:
        print(output_list)

generate_phonetic()
