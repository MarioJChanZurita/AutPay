import json
from src import app
from flask import request
from src.services.bill_service import add_bill, update_bill, delete_bill, get_bills, get_bill


@app.route('/bills/addBill', methods=['PUT'])
def create():
    info = json.loads(request.data)
    return add_bill(info)


@app.route('/bills/update/<id>', methods=['PUT'])
def update(bill_id):
    return update_bill(bill_id)


@app.route('/bills/delete/<id>', methods=['DELETE'])
def delete_movie(bill_id):
    return delete_bill(bill_id)


@app.route('/bills/<id>')
def get(bill_id):
    return get_bill(bill_id)


@app.route('/bills/getAll')
def get_all():
    return get_bills()


