while True:
    print("\n--- CALCULATOR ---")
    print("1. Add (+)")
    print("2. Subtract (-)")

    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    
    choice = input("Enter choice (1-5): ")
    
    if choice == "5":
        print("exit")
        break
        
    if choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == "1":
                result = num1 + num2
                print(f"Result: {num1} + {num2} = {result}")
                
            elif choice == "2":
                result = num1 - num2
                print(f"Result: {num1} - {num2} = {result}")
                
            elif choice == "3":
                result = num1 * num2
                print(f"Result: {num1} * {num2} = {result}")
                
            elif choice == "4":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print(f"Result: {num1} / {num2} = {result}")
        except:
            print("Invalid input. Please enter numbers only.")
    else:
        print("Invalid choice, please select 1-5.")