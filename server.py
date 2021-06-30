from flask import Flask, render_template
from hackat import *
app = Flask(__name__)
Cardlist = []
#Turno 1
Red_Ninja = Creature("Red Ninja" , 3, 3, 4, 1)
Cardlist.append(Red_Ninja)
# turno 2
Hard_Alg = Spell("Hard Algorithm", 2, "hp", 3, 1)
Hard_Alg.PlaySpell(Red_Ninja)

Cardlist.append(Hard_Alg)


Black_Ninja = Creature("Black Ninja", 4, 5, 4 , 2)
FailedPromise = Spell("Failed Promise", 1, "hp", -2 , 2)
FailedPromise.PlaySpell(Red_Ninja)

Cardlist.append(Black_Ninja)
Cardlist.append(FailedPromise)

PartnerProgramming = Spell("PartnerProgramming", 3, "power", 2, 1)
PartnerProgramming.PlaySpell(Red_Ninja)

Cardlist.append(PartnerProgramming)

Red_Ninja.Attack(Black_Ninja)


Cardshow = []
app.cont = 0

@app.route("/")
def hello_world():
    
    if app.cont == len(Cardlist):
        app.cont -= 1
    else:
        Cardshow.append(Cardlist[app.cont])
    app.cont += 1
    

    return render_template('index.html', Cardlist=Cardshow)


app.run(debug=True)
