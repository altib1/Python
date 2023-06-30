from flask import Flask, jsonify, render_template, request
from datetime import datetime
from engine import Engine

app = Flask(__name__)

@app.route('/')
def index(data={}):
    return render_template('index.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    words = data['words']
    dates = data['dates']

    result = process_input(words, dates)
    return jsonify(result)

def process_input(words, dates):
    results = []

    options = {
        "leet_min": True,
        "leet_maj": True,
        "special_char": True,
        "uppercase": True,
        "lowercase": True,
        "Capitalize": True,
        "special_char_level": "common",
        "special_char_max": 5,
    }

    engine = Engine(words, options)

    # Combine variations with dates
    for date in dates:
        for word_list in engine.array_possibilities:
            for word in word_list:
                results.append(word + date)
                results.append(date + word)

    return {'Results': results}

if __name__ == '__main__':
    app.run(debug=True)

