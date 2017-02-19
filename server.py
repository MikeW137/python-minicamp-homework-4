from flask import Flask, render_template, request, jsonify
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/movie', methods = ['POST'])
def addmovie():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        name = request.form['name']
        releaseYear = request.form['releaseYear']
        director = request.form['director']
        actor = request.form['actor']
        cursor.execute('INSERT INTO movies (name, releaseYear, director, actor) VALUES(?,?,?,?)', (name,releaseYear, director, actor))
        connection.commit()
        message = 'Record successfully added'

    except:
        connection.rollback()
        message = 'error in insert operation'

    finally:
        return render_template('result.html', message = message)
        connection.close()

@app.route('/movies')
def movies():
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM movies')
        data = cursor.fetchall()
    finally:
        connection.close()
        return jsonify(data)


@app.route('/search', methods = ['GET'])
def search():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    name = request.args.get('name')
    try:
       cursor.execute('SELECT * FROM movies WHERE name=?', (name,))
       data = cursor.fetchall()
    finally:
        return jsonify(data)
        connection.close()


app.run(debug = True)
