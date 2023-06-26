#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Plant

app = Flask(__name__)
@@ -17,11 +14,32 @@
api = Api(app)

class Plants(Resource):
    pass
    def get(self):
        plants = Plant.query.all()
        plants_serialized = [plant.to_dict() for plant in plants]
        return jsonify(plants_serialized)

    def post(self):
        data = request.get_json()
        plant = Plant(
            name=data.get('name'),
            image=data.get('image'),
            price=data.get('price')
        )
        db.session.add(plant)
        db.session.commit()
        return jsonify(plant.to_dict()), 201

class PlantByID(Resource):
    pass

    def get(self, id):
        session = db.session
        plant = session.get(Plant, id)
        if plant:
            return jsonify(plant.to_dict())
        return {'message': 'Plant not found'}, 404

api.add_resource(Plants, '/plants')
api.add_resource(PlantByID, '/plants/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)