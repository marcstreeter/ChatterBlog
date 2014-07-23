# Built-in
import logging

# Config
from app.config import config

# Library
from app.lib.response import jsonified
from app.lib import error

# 3rd Party
from flask import Blueprint

logger = logging.getLogger(config.root_logger + __name__)

status_blueprint = Blueprint('status', __name__, template_folder='templates', url_prefix=config.api_prefix + "status")

@status_blueprint.route('/', methods=["GET"])
def show():
    try:
        return jsonified("working")
    except:
        raise error.SystemErrors()