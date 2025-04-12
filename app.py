from flask import Flask, jsonify 
from flask_restful import Api 
from blocklist import BLOCKLIST
from resources.hotel import Hoteis, Hotel
from resources.usuario import User, UserRegister, UserLogin, UserLogout
from flask_jwt_extended import JWTManager
import os

diretorio_atual = os.path.abspath(os.path.dirname(__file__))
db_caminho = os.path.join(diretorio_atual, 'banco.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_caminho}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config["JWT_SECRET_KEY"] = "super-secret-key" 
app.config["JWT_BLOCKLIST_ENABLED"] = True  # Ativa o BLOCKLIST
api = Api(app)
jwt = JWTManager(app)

 
@app.before_request
def cria_banco():
    banco.create_all()

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(self, token):
    return token["jti"] in BLOCKLIST


@jwt.revoked_token_loader
def revoked_token_callback():
    return  jsonify(
            {"description": "The token has been revoked.", "error": "token_revoked"}
        ), 401



       
api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')
api.add_resource(User, '/usuarios/<int:user_id>')
api.add_resource(UserRegister, '/cadastro')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)  