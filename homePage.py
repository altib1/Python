import json
from flask import Flask, jsonify, render_template, request
import datetime
import Person 
import unicodedata

app = Flask(__name__)

@app.route('/')
def index(data={}):
    return render_template('index.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    word = data['word']
    date = data['date']
    result = main(word, date)
    return jsonify(result)

def main(word, date):

    variable = str(word)
    variable1 = str(date)
    mot = ''
    date = ''
    mots = []
    dates = []
    
    person = Person.Person(variable, variable1)
    
    # Traitement pour mots
    def strip_accents(s):
        return ''.join(c for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn')  
    
    
    for i in range(len(person.mots)):
        mot = person.mots[i]
        
    # for i in range(len(person.dates)):
    #    date = person.dates[i]
    
    mots.append(person.mots)
    
    for i in range(len(mots)):
        mots.append(strip_accents(mots[i]))
        mots.append(strip_accents(mots[i]).capitalize())
        mots.append(strip_accents(mots[i]).upper())
        mots.append(strip_accents(mots[i]).lower())
    
    mots.append(person.mots.upper())
    mots.append(person.mots.capitalize())
    mots.append(person.mots.lower())
    
    leet = {'a':'4','e':'3','i':'1','o':'0','A':'4','E':'3','I':'1','O':'0'}
    for i in range(len(mots)):
        for lettre in mots[i] :
            for key in leet:
                if lettre == key:
                    count = mots[i].count(lettre)
                    for j in range(count):
                        mots.append(mots[i].replace(lettre, leet[key], j)) 
                    mots.append(mots[i].replace(lettre, leet[key])) 
                    mots[i] = mots[i].replace(lettre, leet[key])    
            mots.append(mots[i])                         
    
    mots = list(dict.fromkeys(mots)); 
    
    #for i in range(len(mots)):
    #    print(str(mots[i]))
    
    # traitements pour dates 
    #print(str(person.dates()))
    
    dates.append(str(person.day()))
    dates.append(str(person.month()))
    dates.append(str(person.year()))
    dates.append(str(person.day()) + str(person.month()) + str(person.year()))
    dates.append(str(person.year()) + str(person.month()) + str(person.day()))
    data = {
        'Results': []
    };
    for i in range(len(dates)):
        for y in range(len(mots)):
            data['Results'].append(mots[y]+dates[i])
            data['Results'].append(dates[i]+mots[y])
    return data