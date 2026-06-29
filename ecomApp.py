from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret-key-change-later"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/products")
def products():
    sample_products = [
        {"id": 1, "name": "Laptop Stand", "price": 29.99},
        {"id": 2, "name": "Wireless Mouse", "price": 19.99},
        {"id": 3, "name": "USB-C Cable", "price": 9.99},
    ]
    return render_template("products.html", products=sample_products)

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

if __name__ == "__main__":
    app.run(debug=True)