

#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt", mode="r") as name_file:
    names = name_file.read()
    name_list = list(names.split("\n"))
    print(name_list)

for name in name_list:
    with open("Input/Letters/starting_letter.txt", mode="r") as letter_file:
        letter = letter_file.read()
    letter = letter.replace('[name]', name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output_file:
        output_file.write(letter)
