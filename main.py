import random

def generate(password_len):
    password = ""

    for i in range(password_len):
        password += random.choice(chars)
    return password

chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
passwords = {}

while True:
    for i in passwords:
        print(i, passwords[i])
    name = input('Название приложения: ')
    password_len = int(input("Введите длину вашего пароля:"))
    

    passwords[name] = generate(10)
