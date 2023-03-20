#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



#get list of names
f = open("./Input/Names/invited_names.txt", "r")
names = f.readlines()
f.close()

with open("./Input/Letters/starting_letter.txt") as l:
    baseletter = l.read()

for name in names:
    name = name.strip()
    path = "./Output/ReadyToSend/" + name + '.txt'
    letter_content = baseletter.replace('[name]', name)
    with open(path,mode="w") as file:
        file.write(letter_content)
