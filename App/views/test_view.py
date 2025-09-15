from flask import jsonify
from flask_restful import Resource


class test(Resource):
    def get(self):
        try:
            return jsonify({'code': 404, 'msg': 'test', 'data': None})

        except Exception as e:
            print(e)

            return jsonify({'code': 404, 'msg': 'test', 'data': None})