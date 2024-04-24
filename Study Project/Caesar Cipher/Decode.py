# Module
from Alphabet_and_Number import alphabet, number

# Create a logic in fuction.
def decode():
    message_first = (input(f"Type your encrypted message : "))
    shift_number = 0
    while shift_number not in range(1, 26):
        shift_number = int(input(f"Type the shift number (1 - 25): "))
  
    message_list = list(message_first)
    result = ""
    alphabet_5 = alphabet * 5
    number_5 = number * 5
    for x in message_list:
        if x in alphabet:
            position = alphabet.index(x)
            result += alphabet_5[position - shift_number]
        elif x in number:
            position = number.index(x)
            result += number_5[position - shift_number]
        else:
            result += x
    print(f"Here's the decoded result : {result}")