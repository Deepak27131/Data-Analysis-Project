import hashlib
import itertools
import string

# Dummy User Database (For Educational Purposes Only)
user_database = {
    "user1": hashlib.sha256("test123".encode()).hexdigest(),
    "user2": hashlib.sha256("hello456".encode()).hexdigest(),
}

def crack_password_for_user(user_id, max_length=6):
    if user_id not in user_database:
        print("User ID not found in database.")
        return None

    # Get the hashed password for the given user
    hash_to_crack = user_database[user_id]
    print(f"Hash to crack for {user_id}: {hash_to_crack}")

    # Character set for brute force
    charset = string.ascii_lowercase + string.digits  # a-z, 0-9

    # Start brute force
    print("Starting brute force...")
    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempt_password = ''.join(attempt)
            attempt_hash = hashlib.sha256(attempt_password.encode()).hexdigest()

            if attempt_hash == hash_to_crack:
                print(f"Password found for {user_id}: {attempt_password}")
                return attempt_password

    print("Password not found within the given constraints.")
    return None

# User Input
user_id = input("Enter the user ID to crack the password: ").strip()  # Input user ID
max_length = int(input("Enter the maximum password length for brute force: ").strip())  # Max password length

# Run the function
crack_password_for_user(user_id, max_length)
