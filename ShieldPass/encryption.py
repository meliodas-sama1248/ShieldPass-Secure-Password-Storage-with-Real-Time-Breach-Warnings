from cryptography.fernet import Fernet
import os

# Generate and save encryption key if it does not exist
def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        print("New encryption key generated!")

# Load the saved encryption key
def load_key():
    if not os.path.exists("secret.key"):
        generate_key()  # Ensure key exists before loading
    return open("secret.key", "rb").read()

# Ensure key is generated before using encryption functions
generate_key()
key = load_key()
cipher_suite = Fernet(key)

# Encrypt password
def encrypt_password(password):
    return cipher_suite.encrypt(password.encode()).decode()

# Decrypt password
def decrypt_password(encrypted_password):
    return cipher_suite.decrypt(encrypted_password.encode()).decode()
