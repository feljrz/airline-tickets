# import os
# print(os.path.abspath(os.path.dirname(os.getcwd()+"/passagens_aereas")))

from flask import Blueprint, Flask, Response, json, jsonify, request
from flask.helpers import make_response
from flask_login import LoginManager, login_required

from controllers import *

url_blueprint = Blueprint("urls", __name__)

login_manager = LoginManager()

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


# 4
@url_blueprint.route("/voo/companhia", methods=["POST"])
def get_aeroporto_by_company():
    data = request.get_json()
    res = hw_get_aeroporto_by_company(data["companhia"])
    return make_response(jsonify(res))


# 5
@url_blueprint.route("/aeroporto/destinos", methods=["POST"])
def get_aeroportos_destino():
    data = request.get_json()
    res = hw_get_aeroportos_destino(data["origem"])
    return make_response(jsonify(res))


# 6
@url_blueprint.route("/voo/data", methods=["POST"])
def get_voos():
    data = request.get_json()
    # date = day + "/" + month + '/' + year
    # print(date, company)
    res = hw_get_voos_companhia(data)
    return make_response(jsonify(res))


# 7
@url_blueprint.route("/voo/passageiros/<num>", methods=["GET"])
def get_voos_passageiros(num):
    res = hw_get_voos_passageiros(num)
    return make_response(jsonify(res))


###########################  Login  #####################


@login_manager.user_loader
def load_user(user_id):
    return hw_load_user(user_id)


@url_blueprint.route("/cadastro", methods=["GET"])
def get_cadastro():
    res = hw_get_cadastros()
    return make_response(jsonify(res))


@url_blueprint.route("/cadastro", methods=["POST"])
def add_cadastro():
    data = request.get_json()
    res = hw_add_cadastro(data)
    return make_response(jsonify(res))


@url_blueprint.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    res = hw_login(data)
    return make_response(jsonify(res))


@url_blueprint.route("/logout", methods=["GET"])
@login_required
def logout():
    res = hw_logout()
    return make_response(jsonify(res))


###########################  Reserva  #####################


@url_blueprint.route("/reserva", methods=["POST"])
def add_reserva():
    data = request.get_json()
    res = hw_add_reserva(data)
    return make_response(jsonify(res))


@url_blueprint.route("/reserva", methods=["GET"])
def get_reservas():
    res = hw_get_reservas()
    return make_response(jsonify(res))


@url_blueprint.route("/reserva/<id>", methods=["GET"])
def get_reserva(id):
    res = hw_get_reserva(id)
    return make_response(jsonify(res))
