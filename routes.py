# import os
# print(os.path.abspath(os.path.dirname(os.getcwd()+"/passagens_aereas")))

from flask import Blueprint, Flask, Response, json, jsonify, request
from flask.helpers import make_response

from controllers import *

url_blueprint = Blueprint("urls", __name__)

############################# Aeroporto #############################
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

@url_blueprint.route("/aeroporto/<id>", methods=["DELETE"])
def remove_aeroporto(id):
    res = hw_remove_aeroporto(id)
    return make_response(jsonify(res))

@url_blueprint.route("/aeroporto", methods=["PUT"])
def update_aeroporto():
    data = request.get_json()
    res = hw_update_aeroporto(data)
    return make_response(jsonify(res))

############################# VOO #############################
@url_blueprint.route("/voo", methods=["POST"])
def add_voo():
    data = request.get_json()
    res = hw_add_voo(data)
    return make_response(jsonify(res))

@url_blueprint.route("/voo", methods=["GET"])
def list_voos():
    res = hw_get_voos()
    return make_response(jsonify(res))

@url_blueprint.route("/voo/<id>", methods=["GET"])
def get_voo(id):
    res = hw_get_voo(id)
    return make_response(jsonify(res))

@url_blueprint.route("/voos", methods=["GET"])
def get_voo_aeroporto():
    res = hw_get_voos_aeroportos()
    return make_response(jsonify(res))

@url_blueprint.route("/voo/<id>", methods=["DELETE"])
def remove_voo(id):
    res = hw_remove_voo(id)
    return make_response(jsonify(res))

@url_blueprint.route("/voo", methods=["PUT"])
def update_voo():
    data = request.get_json()
    res = hw_update_voo(data)
    return make_response(jsonify(res))

#4
@url_blueprint.route("/voo/<companhia>", methods=["GET"])
def get_aeroporto_by_company(companhia):
    print(companhia)
    print("BANANANANANA")
    res = hw_get_aeroporto_by_company(companhia)
    return make_response(jsonify(res))
    
#7
@url_blueprint.route("/pesquisavoos/<num>", methods=["GET"])
def pesquisa_voos(num):
    res = hw_search_voos(num)
    return make_response(jsonify(res))

#5
@url_blueprint.route("/aeroporto/destinos", methods=["POST"])
def get_aeroportos_destino():
    data = request.get_json()
    res = hw_get_aeroportos_destino(data['origem'])
    return make_response(jsonify(res))


#6
@url_blueprint.route("/retornavoos", methods=["POST"])
def get_voos():
    date = day + "/" + month + '/' + year
    print(date, company)
    res = hw_list_voos(date, company)
    return make_response(jsonify(res))
