# import os
# print(os.path.abspath(os.path.dirname(os.getcwd()+"/passagens_aereas")))

from flask import Flask, Blueprint, Response, jsonify, json, request
from flask.helpers import make_response
from controllers import *


url_blueprint = Blueprint("urls", __name__)

@url_blueprint.route("/aeroporto", methods=["POST", "GET"])
def add_person():
    data = request.get_json()
    res = hw_add_aeroporto(data)
    return make_response(jsonify(res))

