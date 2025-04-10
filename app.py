from flask import Flask 
from flask_restful import Api 
from resources.hotel import Hoteis, Hotel
from resources.usuario import User
import os

diretorio_atual = os.path.abspath(os.path.dirname(__file__))
db_caminho = os.path.join(diretorio_atual, 'banco.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_caminho}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
api = Api(app)


@app.before_request
def cria_banco():
    banco.create_all()
       

api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(User, '/usuarios/<int:user_id>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)  