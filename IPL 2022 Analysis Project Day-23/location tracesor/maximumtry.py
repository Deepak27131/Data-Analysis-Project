import hashlib
import itertools
import string

# Example stored hashed password (e.g., hash of "abc123")
stored_hash = hashlib.sha256("abc123".encode()).hexdigest()

# Function to brute force a password
def brute_force_crack(user_id, max_length):
    print(f"Attempting to crack password for User ID: {user_id}")
    
    chars = string.ascii_lowercase + string.digits  # Character set (a-z, 0-9)
    
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            guess_password = ''.join(guess)
            guess_hash = hashlib.sha256(guess_password.encode()).hexdigest()
            
            print(f"Trying: {guess_password}")
            
            if guess_hash == stored_hash:
                print(f"Password cracked for User ID {user_id}: {guess_password}")
                return
    
    print("Password not found within the given length.")

# Input User ID and Max Length for Brute Force
user_id = input("Enter the User ID: ")
max_length = int(input("Enter the maximum password length to try: "))

# Run brute force crack
brute_force_crack(user_id, max_length)
# Compare this snippet from IPL%202022%20Analysis%20Project%20Day-23/location%20tracesor/maximumtry.py: