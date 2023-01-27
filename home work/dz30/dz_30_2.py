"""
Написати програми для реєстрації і авторизації користувача з наступним функціоналом:
- отримання в інтерактивному режимі логіну і пароля користувача;
- верифікація пароля і його шифрування за алгоритмом обраним алгоритмом шифрування;
- запис пари "логін-пароль" у словник з перевіркою на колізії;
- авторизація користувача за логіном і паролем.
"""

import hashlib


def import_users_base():
    users_base = {}
    with open("users_base.txt", "r") as f:
        for line in f:
            line = line.strip().split(":")
            users_base[line[0]] = line[1]
    return users_base


def encrypt_password(password):
    password = hashlib.md5(password.encode())
    return password.hexdigest()


def check_user_exists(login, users_base):
    if login in users_base:
        return True
    else:
        return False


def register_user(login, password, users_base):
    users_base[login] = password
    with open("users_base.txt", "w") as f:
        for user in users_base:
            f.write(user + ":" + users_base[user] + "\n")


users_base = import_users_base()

while True:
    login = input("Задайте логін: ")
    if check_user_exists(login, users_base):
        print("Користувач уже існує, введіть інший логін.")
    else:
        password = input("Задайте пароль: ")
        password = encrypt_password(password)
        register_user(login, password, users_base)
        print("Реєстрація успішна")
        break
