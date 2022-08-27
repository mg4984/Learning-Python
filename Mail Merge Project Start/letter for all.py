PLACEHOLDER="[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content= letter_file.read()
    
    for name in names:
        strip=name.strip()
        new_letter= letter_content.replace(PLACEHOLDER , strip)
        print(new_letter)
    
        with open(f"./Output/ReadyToSend/letter_for_{strip}.txt" , mode="w") as completed_letter:
            completed_letter.write(new_letter)