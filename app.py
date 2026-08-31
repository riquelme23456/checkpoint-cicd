import os
from flask import Flask, jsonify

app = Flask(__name__)

# --- ROTAS ---

@app.route("/", methods=["GET"])
def status():
    """Rota de Health Check (Checagem de Saúde)"""
    return jsonify({"status": "operacional e no ar"}), 200


@app.route("/tickets", methods=["GET"])
def get_tickets():
    """Retorna a lista de tickets"""
    # Em produção, esses dados viriam de um Banco de Dados ou Service Layer
    lista_tickets = [
        {"id": 1, "titulo": "Erro ao logar", "status": "aberto"},
        {"id": 2, "titulo": "Lentidão no dashboard", "status": "em andamento"}
    ]
    return jsonify({"tickets": lista_tickets}), 200


@app.route("/sobre", methods=["GET"])
def sobre():
    """Informações gerais sobre a API"""
    return jsonify({
        "nome": "OpsTrack API",
        "versao": "1.0.0"
    }), 200


# --- PONTO DE ENTRADA ---
if __name__ == "__main__":
    # Carrega a flag de debug via variável de ambiente (padrão: False para segurança)
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() in ("true", "1", "t")
    
    # app.run é recomendado APENAS para desenvolvimento local.
    # Em produção, utilize um servidor WSGI/ASGI como Gunicorn ou Waitress.
    # teste
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)