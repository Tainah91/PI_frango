#mostrar os erros em tempo real
DEBUG = True
#usuário
USERNAME = 'root'
#senha
PASSWORD = 'root'
#servidor
SERVER = 'localhost'
#nome do banco de dados
DB = 'enemteste'
#connection string
SQLALCHEMY_DATABASE_URI=f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
#modificação
SQLALCHEMY_TRACK_MODIFICATIONS = True
#chave secreta - hash (chave criptografada)
#ebtrar em qualquer site que gere hash - colocar o hash
#publicar
SECRET_KEY ="minha-chave-secreta"

#português
BABEL_DEFAULT_LOCALE = 'pt'

