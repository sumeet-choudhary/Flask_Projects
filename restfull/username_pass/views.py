from flask import Flask, request, Blueprint, make_response, jsonify
from flask_restful import Resource, Api, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from restfull import api,app
from logging import FileHandler,WARNING
import logging


# app = Flask(__name__)
# api = Api(app)          # __init__

username_pass_blueprint = Blueprint("username_pass_blueprint", __name__)

# logger = logging.getLogger(__name__)
# # file_handler = FileHandler('error_logs.txt')
# file_handler.setLevel(WARNING)
# # restfull.logger.addHandler(file_handler)


# app.logger.addHandler(file_handler)

# # def main() -> None:
# #     logging.basicConfig(level=logging.WARNING)
# #     logging.debug("This is debug message")
# #     logging.info("This is info message")
# #     logging.warning("This is warning message")
# #     logging.error("This is error message")
# #     logging.critical("This is critical message")
def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(pastime)s %(levelness)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logging.debug("This is debug message")
    logging.info("This is info message")
    logging.warning("This is warning message")
    logging.error("This is error message")
    logging.critical("This is critical message")


AllUser = {
    "user1": "Sumeet",
    "user2": "Amit",
    "user3": "Anjali"
}


class Users(Resource):
    def get(self, user_id):
        try:
            if user_id not in AllUser:
                return make_response(jsonify({'message': 'ID doesnt exist cant get it'}))
                # abort(409, message="ID doesnt exist cant get it")
            return AllUser[user_id]
        except Exception as e:
            return make_response(jsonify({'message': str(e)}))

    @jwt_required()
    def delete(self, user_id):
        try:
            if user_id not in AllUser:
                return make_response(jsonify({'message': 'This ID doesnt exist, cant delete it'}))
                # abort(409, message="This ID doesn't exist, cant delete it")
            del AllUser[user_id]
            return make_response(jsonify({'message': '%s has been deleted successfully' % user_id, 'AllUsers': AllUser}))
        except Exception as e:
            return make_response(jsonify({'message': str(e)}))

    def post(self, user_id):
        try:
            if user_id in AllUser:
                return make_response(jsonify({'message': 'This ID is already taken, try putting other'}))
                # abort(409, message="This ID is already taken, try putting other")
            new_value = request.json.get("value", "NA")
            # new_key = request.json.get("key", "NA")
            # new_dict = request.get_json()
            # new_value = new_dict.get('value')
            AllUser[user_id] = new_value
            access_token = create_access_token(identity=user_id)
            return make_response(jsonify({'message': 'New User with both key and value has been added successfully', 'access_token': access_token}))
        except Exception as e:
            return make_response(jsonify({'message': str(e)}))

    @jwt_required()
    def put(self, user_id):
        try:
            if user_id not in AllUser:
                return make_response(jsonify({'message': 'This ID does not exist, cant update it'}))
                # abort(409, message="This ID doesn't exist, cant update it")
            new_value = request.json.get("value", "NA")
            AllUser[user_id] = new_value['value']
            return make_response(jsonify({'message': 'New changes has been added successfully'}))
        except Exception as e:
            return make_response(jsonify({'message': str(e)}))


class OnlyGet(Resource):
    def get(self):
        return AllUser


api.add_resource(Users, '/<user_id>')
api.add_resource(OnlyGet, '/')


# if __name__ == '__main__':
#     app.run(debug=True)         #main.py
