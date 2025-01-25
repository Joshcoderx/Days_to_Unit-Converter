def day_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours."
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes."
    else:
        return "Unsupported unit."

def validate_and_execute(days_and_units_dict):
    try:
        user_input_number = int(days_and_units_dict["days"])
        if user_input_number > 0:
            calculated_value = day_to_units(user_input_number, days_and_units_dict["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0. Please enter a positive number.")
        else:
            print("You entered a negative number. No conversion for you!")
    except ValueError:
        print("Your input is not a valid number. Don't ruin my program!")

user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter a number of days and conversion unit\n")
    if user_input == "exit":
        print("Goodbye!")
        break
    try:
        days_and_units = user_input.split(":")
        if len(days_and_units) == 2:  # Validate input format
            days_and_units_dict = {"days": days_and_units[0], "unit": days_and_units[1]}
            validate_and_execute(days_and_units_dict)
        else:
            print("Invalid input format. Please use 'number:unit' format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")