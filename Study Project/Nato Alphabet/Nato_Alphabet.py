import pandas

data = pandas.read_csv("C:\\Users\\ASUS\\Documents\\ANDU\\Python\\Study Project\\Nato Alphabet\\nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    name_input = input(f"What's your name: ").upper()
    try :
        phonetic_name = [phonetic_dict[letter] for letter in name_input]
    except KeyError :
        print(f"Sorry, only letters in the alphabet please")
        generate_phonetic()
    else :
        print(phonetic_name)

generate_phonetic()