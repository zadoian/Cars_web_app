import json  # Imports the json module, which allows working with JSON data in Python
import os  # Imports the os module, which allows interacting with the operating system
import uuid  # Imports the uuid module, which allows generating unique identifiers

def clear_screen():  # Defines a function to clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')  # Uses the appropriate system command ('cls' for Windows, 'clear' for Unix) to clear the screen

def menu():  # Defines a function to display the menu to the user
    menu_text = """
    1. Add car
    2. Delete car
    3. View all cars
    4. Search for a car
    5. Save cars to file
    6. Load cars from file
    q. Quit
    """  # A string that contains the menu options
    print(menu_text)  # Prints the menu options to the user

def add_car():  # Defines a function to add a car to the list
    try:
        clear_screen()  # Clears the screen

        if os.path.exists("car_data.json"):  # Checks if the car data file exists
            with open("car_data.json", 'r') as file:  # Opens the file in read mode
                cars = json.load(file)  # Loads the JSON data from the file into the cars list
        else:
            cars = []  # If the file doesn't exist, initializes an empty list

        car_name = input("Enter car name: ")  # Asks the user to enter the car name
        car_model = input("Enter car model: ")  # Asks the user to enter the car model
        car_year = input("Enter car year: ")  # Asks the user to enter the car's year

        car_id = str(uuid.uuid4())  # Generates a unique identifier for the car

        car_entry = {  # Creates a dictionary entry for the car
            "id": car_id,
            "name": car_name,
            "model": car_model,
            "year": car_year
        }

        cars.append(car_entry)  # Adds the car entry to the list of cars

        answer = input("To save press [s]: ")  # Prompts the user to confirm saving the car details
        if answer == "s":  # If the user confirms saving
            with open("car_data.json", 'w') as file:  # Opens the file in write mode
                json.dump(cars, file, indent=4)  # Writes the list of cars to the file in JSON format with an indent of 4 spaces
            print(f"Car '{car_name}' has been added.")  # Prints a message indicating that the car was added
        else:
            print(f"Car '{car_name}' not added.")  # Prints a message indicating that the car was not added

        os.system("pause")  # Pauses the execution until the user presses any key
        clear_screen()  # Clears the screen

    except Exception as e:  # Catches any exceptions that occur
        print(f"An error occurred: {e}")  # Prints the error message

def delete_car():  # Defines a function to delete a car from the list
    try:
        clear_screen()  # Clears the screen
        if os.path.exists("car_data.json"):  # Checks if the car data file exists
            with open("car_data.json", 'r') as file:  # Opens the file in read mode
                cars = json.load(file)  # Loads the JSON data from the file into the cars list
        else:
            print("No car data file found.")  # Prints a message if the file is not found
            return  # Exits the function if the file doesn't exist

        car_id = input("Enter the car ID you want to delete: ")  # Asks the user to enter the car ID to delete

        cars = [car for car in cars if car['id'] != car_id]  # Filters out the car with the specified ID

        answer = input("To save press [s]: ")  # Prompts the user to confirm saving the changes
        if answer == "s":  # If the user confirms saving
            with open("car_data.json", 'w') as file:  # Opens the file in write mode
                json.dump(cars, file, indent=4)  # Writes the updated list of cars to the file
            print(f"Car with ID '{car_id}' has been deleted.")  # Prints a message indicating that the car was deleted
        else:
            print(f"Car with ID '{car_id}' not deleted.")  # Prints a message indicating that the changes were not saved

        os.system("pause")  # Pauses the execution until the user presses any key
        clear_screen()  # Clears the screen

    except Exception as e:  # Catches any exceptions that occur
        print(f"An error occurred: {e}")  # Prints the error message

def view_cars():  # Defines a function to view all cars in the list
    try:
        clear_screen()  # Clears the screen
        if os.path.exists("car_data.json"):  # Checks if the car data file exists
            with open("car_data.json", 'r') as file:  # Opens the file in read mode
                cars = json.load(file)  # Loads the JSON data from the file into the cars list
        else:
            print("No car data file found.")  # Prints a message if the file is not found
            return  # Exits the function if the file doesn't exist

        print("Cars in the list:")  # Prints a header for the car list
        for car in cars:  # Iterates over the cars list
            print(f"ID: {car['id']} - Name: {car['name']} - Model: {car['model']} - Year: {car['year']}")  # Prints the details of each car

        os.system("pause")  # Pauses the execution until the user presses any key
        clear_screen()  # Clears the screen

    except Exception as e:  # Catches any exceptions that occur
        print(f"An error occurred: {e}")  # Prints the error message

