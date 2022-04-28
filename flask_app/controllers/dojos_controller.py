from flask import render_template, request, redirect, session
from flask_app.models.dojo import Dojo
from flask_app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    if not Dojo.validate_form(request.form):
        return redirect('/')
    data = {
        "name": request.form['name'],
        "location": request.form['dojo_location'],
        "language": request.form['favorite_language'],
        "comment": request.form['comment']
    }
    id = Dojo.save(data)
    return redirect(f'/results/{id}')

@app.route('/results/<int:id>')
def show(id):
    dojo = Dojo.get_one(id)
    return render_template("results.html", dojo=dojo)

@app.route('/go-back')
def clear():
    session.clear()
    return redirect('/')

