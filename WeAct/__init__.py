from flask import Flask, json, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from flask_restplus import Api,Resource,fields
from flask_bcrypt import Bcrypt
import config

db = SQLAlchemy()
migrate = Migrate()
base_url = '/'
#flask_restx와 SWagger
# @app.route()

def create_app():
    app = Flask(__name__)
    # api=Api(app,version='1.0',title='ClassesMVC API',description='A simple ClassesMVC API')

    # ns=api.namespace()
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    from . import views
    # name_space = api.namespace('classes', description='classes APIs')
    # classes=api.model('classes',{
    #
    # })

    @app.route(base_url+'/classes/list',methods=['GET'])
    def getClassesList():
        return 'test'

    # def getClassesList():
    #     params = {
    #         "param1": "test1",
    #         "param2": 123,
    #         "param3": "한글"
    #     }
    #     return 'test'
    @app.route(base_url + '/classes/', methods=['POST'])
    def handle_post():
        params = json.loads(request.get_data(), encoding='utf-8')
        if len(params) == 0:
            return 'No parameter'

        params_str = ''
        for key in params.keys():
            params_str += 'key: {}, value: {}<br>'.format(key, params[key])
        return params_str

    app.register_blueprint(views.bp)

    return app
