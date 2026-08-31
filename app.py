from flask import Flask

app = Flask(__name__)


# Rota raiz: usada para checagem simples de que a API está no ar
@app.route("/")
def status():
    return {"status": "API funcionando perfeitamente e disponível"}


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/tickets")
def tickets():
    return {
        "tickets": [
            {"id": 1, "titulo": "Erro ao logar", "status": "aberto"},
            {"id": 2, "titulo": "Lentidão no dashboard", "status": "em andamento"}
        ]
    }


@app.route("/sobre")
def sobre():
    return {
        "nome": "OpsTrack API",
        "versao": "1.0.0"
    }
