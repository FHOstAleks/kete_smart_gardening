from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['POST'])
def receive_data():
    print(request.get_json())
    data = request.get_json()
    print(data)
    sensor_id = data.get('sensor_id')
    sensor_name = data.get('sensor_name')
    user_id = data.get('user_id')
    action = data.get('action')
    # handle the received data here
    print(f"Received data: Sensor ID: {sensor_id}, Sensor Name: {sensor_name}, User ID: {user_id}, Action: {action}")
    return "Data Received"

if __name__ == '__main__':
    # host 0.0.0.0 ermöglicht es im lokalen Netzwerk verfügbar zu sein
    app.run(host='0.0.0.0', port=5000)