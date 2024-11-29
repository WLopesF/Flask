from flask import Flask

app = Flask(__name__)

@app.route('/<nome>')

app.run(host="0.0.0.0")

def saudacao(nome):
    return f"Olá, seu nome é {nome}!"
    
if __name__ == "__main__":
    app.run()