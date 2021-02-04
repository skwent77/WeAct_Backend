from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

app=Flask(__name__)
app.config.from_object(config)

#ORM
db.init_app(app)
migrate.init_app(app,db)

from . import models
