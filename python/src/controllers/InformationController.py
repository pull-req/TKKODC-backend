from flask import make_response, jsonify

from flask_restful import Resource, reqparse

from models.Information import Information, InformationSchema
from models.settings import session

class InformationController(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        # Add argument
        self.reqparse.add_argument('x', type=float, required=True)
        self.reqparse.add_argument('y', type=float, required=True)
        self.reqparse.add_argument('image_url', type=str, required=True)
        self.reqparse.add_argument('info', type=str, required=True)

        super(InformationController, self).__init__()

    def get(self):
        results = Information.query.all()
        json_data = InformationSchema(many=True).dump(results)
        return jsonify({
            'informations': json_data
        })
    
    def post(self):
        # Get args
        args = self.reqparse.parse_args()

        # Create model
        information = Information(args.x, args.y, args.image_url, args.info)

        session.add(information)
        session.commit()

        json_data = InformationSchema().dump(information)
        return jsonify({
            'information': json_data
        })