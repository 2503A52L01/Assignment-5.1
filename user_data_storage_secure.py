import bcrypt
import re
import os
from getpass import getpass

def validate_email(email):
    """Validate email format using regex"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def hash_password(password):
    """Hash password using bcrypt with salt"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(stored_hash, password):
    """Verify password against stored hash"""
    return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))

def store_user_data_secure():
    """Store user data securely with hashed password"""
    print("Secure User Registration System")
    print("================================")
    
    # Get user input with validation
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return
    
    email = input("Enter your email: ").strip()
    if not validate_email(email):
        print("Invalid email format!")
        return
    
    # Use getpass for secure password input (doesn't echo to screen)
    password = getpass("Enter your password: ")
    if len(password) < 8:
        print("Password must be at least 8 characters long!")
        return
    
    # Hash the password
    hashed_password = hash_password(password)
    
    # Store data in file (only store hashed password)
    try:
        with open("users_secure.txt", "a") as file:
            file.write(f"Name: {name}, Email: {email}, PasswordHash: {hashed_password}\n")
        
        print("User data stored securely!")
        
    except IOError as e:
        print(f"Error storing data: {e}")

def read_user_data_secure():
    """Read and display user data from secure file"""
    try:
        with open("users_secure.txt", "r") as file:
            print("\nStored User Data (Secure):")
            print("==========================")
            for line in file:
                # Mask the password hash for display
                if "PasswordHash:" in line:
                    parts = line.split("PasswordHash:")
                    display_line = parts[0] + "PasswordHash: [HASHED]"
                    print(display_line.strip())
                else:
                    print(line.strip())
    except FileNotFoundError:
        print("No secure user data found.")

def verify_user_login():
    """Verify user login credentials"""
    print("\nUser Login Verification")
    print("=======================")
    
    email = input("Enter your email: ").strip()
    password = getpass("Enter your password: ")
    
    try:
        with open("users_secure.txt", "r") as file:
            for line in file:
                if f"Email: {email}" in line:
                    # Extract the stored hash
                    hash_start = line.find("PasswordHash: ") + len("PasswordHash: ")
                    stored_hash = line[hash_start:].strip()
                    
                    if verify_password(stored_hash, password):
                        print("Login successful!")
                        return
                    else:
                        print("Invalid password!")
                        return
        
        print("User not found!")
        
    except FileNotFoundError:
        print("No user data found.")
    except Exception as e:
        print(f"Error during login: {e}")

# Main program
if __name__ == "__main__":
    while True:
        print("\nSecure Options:")
        print("1. Register new user (secure)")
        print("2. View all users (secure display)")
        print("3. Verify user login")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            store_user_data_secure()
        elif choice == "2":
            read_user_data_secure()
        elif choice == "3":
            verify_user_login()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
