def store_user_data():
    """Store user data in a file"""
    print("User Registration System")
    print("========================")
    
    # Get user input
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    # Store data in file
    with open("users.txt", "a") as file:
        file.write(f"Name: {name}, Email: {email}, Password: {password}\n")
    
    print("User data stored successfully!")

def read_user_data():
    """Read and display user data from file"""
    try:
        with open("users.txt", "r") as file:
            print("\nStored User Data:")
            print("=================")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No user data found.")

# Main program
if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Register new user")
        print("2. View all users")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            store_user_data()
        elif choice == "2":
            read_user_data()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
