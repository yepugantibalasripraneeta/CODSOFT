import random
import string

while True:
    print("\n--- PASSWORD GENERATOR ---")
    print("1. Generate Password")
    print("2. Exit")
    
    choice = input("Enter choice (1-2): ")
    
    if choice == "2":
        print("exit")
        break
        
    elif choice == "1":
        try:
            length = int(input("Enter password length: "))
            
            if length < 4:
                print("Password should be at least 4 characters long for safety.")
            else:
                lower = string.ascii_lowercase
                upper = string.ascii_uppercase
                digits = string.digits
                symbols = string.punctuation
                
                all_chars = lower + upper + digits + symbols
                
                password = "".join(random.sample(all_chars, length))
                
                print(f"Generated Password: {password}")
        except:
            print("Please enter a valid number for the length.")
    else:
        print("Invalid choice, please select 1 or 2.")