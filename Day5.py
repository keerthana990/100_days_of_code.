import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# #type 1
# letters_created=random.sample(letters,nr_letters)
# symbols_created=random.sample(symbols,nr_symbols)
# numbers_created=random.sample(numbers,nr_numbers)
# password=symbols_created+numbers_created+letters_created
# random.shuffle(password)
# password_created=''.join(password)
# print("password:"+password_created)

#type2
# password=""
# for l in range(1,nr_letters+1):
#     password+=random.choice(letters)
# for n in range(1,nr_numbers+1):
#     password+=random.choice(numbers)
# for s in range(1,nr_symbols+1):
#     password+=random.choice(symbols)
# print("password: "+password)

#type3
password_l=[]
for l in range(1,nr_letters+1):
    password_l+=random.choice(letters)
for n in range(1,nr_numbers+1):
    password_l+=random.choice(numbers)
for s in range(1,nr_symbols+1):
    password_l+=random.choice(symbols)
random.shuffle(password_l)
password=""
for p in password_l:
    password+=p
print(f"password:{password}")
