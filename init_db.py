import sqlite3

connection = sqlite3.connect("database/ecommerce.db")
cursor = connection.cursor()

cursor.execute("""
DROP TABLE IF EXISTS products
""")

cursor.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL,
    image TEXT
)
""")

products = [
    (
        "USB Security Key",
        "A physical login key used for multi-factor authentication.",
        "Authentication",
        34.99,
        15,
        "securityKey.jpg"
    ),
    (
        "Privacy Screen Filter",
        "A laptop screen cover that helps prevent shoulder surfing in public places.",
        "Privacy",
        24.99,
        20,
        "privacyScreen.jpg"
    ),
    (
        "Ethernet Cable 10 Feet Long",
        "A 10' Ethernet cable for networking labs, routers, and switches.",
        "Networking",
        7.99,
        30,
        "ethernet.jpg"
    ),
    (
        "Webcam Cover Set",
        "Small sliding webcam covers for laptops and monitors.",
        "Privacy",
        2.99,
        50,
        "webCover.jpg"
    ),
    (
        "Student Cyber Lab Notebook",
        "A notebook for tracking commands, screenshots, test results, and security notes.",
        "Study Tools",
        12.99,
        25,
        "cyberNotebook.jpg"
    ),
    (
        "Portable USB-C Hub",
        "A compact hub with USB, HDMI, and Ethernet ports for school or lab work.",
        "Accessories",
        39.99,
        12,
        "usbHub.jpg"
    )
]
#Using parameterized queries like in SQL lab for protection from SQL Injections
cursor.executemany("""
INSERT INTO products (name, description, category, price, stock, image)
VALUES (?, ?, ?, ?, ?, ?)
""", products)

connection.commit()
connection.close()

print("Carlos Tech Supply database created successfully.")