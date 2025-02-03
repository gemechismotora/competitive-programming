def calculator():
    print("Welcome to the Calculator!")
    print("Select an operation to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        # Take input from the user
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == '1':
                    print(f"The result of addition is: {num1 + num2}")
                elif choice == '2':
                    print(f"The result of subtraction is: {num1 - num2}")
                elif choice == '3':
                    print(f"The result of multiplication is: {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"The result of division is: {num1 / num2}")
                    else:
                        print("Error: Division by zero is not allowed.")
            except ValueError:
                print("Invalid input. Please enter numerical values.")
        else:
            print("Invalid choice. Please select a valid option.")

# Run the calculator function
calculator()