def search_car():  # Defines a function to search for a car in the list
    try:
        clear_screen()  # Clears the screen
        if os.path.exists("car_data.json"):  # Checks if the car data file exists
            with open("car_data.json", 'r') as file:  # Opens the file in read mode
                cars = json.load(file)  # Loads the JSON data from the file into the cars list
        else:
            print("No car data file found.")  # Prints a message if the file is not found
            return  # Exits the function if the file doesn't exist

        search_term = input("Enter the car name or ID to search: ")  # Asks the user to enter the car name or ID to search for

        found_cars = [car for car in cars if search_term.lower() in car['name'].lower() or car['id'] == search_term]  # Finds cars that match the search term

        if found_cars:  # Checks if any cars were found
            print("Cars found:")  # Prints a header for the found cars
            for car in found_cars:  # Iterates over the found cars
                print(f"ID: {car['id']} - Name: {car['name']} - Model: {car['model']} - Year: {car['year']}")  # Prints the details of each found car
        else:
            print(f"No cars found matching '{search_term}'.")  # Prints a message if no cars were found

        os.system("pause")  # Pauses the execution until the user presses any key
        clear_screen()  # Clears the screen

    except Exception as e:  # Catches any exceptions that occur
        print(f"An error occurred: {e}")  # Prints the error message

def save_cars():  # Defines a function to save the list of cars to a JSON file
    try:
        clear_screen()  # Clears the screen
        if os.path.exists("car_data.json"):  # Checks if the car data file exists
            with open("car_data.json", 'r') as file:  # Opens the file in read mode
                cars = json.load(file)  # Loads the JSON data from the file into the cars list
        else:
            cars = []  # If the file doesn't exist, initializes an empty list

        with open("car_data.json", 'w') as file:  # Opens the file in write mode
            json.dump(cars, file, indent=4)  # Writes the list of cars to the file in JSON format with an indent of 4 spaces
        print("Cars have been saved.")  # Prints a message indicating that the cars have been saved

        os.system("pause")  # Pauses the execution until the user presses any key
        clear_screen()  # Clears the screen

    except Exception as e:  # Catches any exceptions that occur
        print(f"An error occurred: {e}")  # Prints the error message

def load_cars():  # Defines a function to load the list of cars from a JSON file
    try:
        clear_screen()  # Clears the screen
        if os.path.exists("car_data.json"):  # Checks if the car data file exists
            with open("car_data.json", 'r') as file:  # Opens the file in read mode
                cars = json.load(file)  # Loads the JSON data from the file into the cars list
            print("Cars have been loaded.")  # Prints a message indicating that the cars have been loaded
        else:
            print("No car data file found.")  # Prints a message if the file is not found

        os.system("pause")  # Pauses the execution until the user presses any key
        clear_screen()  # Clears the screen

    except Exception as e:  # Catches any exceptions that occur
        print(f"An error occurred: {e}")  # Prints the error message

def exit_app():  # Defines a function to exit the application
    print("Goodbye!")  # Prints a goodbye message
    clear_screen()  # Clears the screen
    exit()  # Exits the application

def main():  # Defines the main function that controls the flow of the application
    while True:  # An infinite loop that runs the application until the user chooses to exit
        menu()  # Displays the menu to the user
        user_choice = input("Enter your choice: ")  # Prompts the user to enter their choice
        if user_choice == "1":  # If the user chooses to add a car
            add_car()  # Calls the add_car function
        elif user_choice == "2":  # If the user chooses to delete a car
            delete_car()  # Calls the delete_car function
        elif user_choice == "3":  # If the user chooses to view all cars
            view_cars()  # Calls the view_cars function
        elif user_choice == "4":  # If the user chooses to search for a car
            search_car()  # Calls the search_car function
        elif user_choice == "5":  # If the user chooses to save the cars
            save_cars()  # Calls the save_cars function
        elif user_choice == "6":  # If the user chooses to load the cars
            load_cars()  # Calls the load_cars function
        elif user_choice == "q":  # If the user chooses to quit the application
            exit_app()  # Calls the exit_app function
        else:
            print("Option not found! Try again.")  # Prints a message if the option is not found and asks the user to try again
            os.system("pause")  # Pauses the execution until the user presses any key
            clear_screen()  # Clears the screen

if __name__ == "__main__":  # Checks if the script is being run as the main program and not imported as a module
    main()  # Calls the main function to start the application
