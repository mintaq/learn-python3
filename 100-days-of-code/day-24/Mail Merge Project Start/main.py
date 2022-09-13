#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER_NAME = "[name]"

with open("./Input/Names/invited_names.txt", "r") as invited_names_file:
    names = invited_names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as starting_letter_file:
    starting_letter = starting_letter_file.read()
    for name in names:
        starting_letter_cp = starting_letter
        name = name.strip('\n')
        starting_letter_cp = starting_letter_cp.replace(PLACEHOLDER_NAME, name)
        with open(f"./Output/ReadyToSend/mail_{name}.txt", "w") as output_mail_file:
            output_mail_file.writelines(starting_letter_cp)