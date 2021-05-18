# import os
# print(os.path.abspath(os.path.dirname(os.getcwd()+"/passagens_aereas")))

from flask import Blueprint, Flask, Response, json, jsonify, request
from flask.helpers import make_response

from controllers import *

url_blueprint = Blueprint("urls", __name__)


@url_blueprint.route("/aeroporto", methods=["POST"])
def add_person():
    data = request.get_json()
    res = hw_add_aeroporto(data)
    return make_response(jsonify(res))

@url_blueprint.route("/aeroporto", methods=["GET"])
def get_aeroportos():
    res = hw_get_aeroportos()
    return make_response(jsonify(res))

@url_blueprint.route("/aeroporto/<id>", methods=["GET"])
def get_aeroporto(id):
    res = hw_get_aeroporto(id)
    return make_response(jsonify(res))

@url_blueprint.route("/aeroporto/<day>/<month>/<company>", methods=["GET"])
def get_voos(day, month, company):
    date = day + "/" + month
    res = hw_list_voos(date, company)
    return make_response(jsonify(res))

@url_blueprint.route("/aeroporto/<id>", methods=["DELETE"])
def remove_aeroporto(id):
    res = hw_remove_aeroporto(id)
    return make_response(jsonify(res))

@url_blueprint.route("/aeroporto", methods=["PUT"])
def update_aeroporto():
    data = request.get_json()
    res = hw_update_aeroporto(data)
    return make_response(jsonify(res))