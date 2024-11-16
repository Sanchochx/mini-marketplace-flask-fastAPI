from flask import Flask, render_template, redirect
import requests

app = Flask(__name__)

API_URL = "http://127.0.0.1:8000"

@app.route("/")
def home():
    response = requests.get(f"{API_URL}/products")
    products = response.json()
    return render_template("home.html", products=products)

@app.route("/product/<int:product_id>")
def product_details(product_id):
    response = requests.get(f"{API_URL}/products/{product_id}")
    products = response.json()
    return render_template("product_details.html", product=products)

if __name__ == "__main__":
    app.run(debug=True, port=5000)