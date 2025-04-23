from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

def get_drone_lights():
    lights = []
    for i in range(10):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        lights.append({'x': x, 'y': y, 'color': random.choice(['red', 'green', 'blue'])})
    return lights

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/drone_lights')
def drone_lights():
    return jsonify(get_drone_lights())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
