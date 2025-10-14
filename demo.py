import datetime

def calculate_age(birth_date):
    """Calculates the age in years from a given birth date."""
    today = datetime.date.today()
    # Calculate age by subtracting years, and adjust if the birthday hasn't occurred yet this year
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def get_valid_date_of_birth():
    """Prompts the user for their date of birth and validates it."""
    while True:
        dob_str = input("Enter your date of birth (DD-MM-YYYY or YYYY-MM-DD): ")
        try:
            # Check for the presence of '-' to help distinguish formats
            if '-' in dob_str:
                # Try parsing with DD-MM-YYYY first
                try:
                    birth_date = datetime.datetime.strptime(dob_str, "%d-%m-%Y").date()
                except ValueError:
                    # If DD-MM-YYYY fails, try YYYY-MM-DD
                    birth_date = datetime.datetime.strptime(dob_str, "%Y-%m-%d").date()
            else:
                print("Invalid date format. Please use DD-MM-YYYY or YYYY-MM-DD.")
                continue # Ask for input again if format is wrong

            # Validate that the date is not in the future
            today = datetime.date.today()
            if birth_date > today:
                print("Date of birth cannot be in the future. Please enter a valid date.")
                continue # Ask for input again if date is in future

            return birth_date # Return the valid date object

        except ValueError:
            # This catches errors from strptime if the date is invalid (e.g., 30-02-2023)
            print("Invalid date format or date. Please try again.")

def main():
    """Main function to run the age calculator."""
    print("Welcome to the Simple Age Calculator!")

    while True:
        # Get a valid date of birth from the user
        birth_date = get_valid_date_of_birth()
        # Calculate the age
        age = calculate_age(birth_date)

        # Display the calculated age
        print(f"Your current age is: {age} years.")

        # Ask if the user wants to perform another calculation
        another_calculation = input("Do you want to calculate another age? (yes/no): ").lower()
        if another_calculation != 'yes':
            print("Thank you for using the Age Calculator!")
            break # Exit the loop if the user doesn't want to continue

if __name__ == "__main__":
    # This ensures the main function runs only when the script is executed directly
    main()