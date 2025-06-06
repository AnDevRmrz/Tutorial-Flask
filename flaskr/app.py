from ___init__ import create_app
from modelos.modelos import db
from flask_restful import Api
from vistas.vistas import VistaCanciones, VistaCancion, VistaAlbumsUsuario, VistaAlbum, VistaCancionesAlbum, VistaSignIn, VistaLogIn
from flask_jwt_extended import JWTManager
from flask_cors import CORS


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)

api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/cancion/<int:id_cancion>')
api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaLogIn, '/login')
api.add_resource(VistaAlbumsUsuario, '/usuario/<int:id_usuario>/albumes')
api.add_resource(VistaAlbum, '/album/<int:id_album>')
api.add_resource(VistaCancionesAlbum, '/album/<int:id_album>/canciones')

jwt = JWTManager(app)