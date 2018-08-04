from flask import Flask, redirect, render_template, session, request
import random

app=Flask(__name__)
app.secret_key = "dankmemesareneverdankenough"

@app.route("/")
def thedankness():
    if "gold" in session:
        pass

    else: 
        session['list']=[]
        session['gold']=0

    return render_template("index.html", **session)

@app.route("/process_money", methods=["post"])
def memedank():
    if request.form['building']=="farm":
        session['rng']=random.randrange(10, 21)
        session['gold']+=session['rng']
        session['list'].append("You earned:"+ str(session['rng']))

    if request.form['building']=="cave":
        session['rng']=random.randrange(5, 11)
        session['gold']+=session['rng']
        session['list'].append("You earned:"+ str(session['rng']))

    if request.form['building']=="house":
        session['rng']=random.randrange(2, 6)
        session['gold']+=session['rng']
        session['list'].append("You earned:"+ str(session['rng']))

    if request.form['building']=="casino":
        session['rng']=random.randrange(-50, 51)
        if session['rng']>0:
            session['gold']+=session['rng']
            session['list'].append("You earned:"+ str(session['rng']))

        elif session['rng']==0:
            session['gold']+=session['rng']
            session['list'].append("You came out even")

        elif session['rng']<0:
            temp=session['gold']
            temp+=session['rng']
            session['rng']=session['gold']-temp
            session['gold']=temp
            session['list'].append("You lost:"+ str(session['rng']))

    return redirect("/")

@app.route("/valid")
def dankmemes():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)