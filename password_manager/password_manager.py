from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


KEY_PATH = "key.key"  # stores a random salt (not a Fernet key)
DATA_PATH = "password.txt"


def get_or_create_salt():
    if not os.path.exists(KEY_PATH):
        salt = os.urandom(16)
        with open(KEY_PATH, "wb") as f:
            f.write(salt)
        return salt
    with open(KEY_PATH, "rb") as f:
        return f.read()


def derive_fernet_key(master_password):
    salt = get_or_create_salt()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    raw_key = kdf.derive(master_password.encode())
    return base64.urlsafe_b64encode(raw_key)


def add(fer):
    name = input("Account Name: ")
    pwd = input("Account Password: ")
    token = fer.encrypt(pwd.encode()).decode()
    with open(DATA_PATH, 'a', encoding='utf-8') as f:
        f.write(name + "|" + token + "\n")


def view(fer):
    if not os.path.exists(DATA_PATH):
        print("No passwords stored yet.")
        return
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            data = line.rstrip("\n")
            if not data:
                continue
            if "|" not in data:
                continue
            name, token = data.split("|", 1)
            try:
                password = fer.decrypt(token.encode()).decode()
            except Exception:
                print("Skipping a malformed or undecryptable entry for:", name)
                continue
            print("Name: ", name)
            print("Password: ", password)


def main():
    master_password = input("What is the master password: ")
    key = derive_fernet_key(master_password)
    fer = Fernet(key)

    while True:
        user_choose = input(
            "please enter your choice view for view password and add for adding password (view/add): "
        ).strip().lower()
        if user_choose == "view":
            view(fer)
        elif user_choose == "add":
            add(fer)
            continue
        elif user_choose in ["quit", "q"]:
            break
        else:
            continue


if __name__ == "__main__":
    main()
