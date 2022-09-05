#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
with open("./Input/Names/invited_names.txt", "r") as invited_names_file:
    with open("./Input/Letters/starting_letter.txt") as starting_letter_file:
        names = invited_names_file.readlines()
        starting_letter = starting_letter_file.read()
        for name in names:
            starting_letter_cp = starting_letter
            name = name.strip('\n')
            starting_letter_cp = starting_letter_cp.replace("[name]", name)
            with open(f"./Output/ReadyToSend/mail_{name}", "w") as output_mail_file:
                output_mail_file.writelines(starting_letter_cp)
        #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
            #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp