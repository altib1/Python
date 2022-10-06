import datetime
import Person 
import unicodedata

variable = str(input("Mot."))
variable1 = str(input("Date"))
mot = ''
date = ''
mots = []
dates = []

person = Person.Person(variable, datetime.date.today)

# Traitement pour mots
def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn')  


#for i in range(len(person.mots)):
#    mot = person.mots[i]
    
#for i in range(len(person.dates)):
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
 #   print(str(mots[i]))

# traitements pour dates 

dates.append(str(person.dates()))
dates.append(datetime.strptime(person.dates()).year())
dates.append(datetime.date(person.dates).month)
dates.append(datetime.date(person.dates).day)

for i in range(len(dates)):
    print(str(dates[i]))