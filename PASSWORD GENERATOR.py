import random
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
          'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x','y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 
          'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R',
          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers= ['0','1','2','3','4','5','6','7','8','9']
symbols= ['!','@','#','$','%','^','&','*']
print("WELCOME TO PASSWORD GENERATOR")
l=int(input("HOW MANY LETTERS DO YOU WANT\n"))
n=int(input("HOW MANY NUMBERS DO YOU WANT\n"))
s=int(input("HOW MANY SYMBOLS DO YOU WANT\n"))
password=[]
for char in range(1,l+1):
    password+= random.choice(letters)
for char in range(1,l+1):
    password+= random.choice(numbers)
for char in range(1,l+1):
    password+= random.choice(symbols)
random.shuffle(password)
#print (password)
password123 = ""
for char in password:
    password123 += char
print("YOUR NEW PASSWORD IS:",password123)
