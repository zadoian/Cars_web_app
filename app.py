from flask import Flask, render_template, request, redirect, url_for, flash
import uuid
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load cars data from JSON file
def load_cars():
    if os.path.exists("car_data.json"):
        with open("car_data.json", 'r') as file:
            return json.load(file)
    return []

# Save cars data to JSON file
def save_cars(cars):
    with open("car_data.json", 'w') as file:
        json.dump(cars, file, indent=4)

@app.route('/')
def index():
    cars = load_cars()
    return render_template('index.html', cars=cars)

@app.route('/add', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        car_name = request.form['name']
        car_model = request.form['model']
        car_year = request.form['year']

        car_id = str(uuid.uuid4())
        car_entry = {
            "id": car_id,
            "name": car_name,
            "model": car_model,
            "year": car_year
        }

        cars = load_cars()
        cars.append(car_entry)
        save_cars(cars)

        flash('Car added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_car.html')

@app.route('/delete/<car_id>')
def delete_car(car_id):
    cars = load_cars()
    cars = [car for car in cars if car['id'] != car_id]
    save_cars(cars)

    flash('Car deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/search', methods=['GET', 'POST'])
def search_car():
    if request.method == 'POST':
        search_term = request.form['search']
        cars = load_cars()
        found_cars = [car for car in cars if search_term.lower() in car['name'].lower() or car['id'] == search_term]
        return render_template('index.html', cars=found_cars)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
