import random
import string

ml = True
min_leng = 0

def generate_password(min_len, numbers=True, special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special_c = string.punctuation

    char = letters
    if numbers:
        char += digits
    if special_char:
        char += special_c

    password = ""
    req = False
    has_num = False
    has_special = False

    while not req or len(password) < min_len:
        new_char = random.choice(char)
        password += new_char

        if new_char in digits:
            has_num = True
        elif new_char in special_c:
            has_special = True

        req = True

        if numbers:
            req = has_num

        if special_char:
            req = req and has_special

    return password


while ml:
    try:
        min_leng = int(input("Please Enter minimum length : "))
        ml = False
    except:
        print("Please enter a number !")


has_n = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_spec = input("Do you want to have special characters (y/n)? ").lower() == "y"

pwd = generate_password(min_leng, has_n, has_spec)
print(pwd)
