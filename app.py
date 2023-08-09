#feature/bravo
from flask import Flask, request, jsonify

#feature/alfa
@app.route("/init")
def main():
    return {"payload":"welcome to my project "}

app = Flask(name)

@app.route("/init/:<content>', methods=['GET']")
def main(content):
    if content=="alfa":
        return {"payload":content}
    else:
        return "Usuario No Existe"

 #develop
@app.route('/read/:<content>', methods=['GET'])
def read_content(content):
    if content=="foo":
        return {"payload":content}
    else:
        return "Usuario No Existe"
    
 #feature/alfa
@app.route('/create/:<content>', methods=['GET'])

@app.route('/create/:<content>', methods=['POST'])
 develop
def create_content(content):
    if content=="bar":
        return {"payload":content}
    else:
        return "Usuario No Existe"

@app.route('/delete/:<content>', methods=['DELETE'])
def delete_content(content):
    if content == "qux":
        return {"payload": content}
    else:
        return "Usuario No Existe"

@app.route('/put/:<content>', methods=['PUT'])
def put_content(content):
    if content == "echo":
        return {"payload": content}
    else:
        return "Usuario No Existe"

if name == "main":
    app.run(debug=True)

develop
