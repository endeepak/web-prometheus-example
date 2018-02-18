from flask import Flask
from flask_prometheus import monitor

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

app.memory_load_str = ''
MB = 1024 * 1024

@app.route('/load/memory')
def memory_load():
    app.memory_load_str += 'a' * MB
    return 'Added 1MB memory'

@app.route('/load/cpu')
def cpu_load():
	for number in range(1000):
		cpu_load_simulation = number * number
	return 'Generated CPU load'

monitor(app, port=8000)
app.run(host='0.0.0.0')