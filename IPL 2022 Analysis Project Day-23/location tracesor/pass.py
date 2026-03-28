import hashlib
import os
import json

# Function to hash a password
def hash_password(password):
    salt = os.urandom(16)  # Generate a random salt
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt + hashed_password  # Store salt and hash together

# Function to verify a password
def verify_password(stored_password, provided_password):
    salt = stored_password[:16]  # Extract the salt from the stored password
    stored_hash = stored_password[16:]  # Extract the hash
    new_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode(), salt, 100000)
    return new_hash == stored_hash  # Compare the hashes

# Function to save passwords to a file
def save_passwords(passwords, filename='passwords.json'):
    with open(filename, 'w') as f:
        json.dump(passwords, f)

# Function to load passwords from a file
def load_passwords(filename='passwords.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Main program
def main():
    passwords = load_passwords()
    
    while True:
        action = input("Would you like to (add) a password, (retrieve) a password, or (exit)? ").strip().lower()
        
        if action == 'add':
            site = input("Enter the site name: ")
            password = input("Enter the password: ")
            passwords[site] = hash_password(password)
            save_passwords(passwords)
            print("Password saved.")
        
        elif action == 'retrieve':
            site = input("Enter the site name: ")
            if site in passwords:
                provided_password = input("Enter the password to verify: ")
                if verify_password(passwords[site], provided_password):
                    print("Password is correct.")
                else:
                    print("Incorrect password.")
            else:
                print("No password found for that site.")
        
        elif action == 'exit':
            break
        
        else:
            print("Invalid action. Please choose 'add', 'retrieve', or 'exit'.")

if __name__ == "_main_":
    main()