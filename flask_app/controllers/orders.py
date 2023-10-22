from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.orders import Order

@app.route('/', methods=['GET', 'POST'])
def home():
    orders = Order.get_orders()
    return render_template('index.html', orders = orders)

@app.route('/new/order')
def add_order():
    return render_template('new_order.html')

@app.route('/add/order', methods=["POST"])
def create_order():
    data = {
        "name" : request.form["name"],
        "cookie_type" : request.form["cookie_type"],
        "quantity" : request.form["quantity"]
    }
    if not Order.validate_order(data):
        return redirect('/new/order')
    Order.save(data)
    return redirect('/')

@app.route('/change/order/<int:id>')
def change_order(id):
    data = {
        "id": id
    }
    order = Order.obtain_order(data)
    return render_template('change_order.html', order = order)

@app.route('/update/order', methods=["POST"])
def update_order():
    data = {
        "id" : request.form["id"],
        "name" : request.form["name"],
        "cookie_type" : request.form["cookie_type"],
        "quantity" : request.form["quantity"]
    }
    if not Order.validate_order(data):
        order = data
        return render_template('change_order.html', order = order)
    Order.update_order(data)
    return redirect('/')

@app.route('/delete/order/<int:id>')
def delete_order(id):
    data = {
        "id" : id
    }
    Order.delete_order(data)
    return redirect('/')