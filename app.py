from flask import Flask 
from flask_restful import Api 
from resources.hotel import Hoteis, Hotel
import os

diretorio_atual = os.path.abspath(os.path.dirname(__file__))
db_caminho = os.path.join(diretorio_atual, 'banco.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_caminho}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
api = Api(app)

configuracoes_carregadas = False

@app.before_request
def cria_banco():
    global configuracoes_carregadas
    if not configuracoes_carregadas:
        banco.create_all()
        configuracoes_carregadas = True

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)  