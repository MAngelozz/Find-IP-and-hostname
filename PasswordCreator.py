import secrets 
import string

def password_gen (password_lenght):

    characters = string.ascii_letters + string.digits

    secure_password = ''.join(secrets.choice(characters) for i in range(password_lenght))

    return secure_password

def main():

    user_password_lenght = int(input("Input your digits for password: "))

    print("Password Generated: ", password_gen(user_password_lenght))


main()