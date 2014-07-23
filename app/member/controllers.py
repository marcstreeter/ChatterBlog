# Built-in
import logging

# config
from app.config import config

# Library
from app.lib.response import jsonified
from app.lib import error

# 3rd Party
from flask import Blueprint, jsonify

logger = logging.getLogger(config.root_logger + __name__)

member_blueprint = Blueprint('member', __name__, url_prefix=config.api_prefix + "member")

@member_blueprint.route('/', methods=['GET'])
def show():
    try:
        return jsonified("members on the way")
    except:
        raise error.SystemError()