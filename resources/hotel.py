from flask_restful import Resource, reqparse

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
    },
    {
        'hotel_id': 'bravo',
        'nome': 'Bravo Hotel',
        'estrelas': 4.4,
        'diaria': 380.90,
        'cidade': 'Santa Catarina'
    },
    {
        'hotel_id': 'charlie',
        'nome': 'Charlie Hotel',
        'estrelas': 3.9,
        'diaria': 320.20,
        'cidade': 'Curitiba'
    }
]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}
    
class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'Hotel not found.'}, 404

    def post(self, hotel_id):
        """Recebe os elementos da requisição e habilita o parseamento"""
        argumentos = reqparse.RequestParser()

        """Irá pegar os argumentos especificos"""
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')

        """Irá instanciar e parsear com chave e valor"""
        dados = argumentos.parse_args()

        """Será criado um novo_hotel, iremos acessar através da instancia dados"""
        novo_hotel = {
            'hotel_id': hotel_id,
            'nome': dados['nome'],
            'estrelas': dados['estrelas'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade']
        }

        """Adiciona na lista hoteis o novo hotel"""
        hoteis.append(novo_hotel)
        
        """Retornar o novo hotel com o status code de sucesso 200"""
        return novo_hotel, 200

    def put(self, hotel_id):
        pass 

    def delete(self, hotel_id):
        pass 