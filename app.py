from flask import Flask, jsonify, request
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
from flask_cors import CORS  # Importe o CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

    
api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})


hoteis = []
@app.route('/hoteis', methods=['GET', 'POST'])
def gerenciar_hoteis():
    if request.method == 'POST':
        # Lidar com a solicitação POST para criar um novo hotel
        novo_hotel = request.json  # Os dados do novo hotel são enviados como JSON

        # Adicione o novo hotel à lista de hotéis
        hoteis.append(novo_hotel)

        # Você pode retornar uma resposta de sucesso, se desejar
        return jsonify({"message": "Hotel adicionado com sucesso"}), 201

    elif request.method == 'GET':
        # Lidar com a solicitação GET para obter a lista de hotéis
        return jsonify({"hoteis": hoteis}), 200

if __name__ == '__main__':
    app.run(debug=True)