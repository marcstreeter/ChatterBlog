# Built-in
import logging

# 3rd Party
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Config
from app.config import config

# Module
## Blueprints
from member import member_blueprint
from status import status_blueprint
## Library
from app.shared import error
from app.shared.response import jsonified

logger = logging.getLogger(config.root_logger[:-1])  # root logger mustn't have the trailing '.'

app = Flask(__name__)
app.config.from_object('app.config.config')

#Register DB
db = SQLAlchemy(app)

# Register Blueprints
app.register_blueprint(member_blueprint)
app.register_blueprint(status_blueprint)

# Error Handlers
@app.errorhandler(error.InvalidUsageError)
def handle_invalid_usage(error):
    return jsonified(error)

@app.errorhandler(error.SystemError)
def handle_system(error):
    return jsonified(error)

@app.errorhandler(error.UnauthenticatedError)
def handle_unauthenticated(error):
    return jsonified(error)