from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Order:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.cookie_type = data["cookie_type"]
        self.quantity = data["quantity"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO orders (name, cookie_type, quantity) VALUES (%(name)s, %(cookie_type)s, %(quantity)s);"
        return connectToMySQL('cookie_orders_schema').query_db(query,data)

    @classmethod
    def get_orders(cls): 
        query = "SELECT * FROM orders;"
        results = connectToMySQL('cookie_orders_schema').query_db(query)
        orders = []
        for order in results:
            orders.append(cls(order))
        return orders
    
    @classmethod
    def obtain_order(cls,data):
        query = "SELECT * FROM orders WHERE id = %(id)s;"
        results = connectToMySQL('cookie_orders_schema').query_db(query,data)
        orders = []
        for order in results:
            orders.append(cls(order))
        return orders[0]
    
    @classmethod
    def update_order(cls,data):
        query = "UPDATE orders SET name = %(name)s, cookie_type = %(cookie_type)s, quantity = %(quantity)s WHERE id = %(id)s;"
        results = connectToMySQL('cookie_orders_schema').query_db(query,data)

    @classmethod
    def delete_order(cls,data): 
        query = "DELETE FROM orders WHERE id = %(id)s;"
        return connectToMySQL('cookie_orders_schema').query_db(query,data)
    
    @staticmethod
    def validate_order(order):
        is_valid = True 
        if len(order['name']) < 2:
            flash("Name must be at least 2 characters long.")
            is_valid = False
        if len(order['cookie_type']) < 2:
            flash("Cookie type must be at least 2 characters long.")
            is_valid = False
        if int(order['quantity']) < 0:
            flash("Number of boxes must be greater than 0.")
            is_valid = False
        return is_valid

