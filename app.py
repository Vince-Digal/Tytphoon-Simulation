from flask import Flask, render_template, jsonify
import pandas as pd
import math

app = Flask(__name__)

# Load IBTrACS data 
IBTRACS_FILE_PATH = r'C:\Users\Clyde B. Verano\OneDrive\Desktop\jupyter projects\data\ibtracs.ALL.list.v04r01.csv'

# Read the IBTrACS data into a pandas DataFrame
df = pd.read_csv(IBTRACS_FILE_PATH, low_memory=False)

# Sample typhoon information (replace with your actual typhoon data or database)
typhoon_data = {
    "name": "Typhoon Example",
    "year": 2025,
    "latitude": 12.8797,  # Initial position of the typhoon
    "longitude": 121.7740,
    "max_wind_speed": 120,  # in knots
    "min_pressure": 960,  # in mb
    "direction": 270,  # West
    "movement_speed": 20  # in km/h
}

@app.route('/')
def home():
    return render_template('index.html')  # Renders the main HTML page

@app.route('/typhoon_data_full')
def typhoon_data_full():
    # Return typhoon data for the frontend (wind speed, pressure, etc.)
    return jsonify({
        "wind_speed": typhoon_data["max_wind_speed"],
        "pressure": typhoon_data["min_pressure"],
        "direction": typhoon_data["direction"],
        "movement_speed": typhoon_data["movement_speed"]
    })

@app.route('/typhoon_movement')
def typhoon_movement():
    # Simulate movement based on direction and speed
    lat_change = (math.cos(math.radians(typhoon_data['direction'])) * typhoon_data['movement_speed']) / 111  # 111 km per degree latitude
    lon_change = (math.sin(math.radians(typhoon_data['direction'])) * typhoon_data['movement_speed']) / (111 * math.cos(math.radians(typhoon_data['latitude'])))
    
    # Update the typhoon's position
    typhoon_data['latitude'] += lat_change
    typhoon_data['longitude'] += lon_change

    # Return updated position
    return jsonify({
        "name": typhoon_data["name"],
        "latitude": typhoon_data["latitude"],
        "longitude": typhoon_data["longitude"],
        "max_wind_speed": typhoon_data["max_wind_speed"],
        "min_pressure": typhoon_data["min_pressure"]
    })

if __name__ == '__main__':
    app.run(debug=True)  # Start the Flask development server
