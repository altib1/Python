from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
     # Read the JSON data from the file
    with open('output.json', 'r') as file:
        json_data = file.read()

    # Convert the JSON data to a Python dictionary
    data = json.loads(json_data)

    # Render the template with the data
    return render_template('index.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'word': request.form['word'],
        'date': request.form['date']
    }
    with open('main.json', 'a') as file:
        json.dump(data, file)
        file.write('\n')
    return 'Data submitted successfully!'

@app.route('/json_data')
def json_data():
    # Read the JSON data from the file
    with open('output.json', 'r') as f:
        json_data = f.read()
    if json_data:
        data = json.loads(json_data)
    else:
        data = {}

    # Convert the JSON data to a Python dictionary
    data = json.loads(json_data)

    # Return the JSON data as a response
    return jsonify(data)


if __name__ == '__main__':
    app.run()