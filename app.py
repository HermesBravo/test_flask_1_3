from flask import Flask, request, jsonify

app = Flask(name)

@app.route("/init")
def main():
    return {"payload":"welcome to my project"}

@app.route('/read/:<content>', methods=['GET'])
def read_content(content):
    if content=="foo":
        return {"payload":content}
    else:
        return "Usuario No Existe"
    
@app.route('/create/:<content>', methods=['POST'])
def create_content(content):
    if content=="bar":
        return {"payload":content}
    else:
        return "Usuario No Existe"

@app.route('/delete/<content>', methods=['DELETE'])
def delete_content(content):
    if content == "qux":
        return {"payload": content}
    else:
        return "Usuario No Existe"

@app.route('/put/<content>', methods=['PUT'])
def put_content(content):
    if content == "echo":
        return {"payload": content}
    else:
        return "Usuario No Existe"

if name == "main":
    app.run(debug=True)
