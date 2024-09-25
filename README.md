# Simple Drive Locker

This script is a simple tool that helps you securely store and retrieve passwords for usernames. It uses the **Fernet** symmetric encryption from the `cryptography` library to encrypt and decrypt passwords.

## Features
- **Encrypt and store passwords**: Safely store your passwords using generated encryption keys.
- **Retrieve passwords**: Access stored passwords by entering your username.
- **Simple Menu**: Choose from three options: Make a new entry, retrieve a password, or exit the program.

## Requirements
- Python 3.x
- Cryptography library (`pip install cryptography`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/simple-drive-locker.git
   cd simple-drive-locker
Usage
Make an entry for username and password:
Select option 1 from the menu, input your username and password. The password will be encrypted and stored in lock.txt.

Retrieve a password:
Select option 2, enter the username, and the corresponding password will be decrypted and displayed.

Exit the program:
Choose option 3 to exit.

Notes
The encryption key for each password is stored in key.txt, while usernames are stored in usernames.txt.
Make sure to securely handle these files, as they contain sensitive information.
