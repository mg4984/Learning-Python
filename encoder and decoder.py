alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
          'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x','y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
          'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x','y', 'z']
direction = input("type 'encode' or 'decode'\n")
text= input("ENTER YOUR MESSAGE\n")
shift=int(input("ENTER THE SHIFT NUMBER\n"))
def encrypt(plain_text , shift_amount):
    cypher_text=" "
    for letter in plain_text:
        position= alphabet.index(letter)
        new_position= position+ shift_amount
        new_letter= alphabet[new_position]
        cypher_text+= new_letter 
    print("THE ENCODED TEXT IS",cypher_text)
    


def decrypt(plain_text,shift_amount):
    cypher_text= ' '
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position-shift_amount
        new_letter= alphabet[new_position]
        cypher_text+= new_letter
    print("THE DECODED TEXT IS",cypher_text)


if direction == "encode" :
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(plain_text=text , shift_amount=shift)