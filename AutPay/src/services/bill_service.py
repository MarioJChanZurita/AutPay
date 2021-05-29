from src.models.bill import Bill
from flask import jsonify, request


def get_bills():
    bill = Bill.objects()
    return jsonify(bill), 200


def add_bill(info):
    bill = Bill(charge=info['charge'],
                total=info['total'])
    bill.save()
    return jsonify(bill.to_json()), 200


def update_bill(bill_id):
    body = request.get_json()
    bill = Bill.objects.get_or_404(id=bill_id)
    bill.update(**body)
    return jsonify(bill.id), 200


def delete_bill(bill_id):
    bill = Bill.objects.get_or_404(id=bill_id)
    bill.delete()
    return jsonify(str(bill.id)), 200


def get_bill(bill_id):
    bill = Bill.objects.first_or_404(id=bill_id)
    return jsonify(bill), 200



# for movie in movies:
  #      movie_dict = movie.to_mongo().to_dict()
   #     movie_dict['created_at'] = movie.created_at.isoformat()
    #    movies_list.append(movie_dict)