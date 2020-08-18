import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://root:coba@db-mongo:27017/')
db = client.tododb


@app.route('/',methods=['POST','GET'])
def todo():
    if request.method=="POST":
        item_doc = {
        'tanggal': request.form['tanggal'],
        'keterangan': request.form['keterangan']
        }
        print(item_doc)
        db.tododb.insert_one(item_doc)
    _items = db.tododb.find()
    items = [item for item in _items]

    return render_template('todo.html', items=items)


@app.route('/new', methods=['POST'])
def new():

    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    db.tododb.insert_one(item_doc)

    return redirect(url_for('todo'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000,debug=True)