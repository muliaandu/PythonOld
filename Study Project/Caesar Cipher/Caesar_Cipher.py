# Welcome Message.
print(f"Welcome to Caesar Cipher.")

# Module
from Encode import encode
from Decode import decode

# Variable.
running = True
running_again = ""

# Print out the result.
while running is True:
    # Ask for Encode or Decode.
    pick = ""
    while pick != "encode" and pick != "decode":
        pick = input(f"Type 'encode' to encrypt, type 'decode' to decript : ").lower()

    if pick == "encode":
        encode()
        while running is True:
            running_again = input(f"Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
            if running_again == "yes":
                break
            elif running_again == "no":
                running = False
            else:
                continue
    elif pick == "decode":
        decode()
        while running is True:
            running_again = input(f"Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
            if running_again == "yes":
                break
            elif running_again == "no":
                running = False
            else:
                continue
    else:
        continue

print(f"Thank you for using Caesar Cipher Encoder and Decoder.")