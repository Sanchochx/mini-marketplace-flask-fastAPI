from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

products_db = [
    {
        "id": 1,
        "name": "Acer Nitro v15",
        "price": 850,
        "stock": 55,
        "description": "Un buen pc portatil para mocharla en Dota.",
        "image_url": "/static/img/acernitrov15.jpg",
    },
    {
        "id": 2,
        "name": "OnePlus 12",
        "price": 760,
        "stock": 20,
        "description": "El mismo celular que tiene rasta.",
        "image_url": "/static/img/oneplus12.jpg"
    },
    {
        "id": 3,
        "name": "KickBoxing Gloves",
        "price": 44.44,
        "stock": 10,
        "description": "Los mejores guantes de kickboxing para entrenar.",
        "image_url": "/static/img/kickboxingloves.jpg"
    },
    {
        "id": 4,
        "name": "Mouse HyperX",
        "price": 139.99,
        "stock": 15,
        "description": "El propio mouse para el rampage en Dota.",
        "image_url": "/static/img/hyperxmouse.jpg"
    },
    {
        "id": 5,
        "name": "Gundam Evangelion",
        "price": 120,
        "stock": 5,
        "description": "Very cool gundam.",
        "image_url": "/static/img/gundamevangelion.jpg"
    }
]

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    description: str
    image_url: str

@app.get("/products", response_model=List[Product])
def get_products():
    return [Product(**product) for product in products_db]

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = next((item for item in products_db if item["id"] == product_id), None)
    if product is None:
        return {"message": "Producto no encontrado"}
    return Product(**product)

