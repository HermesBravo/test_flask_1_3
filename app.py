from flask import Flask, request
app = Flask(__name__)

@app.route("/init")
def main():
    return {"payload":"welcome to my project "}

@app.route('/read/:<content>', methods=['GET'])
def read_content(content):
    if content=="foo":
        return {"payload":content}
    else:
        return "Usuario No Existe"
    
@app.route('/create/:<content>', methods=['GET'])
def create_content(content):
    if content=="bar":
        return {"payload":content}
    else:
        return "Usuario No Existe"

if __name__ == "__main__":
    app.run(debug=True)
