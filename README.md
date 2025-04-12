### REST APIs com Python e Flask
É um curso da Udemy, ministrado pelo professor [Danilo Moreira](https://www.linkedin.com/in/odanilomoreira/).

Para saber mais sobre o curso [link do curso](https://www.udemy.com/course/rest-apis-com-python-e-flask/)  <br/> <br/>

#### Tecnologias utilizadas
Estão sendo utilizadas as seguintes tecnologias (em atualização, conforme utilização):
- Python
- Flask
- Flask-Restful
- sqlite3
- Flask-SQLAlchemy
- flask_jwt_extended  <br/> <br/>

#### Instalação de pacotes utilizados:
- Para instalar as bibliotecas, só utilizar o comando abaixo: <br>
<code>pip install -r requirements.txt</code>  <br/> <br/>

#### Bibliotecas e funções deprecated (Obsoleta)
Quando instalamos o Flask, vem junto algumas dependências como o werkzeug.
Assim como o Flask, essas dependencias, também com o tempo podem ficar obsoletas ou deprecated.

[Mudanças no Werkzeug](https://werkzeug.palletsprojects.com/en/stable/changes/)
- safe_str_cmp: Na versão do werkzeug, foi removida na versão 2.1.0. A orientação é utilizar hmac ou hashlib. Nesse caso, iremos utilizar o hmac.

[Mudanças no Flask](https://flask.palletsprojects.com/en/stable/changes/)
- before_first_request: Essa anotação foi removida na versão 2.3.0, uma alternativa é a utilização da anotação @app.before_request
