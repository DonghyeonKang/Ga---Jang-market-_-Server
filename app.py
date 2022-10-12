from flask import Flask # Flask start 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "1"

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True, threaded=True)