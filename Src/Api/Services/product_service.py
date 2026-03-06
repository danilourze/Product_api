from Src.Api.Database import db
from Src.Api.Model.product import Product
from Src.Api.Queue.redis_queue import enqueue_product_operation


def create_product(data):
    enqueue_product_operation("create", data)


def update_product(product_id, data):
    payload = {"id": product_id, **data}
    enqueue_product_operation("update", payload)


def delete_product(product_id):
    enqueue_product_operation("delete", {"id": product_id})


def patch_product(product_id, data):
    payload = {"id": product_id, **data}
    enqueue_product_operation("patch", payload)


def list_products():

    products = db.session.query(Product).all()

    return [
        {
            "id": p.id,
            "name": p.name,
            "brand": p.brand,
            "price": p.price
        }
        for p in products
    ]