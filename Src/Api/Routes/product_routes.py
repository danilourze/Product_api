from flask import Blueprint, request, jsonify
from Src.Api.Services.product_service import (
    create_product,
    update_product,
    delete_product,
    patch_product, list_products
)
from Src.Api.Middlewares.auth_middleware import token_required

product_bp = Blueprint("products", __name__)


@product_bp.route("/products", methods=["POST"])
@token_required
def create():
    data = request.json
    create_product(data)
    return jsonify({"message": "Product queued for creation"}), 202


@product_bp.route("/products/<int:product_id>", methods=["PUT"])
@token_required
def update(product_id):
    data = request.json
    update_product(product_id, data)
    return jsonify({"message": "Product queued for update"}), 202


@product_bp.route("/products/<int:product_id>", methods=["DELETE"])
@token_required
def delete(product_id):
    delete_product(product_id)
    return jsonify({"message": "Product queued for deletion"}), 202


@product_bp.route("/products/<int:product_id>", methods=["PATCH"])
@token_required
def patch(product_id):
    data = request.json
    patch_product(product_id, data)
    return jsonify({"message": "Product queued for patch update"}), 202


@product_bp.route("/products", methods=["GET"])
@token_required
def get_products():

    products = list_products()

    return jsonify(products), 200