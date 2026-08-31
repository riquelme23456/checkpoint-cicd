from flask import Flask

app = Flask(__name__)


# Rota raiz: usada para checagem simples de que a API está no ar
@app.route("/")
def status():
    return {"status": "API online"}


if __name__ == "__main__":
    app.run(debug=True)
