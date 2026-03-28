import itertools
import hashlib

# Example hashed password (SHA-256 of "abc123")
stored_hash = hashlib.sha256("abc123".encode()).hexdigest()

def crack_password(chars, max_length):
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            guess = ''.join(guess)
            guess_hash = hashlib.sha256(guess.encode()).hexdigest()
            if guess_hash == stored_hash:
                return guess
    return None

# Character set and max length
characters = "abcdefghijklmnopqrstuvwxyz1234567890"
max_length = 6

# Brute force attack
result = crack_password(characters, max_length)
if result:
    print(f"Password cracked: {result}")
else:
    print("Password not found.")
