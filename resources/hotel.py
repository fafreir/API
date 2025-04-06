from flask_restful import Resource, reqparse

hoteis = [
    {
        "hotel_id": "alpha",
        "nome": "Alpha Hotel",
        "estrelas": 4.3,
        "diaria": 420.34,
        "cidade": "Rio de Janeiro"
    },
    {
        "hotel_id": "bravo",
        "nome": "Bravo Hotel",
        "estrelas": 4.4,
        "diaria": 380.90,
        "cidade": "Santa Catarina"
    },
    {
        "hotel_id": "charlie",
        "nome": "Charlie Hotel",
        "estrelas": 3.9,
        "diaria": 320.20,
        "cidade": "Curitiba"
    }
]

class Hoteis(Resource):
    def get(self):
        return {"hoteis": hoteis}
    
class Hotel(Resource):
    
    """Recebe os elementos da requisição e habilita o parseamento"""
    argumentos = reqparse.RequestParser()

    """Irá pegar os argumentos especificos"""
    argumentos.add_argument("nome")
    argumentos.add_argument("estrelas")
    argumentos.add_argument("diaria")
    argumentos.add_argument("cidade")
    
    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel["hotel_id"] == hotel_id:
                return hotel
        return None 
    
    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {"message": "Hotel not found."}, 404

    def post(self, hotel_id):
        
        """Irá instanciar e parsear com chave e valor"""
        dados = Hotel.argumentos.parse_args()

        """Vai desempacotar os dados"""
        novo_hotel = {'hotel_id': hotel_id, **dados}

        """Adiciona na lista hoteis o novo hotel"""
        hoteis.append(novo_hotel)
        
        """Retornar o novo hotel com o status code de sucesso 200"""
        return novo_hotel, 200

    def put(self, hotel_id):
        """Pega os dados e irá parsear em chave e valor"""
        dados = Hotel.argumentos.parse_args()

        """Vai desempacotar os dados"""
        novo_hotel = {'hotel_id': hotel_id, **dados}

        """Se o hotel existe, irá atualizar e retornar com status code de sucesso"""
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200

        """Caso não exista, irá inserir na lista de hoteis, retornar o novo hotel/
        com status code 201, que é de created
        """
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        pass 