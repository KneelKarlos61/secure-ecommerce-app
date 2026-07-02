import sqlite3
from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret-key-change-later"
def get_db_connection():
    connection = sqlite3.connect("database/ecommerce.db")
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/products")
def products():
    connection = get_db_connection()

    products = connection.execute("""
        SELECT id, name, description, category, price, stock, image
        FROM products
    """).fetchall()

    connection.close()

    return render_template("products.html", products=products)

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

if __name__ == "__main__":
    app.run(debug=True)