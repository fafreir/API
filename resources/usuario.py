from flask_restful import Resource, reqparse
from blocklist import BLOCKLIST
from models.usuario import UserModel
from flask_jwt_extended import create_access_token, get_jwt, jwt_required
import hmac

    
atributos = reqparse.RequestParser()
atributos.add_argument('login', type=str, required=True, help="The field 'login' cannot be left blank")
atributos.add_argument('senha', type=str, required=True, help="The field 'senha' cannot be left blank")

class User(Resource):
  
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {"message": "User not found."}, 404

    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            try:
                user.delete_user()
            except:
                return {'message':"An internal error ocurred trying to delete user"}, 500
            return {'message': 'User deleted.'}
        return {'message':'User not found'}, 404
    
class UserRegister(Resource):
    def post(self):
        
        dados = atributos.parse_args()
        if UserModel.find_by_login(dados['login']):
            return {'message':"The login '{}' already exists".format(dados['login'])}
        # user = UserModel(dados['login'], dados['senha'])
        user = UserModel(**dados)
        user.save_user()
        return {'message':'User create sucessfully'}, 201

class UserLogin(Resource):

    @classmethod
    def post(cls):
        dados = atributos.parse_args()
        user = UserModel.find_by_login(dados['login'])
        # if user and safe_str_cmp(user.senha, dados['senha'])
        if user and hmac.compare_digest(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=str(user.user_id))
            return {'access_token':token_de_acesso}, 200
        return {'message':'The username or password is incorrect.'}, 401
    
class UserLogout(Resource):

    @jwt_required()
    def post(self):
        """Ao realizar logout, pega o id do Token """
        jti_id = get_jwt()['jti'] # JWT Token Identifier
        """ Adiciona o Token na BLOCKLIST """
        BLOCKLIST.add(jti_id)
        return {'message':'Logged out sucessfully!'}, 200