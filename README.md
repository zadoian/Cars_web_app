
# Car Management Application

This Python application allows users to manage a list of cars. The app provides functionalities to add, delete, view, search, save, and load car data. Each car is assigned a unique identifier (UUID) to allow for multiple cars with the same name without overwriting existing entries.

## Features

- **Add Car:** Allows the user to add multiple cars, even with the same name, to the list. Each car is given a unique ID.
- **Delete Car:** Removes a car from the list by its unique ID.
- **View All Cars:** Displays all cars currently in the list, including their ID, name, model, and year.
- **Search for Car:** Find and display details of specific cars by their name or ID.
- **Save Cars to File:** Saves the current list of cars to a JSON file for persistent storage.
- **Load Cars from File:** Loads the list of cars from a JSON file.
- **Exit the Application:** Closes the application.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/car-management-app.git
   cd car-management-app
   ```

2. Ensure you have Python 3.x installed on your system.

3. Run the application:
   ```bash
   python car_management.py
   ```

## How to Use

### Menu Options

1. **Add Car:**
   - Prompts you to enter the car's name, model, and year.
   - Assigns a unique ID to the car and adds it to the list.

2. **Delete Car:**
   - Prompts you to enter the car's unique ID.
   - Removes the car with the corresponding ID from the list.

3. **View All Cars:**
   - Displays a list of all cars currently stored in the system, including their ID, name, model, and year.

4. **Search for Car:**
   - Prompts you to enter a car's name or ID.
   - Displays all cars that match the search term.

5. **Save Cars to File:**
   - Saves the list of cars to `car_data.json` in JSON format.

6. **Load Cars from File:**
   - Loads the list of cars from `car_data.json`.

7. **Quit:**
   - Exits the application.

## Code Overview

- **main()**: The main function that controls the application's flow.
- **add_car()**: Adds a car to the list with a unique ID.
- **delete_car()**: Deletes a car based on its ID.
- **view_cars()**: Displays all cars in the list.
- **search_car()**: Searches for cars by name or ID.
- **save_cars()**: Saves the car list to a JSON file.
- **load_cars()**: Loads the car list from a JSON file.
- **clear_screen()**: Clears the terminal screen for better readability.
- **menu()**: Displays the menu options to the user.
- **exit_app()**: Exits the application.

## Example Usage

```bash
$ python car_management.py
1. Add car
2. Delete car
3. View all cars
4. Search for a car
5. Save cars to file
6. Load cars from file
q. Quit
Enter your choice: 1
Enter car name: Toyota
Enter car model: Corolla
Enter car year: 2020
To save press [s]: s
Car 'Toyota' has been added.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or fixes.

## Contact

If you have any questions or suggestions, feel free to contact me at [your-email@example.com].
