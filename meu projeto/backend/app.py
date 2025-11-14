from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # permite acesso do frontend

notas = {
    "nicole": "",
    "marcelo": "",
    "juan": ""
}

@app.get("/notas")
def get_notas():
    return jsonify(notas)

@app.post("/notas")
def post_notas():
    data = request.json
    usuario = data.get("usuario")
    texto = data.get("texto")
    if usuario in notas:
        notas[usuario] = texto
    return jsonify(notas)

@app.get("/")
def home():
    return "Backend funcionando!"

# Apenas local, mas o Render ignora isso (bom!)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
