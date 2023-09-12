from cryptography.fernet import Fernet
import getpass

def encrypt_text(text, key):
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text.encode())
    return encrypted_text


def decrypt_text(encrypted_text, key):
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text).decode()
    return decrypted_text

test = 1
print("DRIVE MENU")
print("1. Make an entry for username and password")
print("2. Want to see the password of yours :)")
print("3. Exit")

while test:
    choice = input("Enter your choice (1/2/3) for exit: ")
    if choice == '1':
        print("Entry " + str(test))
        user_name = input("Enter your username: ")
        with open("usernames.txt", "a+") as user_locker:
            user_locker.write(user_name + "\n")
        passwd = getpass.getpass("Enter your password: ")  
        key = Fernet.generate_key()
        key_list = open("key.txt", "ab")  
        key_list.write(key + b'\n')  
        key_list.close()
        temp = encrypt_text(passwd, key)
        with open("lock.txt", "ab") as locker:
            locker.write(temp + b'\n')  
    elif choice == '2':
        user_line = 0
        d_username = input("Enter the username to know your password: ")
        user_locker = open("usernames.txt", "r")
        for line in user_locker:
            if d_username == line.strip():  
                break
            user_line += 1
        pass_line = 0
        key_line = 0
        key_list = open("key.txt", "rb")
        for line in key_list:
            if key_line == user_line:
                key2 = line.strip()
                break
            key_line += 1
        locker = open("lock.txt", "rb")
        for line in locker:
            if pass_line == user_line:
                print("Password:", decrypt_text(line.strip(), key2))
                break
            pass_line += 1
    elif choice == '3':
        break  
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
    test += 1
