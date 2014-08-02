# Built-in
import logging

# config
from app.config import config

# Library
from app.shared.response import jsonified
from app.shared import error
from app.shared.Member import Member

# 3rd Party
from flask import Blueprint, request

logger = logging.getLogger(config.root_logger + __name__)

member_blueprint = Blueprint('member', __name__, url_prefix=config.api_prefix + "member")


@member_blueprint.route('/', methods=['GET'])
def show():
    try:
        return jsonified("members on the way")
    except:
        raise error.SystemError()


@member_blueprint.route('/', methods=["POST"])
def register():
    try:
        json_resp = request.get_json(force=True)
        password = json_resp.get("password")
        username = json_resp.get("username")
        email = json_resp.get("email")
        phone = json_resp.get("phone")

        member = Member(name=username, email=email, phone=phone, password=password)

    except:
        raise error.SystemError()

    try:
        return jsonified(data="registered user %s" % member)

    except:
        raise error.SystemError()

