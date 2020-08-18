import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import uuid 
app = Flask(__name__)

client = MongoClient('mongodb://root:coba@db-mongo:27017/')
db = client.tododb


@app.route('/',methods=['POST','GET'])
def todo():
    if request.method=="POST":
        id = uuid.uuid1()
        item_doc = {
        'uuid': id.hex,
        'tanggal': request.form['tanggal'],
        'keterangan': request.form['keterangan']
        }
        print(item_doc)
        db.tododb.insert_one(item_doc)
    _items = db.tododb.find()
    items = [item for item in _items]

    return render_template('todo.html', items=items)


@app.route('/update', methods=['POST'])
def update():
    where = {
        "uuid": request.form["idnya"]
    }
    item_doc = {
        "tanggal": request.form["tanggal"],
        "keterangan": request.form["keterangan"]
    }
    db.tododb.update_one(where, {"$set":item_doc})
    print(where, {"$set":item_doc})
    return redirect(url_for('todo'))

@app.route('/hapus/<string:id_data>', methods=['POST','GET'])
def hapus(id_data):
    where = {
        "uuid": id_data
    }
    db.tododb.delete_one(where)
    # print(where, {"$set":item_doc})
    return redirect(url_for('todo'))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000,debug=True)