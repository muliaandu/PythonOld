import pandas

data = pandas.read_csv("D:\\Python\\Study Project\\Nato Alphabet\\nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

name_input = input(f"What's your name: ").upper()
phonetic_name = [phonetic_dict[letter] for letter in name_input]
print(phonetic_name)
