import sqlite3
from functools import wraps

from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret-key-change-later"


def get_db_connection():
    connection = sqlite3.connect("database/ecommerce.db")
    connection.row_factory = sqlite3.Row
    return connection


def login_required(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in first.")
            return redirect(url_for("login"))

        return route_function(*args, **kwargs)

    return wrapper


def role_required(allowed_roles):
    def decorator(route_function):
        @wraps(route_function)
        def wrapper(*args, **kwargs):
            if "user_id" not in session:
                flash("Please log in first.")
                return redirect(url_for("login"))

            if session.get("role") not in allowed_roles:
                return (
                    "<h1>Access Denied</h1>"
                    "<p>Your role does not have permission for this page.</p>"
                ), 403

            return route_function(*args, **kwargs)

        return wrapper

    return decorator


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        password_hash = generate_password_hash(password)

        connection = get_db_connection()

        try:
            connection.execute(
                "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                (username, password_hash, "buyer"),
            )

            connection.commit()
            connection.close()

            flash("Account created. Please log in.")
            return redirect(url_for("login"))

        except sqlite3.IntegrityError:
            connection.close()
            flash("That username is already taken.")
            return redirect(url_for("register"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        connection = get_db_connection()

        user = connection.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,),
        ).fetchone()

        connection.close()

        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            session["role"] = user["role"]

            flash("You are now logged in.")
            return redirect(url_for("home"))

        flash("Invalid username or password.")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for("home"))


@app.route("/products")
def products():
    connection = get_db_connection()

    products_list = connection.execute(
        """
        SELECT id, name, description, category, price, stock, image
        FROM products
        """
    ).fetchall()

    connection.close()

    return render_template("products.html", products=products_list)


@app.route("/checkout", methods=["GET", "POST"])
@role_required(["buyer"])
def checkout():
    if request.method == "POST":
        flash("Order placed successfully.")
        return redirect(url_for("checkout"))

    return render_template("checkout.html")


@app.route("/admin/system")
@role_required(["system_admin"])
def system_admin_dashboard():
    return """
    <h1>System Admin Dashboard</h1>
    <p>Only system administrators can access this page.</p>
    <p><a href="/">Back Home</a></p>
    """


@app.route("/admin/web")
@role_required(["web_admin"])
def web_admin_dashboard():
    return """
    <h1>Web Admin Dashboard</h1>
    <p>Only web administrators can access this page.</p>
    <p><a href="/">Back Home</a></p>
    """


@app.route("/merchant/dashboard")
@role_required(["merchant"])
def merchant_dashboard():
    return """
    <h1>Merchant Dashboard</h1>
    <p>Only merchants can access this page.</p>
    <p><a href="/">Back Home</a></p>
    """


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
        ssl_context=("certs/server.crt", "certs/server.key"),
    )
