from flask import Flask

app = Flask (__name__)

@app.route('/')
def home():
    return "Página Inicial"

@app.route('/paginaDois')
def dois():
    return "Essa é a página dois do site"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)