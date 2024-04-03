#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"
with open("D:\\Python\\Study Project\\Mail Merge\\Input\\Names\\invited_names.txt") as name:
    names = name.readlines()

with open("D:\\Python\\Study Project\\Mail Merge\\Input\\Letters\\starting_letter.txt") as email:
    email_send = email.read()
    for name in names:
        stripped = name.strip()
        new_email = email_send.replace(PLACEHOLDER, stripped)
        with open(f"D:\\Python\\Study Project\\Mail Merge\\Output\\ReadyToSend\\Email_for_{stripped.capitalize()}.txt", mode = "w") as completed_email:
            completed_email.write(new_email)
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp