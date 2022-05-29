from flask import Flask, jsonify, send_file
import json 
app = Flask(__name__)

@app.route("/")
def home(): 
    return send_file("db.json")

@app.route("/write/<name>,<time>")
def write(name, time): 
    with open("db.json",'r+') as file:
        entry = {'name': name, "time": float(time)}
        
        print("working")
        file_data = json.load(file)
        file_data.append(entry)
        file.seek(0)
        json.dump(file_data, file)

    return("done")


@app.route("/deleteserver")
def delete(): 
    with open("db.json",'w') as file:
        file_data = []

        json.dump(file_data, file)

    return("done")
