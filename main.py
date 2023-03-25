import json

import psycopg2
from config import host, user, password, db_name
def Main():
    with open("data/categories_item.json", encoding="utf-8") as file:
        category = json.load(file)
    with open("data/all_products.json", encoding="utf-8") as file:
        product = (json.load(file))
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(
                f"""DROP TABLE IF EXISTS categories CASCADE"""
            )

            cursor.execute(
                """CREATE TABLE categories(
                id serial PRIMARY KEY,
                category_name varchar(100) NOT NULL
                );"""
            )
            for i in category:
                cursor.execute(
                    "INSERT INTO categories (id, category_name) VAlUES(%s, %s);", (i["Category_id"], i["Category_name"])
                )
            cursor.execute(
                """DROP TABLE IF EXISTS products"""
            )
            cursor.execute(
               """CREATE TABLE products(
               product_id serial PRIMARY KEY,
               product_name varchar(150) NOT NULL,
               calories varchar(20) NOT NULL,
               proteins varchar(20),
               fats varchar(20),
               carbohydrates varchar(20),
               category_id INTEGER REFERENCES categories (id)
               );"""
            )
            for item in product:
                for i in item:
                    cursor.execute(
                        """INSERT INTO products 
                        (product_id, product_name, calories, proteins, fats, carbohydrates, category_id) 
                        VALUES(%s, %s, %s, %s, %s, %s, %s);""",
                        (i["Product_id"], i["Title"], i["Calories"], i["Proteins"], i["Fats"], i["Carbohydrates"], i["Category_id"])
                    )

    except Exception as _ex:
        print("[INFO] Error PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed")


